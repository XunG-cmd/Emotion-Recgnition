from time import sleep
import  os
from Utils import *
from Types import *
from logging import debug as DEBUG
class Receiver:
    def __init__(s):
        s.t_path="./res_test"
        s.test =os.listdir(s.t_path)
        DEBUG("./res_test:",s.test)
        assert not s.test==[]
        s.test_i=-1
    def receive(s):#block
        sleep(0.3)
        s.test_i=(s.test_i+1)%(len(s.test))
        return Image(os.path.join( s.t_path,s.test[s.test_i] ))
    def close(self):
        pass