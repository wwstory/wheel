def iou(rect1, rect2):
    '''
        计算iou
    '''
    gxmin, gymin, gxmax, gymax = rect1
    pxmin, pymin, pxmax, pymax = rect2

    # if (gxmax < pxmin and gymax < pymin) or (pxmax < gxmin and pymax < gymin):  # 上下左右错开的情况，iou计算出来为正值
    #     return 0.

    xmin = max(gxmin, pxmin)
    ymin = max(gymin, pymin)
    xmax = min(gxmax, pxmax)
    ymax = min(gymax, pymax)

    if xmax - xmin < 0 or ymax - ymin < 0:  # 没有相交区域
        return 0.

    S_cross = (xmax - xmin) * (ymax - ymin)
    S1 = (gxmax - gxmin) * (gymax - gymin)
    S2 = (pxmax - pxmin) * (pymax - pymin)

    iou = (S_cross) / (S1 + S2 - S_cross)

    return iou


if __name__ == "__main__":
    li1 = [
        [10, 20, 30, 40],
        [10, 20, 30, 40],
        [10, 20, 30, 40],
        [50, 51, 180, 200],
        [46, 55, 171, 200],
    ]
    li2 = [
        [50, 60, 70, 80],
        [20, 30, 40, 50],
        [30, 40, 50, 60],
        [48, 53, 170, 210],
        [200, 51, 242, 81],
    ]
    for l1, l2 in zip(li1, li2):
        print(iou(l1, l2))

    # import cv2
    # import numpy as np
    # import random
    # img = np.zeros((300, 300, 3))
    # for l1, l2 in zip(li1, li2):
    #     score = iou(l1, l2)
    #     color = [random.random() for _ in range(3)]
    #     cv2.rectangle(img, tuple(l1[:2]), tuple(l1[2:]), color, thickness=1)
    #     cv2.rectangle(img, tuple(l2[:2]), tuple(l2[2:]), color, thickness=1)
    #     cv2.putText(img, str(score), (10, 10), 0, 0.3, color)
    #     cv2.imshow('', img)
    #     cv2.waitKey(1000)
    #     img[::]=0
    # while True:
    #     if cv2.waitKey(1) != -1:
    #         break
    # cv2.destroyAllWindows()