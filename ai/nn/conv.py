import numpy as np
from pad import pad
from utils import cal_output_size, cal_dilation_size

## for
# def conv2d(input, weight, bias=None, stride=1, padding=0, dilation=1):
#     """卷积

#     Args:
#         input (np.ndarray 输入的网络层
#         weight (int|np.ndarray): kernel卷积核
#         bias ([type], optional): 偏移（没使用到）. Defaults to None.
#         stride (int|np.ndarray, optional): 步长. Defaults to 1.
#         padding (int|np.ndarray, optional): 补边. Defaults to 0.
#         dilation (int|np.ndarray, optional): 扩展\视野域. Defaults to 1.

#     Returns:
#         np.ndarray: 卷积后的输出层
    
#     源码中的jit： https://pytorch.org/tutorials/beginner/Intro_to_TorchScript_tutorial.html
#     c++加载torchscript： https://pytorch.org/tutorials/advanced/cpp_export.html
#     """

#     if padding != 0:
#         input = pad(input, padding)
#     if isinstance(stride, int):
#         stride = (stride, stride)
#     assert len(stride) == 2, 'stride尺寸不对!'
#     if isinstance(dilation, int):
#         dilation = (dilation, dilation)
#     assert len(dilation) == 2, 'dilation尺寸不对!'

#     kernel_shape = weight.shape
#     dilation_size = cal_dilation_size(kernel_shape[-2:], dilation)
#     output_size = cal_output_size(input.shape[-2:], dilation_size, stride)
#     assert np.min(output_size) > 0, 'kernel size不能大于input size!'

#     output = np.zeros((weight.shape[0], *output_size))
#     for i in range(output_size[0]):
#         for j in range(output_size[1]):
#             row, col = i*stride[0],  j*stride[1]
#             out = input[:, row:row+dilation_size[0]:dilation[0], col:col+dilation_size[1]:dilation[1]] * weight
#             output[:, i, j] = np.sum(np.sum(np.sum(out, axis=1), axis=1), axis=1)   # (c, h, w)
#     return output



def conv2d(input, weight, stride=None, padding=0, dilation=1, bias=None):
    """卷积

    Args:
        input (np.ndarray 输入的网络层
        weight (int|np.ndarray): kernel卷积核
        bias ([type], optional): 偏移（没使用到）. Defaults to None.
        stride (int|np.ndarray, optional): 步长. Defaults to 1.
        padding (int|np.ndarray, optional): 补边. Defaults to 0.
        dilation (int|np.ndarray, optional): 扩展\视野域. Defaults to 1.

    Returns:
        np.ndarray: 卷积后的输出层
    """
    # rename
    x = input
    kernel = weight

    # check parameter
    if padding != 0:
        x = pad(x, padding)
    if stride is None:
        stride = kernel.shape[-2:]
    elif isinstance(stride, int):
        stride = (stride, stride)
    assert len(stride) == 2, 'stride尺寸不对!'
    if isinstance(dilation, int):
        dilation = (dilation, dilation)
    assert len(dilation) == 2, 'dilation尺寸不对!'

    # calculate dim
    kernel_shape = kernel.shape
    dilation_size = cal_dilation_size(kernel_shape[-2:], dilation)
    output_size = cal_output_size(x.shape[-2:], dilation_size, stride)
    assert np.min(output_size) > 0, 'kernel size不能大于input size!'

    c, h, w = x.shape
    oo, oi, kh, kw = kernel_shape
    sh, sw = stride
    dh, dw = dilation
    oh, ow = output_size

    shape = (oi, oh, ow, kh, kw)
    strides = np.array([w*h, w*sh, sw, w*dh, dw]) * x.itemsize

    # get matrix block
    y = np.lib.stride_tricks.as_strided(x, shape=shape, strides=strides)

    # cal cnn
    # np.tensordot:
    # (oo, oh, ow) = (oo, oi, kh, kw) * (oi, oh, ow, kh, kw)
    #              = (oo, ?, ?, ?) * (?, oh, ow, ?, ?)
    z = np.tensordot(kernel, y, axes=[(1, 2, 3), (0, 3, 4)])
    return z


if __name__ == "__main__":
    # 构造数据
    img = np.arange(3*4*5).reshape(3, 4, 5)
    input_channel = 3
    output_channel = 4
    e = np.eye(3)
    kernel = np.array([[e, e, e], [e*2, e*2, e*2], [e*3, e*3, e*3], [e*4, e*4, e*4]])

    # 卷积
    img_conv = conv2d(img, kernel, stride=1, dilation=1)

    print(img_conv)

    # 验证
    # import torch
    # import torch.nn.functional as F

    # img = np.arange(3*4*5).reshape(3, 4, 5)
    # e = np.eye(3)
    # k = np.array([[e, e, e], [e*2, e*2, e*2], [e*3, e*3, e*3], [e*4, e*4, e*4]])

    # img = torch.from_numpy(img).double().unsqueeze(0)
    # k = torch.from_numpy(k)
    # print(F.conv2d(img, k))