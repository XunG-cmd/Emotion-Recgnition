import cv2
import numpy as np
class Image:
    def __init__(self,path):
        self.data=path
    def get_path_and_img0(self):#传递给myDect.py的detect函数的是path 和 img0
        # cv2的imread读中文路径会失败
        return self.data,cv2.imdecode(np.fromfile(self.data, dtype=np.uint8), cv2.IMREAD_COLOR)#cv2.IMREAD_COLOR:若为4通道，也只读取3通道。因为4通道灌进网络会炸
