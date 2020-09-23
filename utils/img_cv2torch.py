import cv2
import torch
import torchvision.transforms as T

def cv_to_tensor(img):
    '''
        opencv numpy.ndarray -> torch tensor
    '''
    # imgrgb = img[:, :, ::-1]
    if img.dtype != np.float32:
        img = img.astype(np.float32)
    imgrgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    transform = T.Compose([
        T.ToTensor()
    ])
    imgt = transform(imgrgb)
    return imgt

def tensor_to_cv(img):
    '''
        torch tensor -> opencv numpy.ndarray
    '''
    img = img.numpy()
    img = img.transpose((1, 2, 0))
    imgbgr = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    return imgbgr
