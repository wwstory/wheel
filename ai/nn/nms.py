from iou import iou

def nms(bbox, threshold):
    bbox = sorted(bbox, key=lambda x:x[-1])
    remain = []
    while bbox:
        i = len(bbox) - 2
        while i >= 0:
            score = iou(bbox[-1][:4], bbox[i][:4])
            if score > threshold:
                bbox.pop(i)
            i -= 1
        remain.append(bbox.pop())
    return remain


if __name__ == "__main__":
    import cv2

    bbox = [
        [48, 2, 218, 172, 0, 0.97],
        [303, 126, 437, 228, 1, 0.41],
        [75, 87, 191, 172, 0, 0.7],
        [216, 121, 344, 239, 1,  0.56],
        [29, 61, 135, 164, 0, 0.4],
        [283, 164, 373, 250, 1,  0.73],
        [93, 48, 238, 206, 0, 0.64],
        [269, 86, 426, 252, 1, 0.97],
    ]
    new_bbox = nms(bbox, 0.2)
    print('nms:', new_bbox)

    img = cv2.imread('../../tmp/megumin.jpg')
    img0 = img.copy()

    # init
    for box in bbox:
        if box[-2] == 0:
            cv2.rectangle(img, tuple(box[:2]), tuple(box[2:4]), [255, 100, 100], 2)
        else:
            cv2.rectangle(img, tuple(box[:2]), tuple(box[2:4]), [100, 255, 100], 2)
        cv2.imshow('', img)
        cv2.waitKey(100)
    cv2.waitKey(1000)
    # nms
    img = img0
    for box in new_bbox:
        if box[-2] == 0:
            cv2.rectangle(img, tuple(box[:2]), tuple(box[2:4]), [255, 100, 100], 2)
        else:
            cv2.rectangle(img, tuple(box[:2]), tuple(box[2:4]), [100, 255, 100], 2)
        cv2.imshow('', img)
        cv2.waitKey(100)

    while True:
        if cv2.waitKey(1) != -1:
            break
    cv2.destroyAllWindows()