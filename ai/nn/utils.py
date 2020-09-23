import numpy as np

def cal_output_size(input_size, kernel_size, stride=None, padding=(0, 0)):
    '''
        计算卷积后的尺寸
    '''
    stride = stride if stride else kernel_size
    input_size, kernel_size, stride, padding = list(map(np.array, [input_size, kernel_size, stride, padding]))  # to numpy

    output_shape = (input_size - kernel_size + padding) // stride + 1
    return output_shape


def cal_dilation_size(kernel_size, dilation=1):
    '''
        计算空洞卷积感受野尺寸
    '''
    if isinstance(dilation, int):
        dilation = (dilation, dilation)
    kernel_size, dilation = list(map(np.array, [kernel_size, dilation]))

    return (dilation - 1) * (kernel_size - 1) + kernel_size