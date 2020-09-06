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
    cv2.rectangle(img, c1, c2, color, thickness=line_thickness, lineType=cv2.LINE_AA)
    if label:
        t_size = cv2.getTextSize(label, 0, fontScale=line_thickness / 3, thickness=line_thickness)[0]
        c2 = c1[0] + t_size[0], c1[1] - t_size[1] - 3
        cv2.rectangle(img, c1, c2, color, -1, cv2.LINE_AA)  # filled
        cv2.putText(img, label, (c1[0], c1[1] - 2), 0, line_thickness / 3, [225, 255, 255], thickness=line_thickness, lineType=cv2.LINE_AA)
    return img


if __name__ == "__main__":
    # 加载图
    img = cv2.imread('/tmp/test.jpg')
    # 设置边框和文本
    bbox = [519, 103, 6, 15]
    bbox = [0.652343, 0.379166, 0.121875, 0.247222]
    bbox = [0.640938, 0.897200, 0.640188, 0.089882]
    label = 'this'
    # 绘制
    out_img = draw_bbox(bbox, img, mode='cxcywh', is_scale=True, label=label, color=[0, 170, 140], line_thickness=1)
    # 保存
    cv2.imwrite('/tmp/out.jpg', out_img)