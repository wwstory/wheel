import numpy as np

def pad(input, padding, mode='constant', value=0):
    '''
        padding - [left, right, top, bottom]
        mode - 'constant', 'replicate'
    '''
    if len(padding) == 4:
        c, h, w = input.shape
        l, r, t, b = padding
        if 'constant' == mode:
            padding_lr = np.ones((c, h, 1)) * value
            input = np.concatenate((*[padding_lr.copy() for _ in range(l)], input, *[padding_lr.copy() for _ in range(r)]), axis=2) # c, h, w
            padding_tb = np.ones((c, 1, w+(l+r))) * value
            input = np.concatenate((*[padding_tb.copy() for _ in range(t)], input, *[padding_tb.copy() for _ in range(b)]), axis=1) # c, h, w
        elif 'replicate' == mode:
            padding_left = input[:,:,:1]
            padding_right = input[:,:,-1:]
            input = np.concatenate((*[padding_left.copy() for _ in range(l)], input, *[padding_right.copy() for _ in range(r)]), axis=2)    # c, h, w
            padding_top = input[:,:1:]
            padding_bottom = input[:,-1:,:]
            input = np.concatenate((*[padding_top.copy() for _ in range(t)], input, *[padding_bottom.copy() for _ in range(b)]), axis=1)    # c, h, w
    elif len(padding) == 2:   # 仅在宽上加
        return pad(input, (*padding, 0, 0), mode, value)
    else:
        assert len(padding) in (2, 4), '输入input的pad维度有误!'
    return input



if __name__ == "__main__":
    import matplotlib.pyplot as plt
    # 建个灰度图便于查看
    img = ((np.random.randn(3, 10, 20)+1)/2).clip(0, 1)
    im = (img[0,:,:] + img[1,:,:] + img[2,:,:]) / 3
    img = np.stack([im, im, im])
    img0 = img.copy()
    img0 = img0.transpose((1, 2, 0))    # (c, h, w) -> (h, w, c)

    img_pad = pad(img, (1, 2, 3, 4), mode='constant')
    img_pad = img_pad.transpose((1, 2, 0))  # (c, h, w) -> (h, w, c)

    plt.subplot(1, 2, 1)
    plt.imshow(img0)
    plt.subplot(1, 2, 2)
    plt.imshow(img_pad)
    plt.show()
