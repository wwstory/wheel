import cv2
import random

def draw_bbox(bbox, img, mode='x1y1x2y2', is_scale=False, color=None, label=None, line_thickness=None):
    '''
        mode: x1y1x2y2 | x1y1wh | cxcywh
    '''
    # 配置
    color = color or [random.randint(0, 255) for _ in range(3)]

    # 解bbox
    if mode == 'x1y1x2y2':
        x1, y1, x2, y2 = bbox
        c1, c2 = (x1, y1), (x2, y2)
    elif mode == 'x1y1wh':
        x1, y1, w, h = bbox
        c1, c2 = (x1, y1), (min(x1 + w, img.shape[1]), min(y1 + h, img.shape[0]))
    elif mode == 'cxcywh':
        cx, cy, w, h = bbox
        c1, c2 = (max(cx - w / 2, 0), max(cy - h / 2, 0)), (min(cx + w / 2, img.shape[1]), min(cy + h / 2, img.shape[0]))
    else:
        assert False, '没有这个画框模式！'
    # 解归一化
    if is_scale:
        c1 = (c1[0] * img.shape[1], c1[1] * img.shape[0])
        c2 = (c2[0] * img.shape[1], c2[1] * img.shape[0])
    
    c1, c2 = tuple(map(int, c1)), tuple(map(int, c2))

    # 绘制
    line_thickness = line_thickness or 1
    cv2.rectangle(img, c1, c2, color, thickness=line_thickness, lineType=cv2.LINE_AA)
    if label:
        label = str(label)
        t_size = cv2.getTextSize(label, 0, fontScale=line_thickness / 3, thickness=line_thickness)[0]
        c2 = c1[0] + t_size[0], c1[1] - t_size[1] - 3
        cv2.rectangle(img, c1, c2, color, -1, cv2.LINE_AA)  # filled
        cv2.putText(img, label, (c1[0], c1[1] - 2), 0, line_thickness / 3, [225, 255, 255], thickness=line_thickness, lineType=cv2.LINE_AA)
    return img


if __name__ == "__main__":
    """
        >>> python3 draw_bbox.py --img_path="/tmp/test.jpg" --bbox="0.1 0.2 0.3 0.4"
    """
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--img_path', default='/tmp/test.jpg')
    parser.add_argument('--bbox', default='0 0 0 0')
    parser.add_argument('--txt', default='')
    parser.add_argument('--mode', default='cxcywh')
    parser.add_argument('--out_path', default='')
    parser.add_argument('--color', default='100 100 255')
    args = parser.parse_args()

    # 加载图
    img = cv2.imread(args.img_path)
    # 设置边框和文本
    bbox = list(map(float, (args.bbox.split())))
    label = args.txt
    mode = args.mode
    out_path = args.out_path
    color = list(map(float, (args.color.split())))
    is_scale = sum(bbox) < 4
    # 绘制
    out_img = draw_bbox(bbox, img, mode=mode, is_scale=is_scale, label=label, color=color, line_thickness=1)
    # 保存
    if out_path:
        cv2.imwrite(out_path, out_img)
    cv2.imshow('', out_img)
    while True:
        if cv2.waitKey(1) != -1:
            break
    cv2.destroyAllWindows()