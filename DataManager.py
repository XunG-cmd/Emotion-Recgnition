import sqlite3
from Utils import *
class DataManager:
    def __init__(s,db_path):
        s.db_path=db_path
        s.connnector = None#懒加载

    def push(s,curEmotion,labeled_image):
        pass
    def getStatistics(s):
        if(s.connnector==None):
            s.connnector = sqlite3.connect(s.db_path)
            DEBUG("数据库打开成功")
            s.cursor = s.connnector.cursor()
    def close(self):
        pass
        # if (not self.connnector == None):
        #     self.connnector.close()