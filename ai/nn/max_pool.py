import numpy as np
from pad import pad
from utils import cal_output_size

def max_pool2d(input, kernel_size, stride=None, padding=0):
    if padding != 0:
        input = pad(input, padding)
    if isinstance(kernel_size, int):
        return max_pool2d(input, (kernel_size, kernel_size), stride, padding)
    assert len(kernel_size) == 2, 'kernel size尺寸不对!'

    if stride is None:
        stride = kernel_size
    assert len(stride) == 2, 'stride尺寸不对!'

    output_size = cal_output_size(input.shape[1:], kernel_size, stride)
    output = np.zeros((input.shape[0], *output_size))
    for i in range(output_size[0]):
        for j in range(output_size[1]):
            row, col = i*stride[0],  j*stride[1]
            output[:, i, j] = np.max(np.max(input[:, row:row+kernel_size[0],col:col+kernel_size[1]], axis=1), axis=1)   # (c, h, w)
    return output


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    # 建个灰度图便于查看
    img = ((np.random.randn(10, 20, 3)+1)/2).clip(0, 1)
    im = (img[:,:,0] + img[:,:,1] + img[:,:,2]) / 3
    img = np.stack([im, im, im], axis=2)
    img0 = img.copy()
    img = img.transpose([2, 0, 1])  # (h, w, c) -> (c, h, w)

    img_max_pool = max_pool2d(img, (3, 3), (3, 3))
    img_max_pool = img_max_pool.transpose([1, 2, 0])  # (c, h, w) -> (h, w, c)

    plt.subplot(1, 2, 1)
    plt.imshow(img0)
    plt.subplot(1, 2, 2)
    plt.imshow(img_max_pool)
    plt.show()

