import sys, os

print(__file__)
print(os.path.dirname(__file__))
sys.path.append(os.path.join(os.path.dirname(__file__), "EmotionRecognition"))
print(sys.path)




from multiprocessing import  Process,Queue
import threading
from Utils import *
from Types import *
from DataManager import DataManager
from GUI import GUI
from Transmitter import Transmitter
from Receiver import Receiver
from EmotionRecognizer import EmotionRecognizer
from AudioManager import AudioManager


class App():
    def __init__(s):
        ###组件
        s.receiver=Receiver()
        s.transitter=Transmitter()
        s.audioManager=AudioManager(transitter=s.transitter)
        s.dataManager=DataManager(db_path="./db1.db")
        s.emotionRecognizer=EmotionRecognizer()
        s.gui=GUI(onClickStatistics=lambda s:s.getStatistics(s),onClose=s.close   )
        ###thread_app
        thread_app=threading.Thread(target=s.run,daemon=True  )
        thread_app.start()
        s.gui.run()


    def run(s):

        ### audioManager
        thread_audioManager=threading.Thread(target=s.audioManager.run,daemon=True  )
        thread_audioManager.start()
        ###EmotionRecognizer
        q1=Queue()
        q2=Queue()
        queue_reader=q1
        queue_writer=q2
        process_emotionRecognizer = Process(target=s.emotionRecognizer.run,args=( q2,q1))
        process_emotionRecognizer.start()
        s.process_emotionRecognizer=process_emotionRecognizer

        while(1):
            DEBUG("loop")
            received_image=s.receiver.receive()
            ##
            queue_writer.put(received_image)
            l_catagory_and_score,labeled_image=queue_reader.get(block=True)
            DEBUG(11)
            DEBUG(labeled_image)
            DEBUG(l_catagory_and_score)
            ##
            l_cur_emotions=s.get_emotions(l_catagory_and_score)
            DEBUG(labeled_image)
            s.dataManager.push(l_cur_emotions,labeled_image)
            curAudio=s.audioManager.push_and_getCurAudio(l_cur_emotions)
            s.gui.update(l_cur_emotions,labeled_image,curAudio)

    def get_emotions(self,l_catagory_and_score):
        DEBUG(l_catagory_and_score)

        def catagory_and_score_2_emotion(catagory_and_score):
            ret={}
            dic_catagory_and_score={}
            for tuple in catagory_and_score:
                dic_catagory_and_score[tuple[0]]=tuple[1]
            key_2_weight={
                "happy":{"Excitement":2,"Happiness":2,"Surprise":2,"Pleasure":2,"Affection":2,"Anticipation":2},
                "peace":{"Peace":6 },
                "sad":{"Pain":6,"Suffering":6,"Sympathy":3,"Sadness":6,"Sensitivity":6},
                "angry":{"Anger":6,"Annoyance":6,"Aversion":3,"Disapproval":6},
                "anxious":{"Disquietment":6,"Embarrassment":6,"Yearning":6},
                "fear":{"Fear":6,"Doubt/Confusion":6},
                "bored":{"Disconnection":6,"Fatigue":6}
            }
            # key_2_weight.keys():  ["happy","peace","sad","angry","anxious","fear","bored"]
            for key,val in key_2_weight.items():
                ret[key]=0
                dic_weight=val# {"Peace":6,"Engagement":6}
                for _key,_val in dic_weight.items(): #_val:权重，eg.  6   3
                    ret[key]+=_val*dic_catagory_and_score[_key]
            # return {"happy": 0.1, "peace": 0, "sad": 0, "angry": 0, "anxious": 0.5, "fear": 0, "bored": 0.15}
            return  ret

            # 开心类（好运来）：excitment + happiness + suprise + pleasure + affection + 0.5
            # anticipation
            # 平静、宁静、专注类（搞点纯音乐）：peace + engagement
            # 伤心、痛苦类（大悲咒）：pain + suffering + 0.5
            # sympathy + sadness + sensitivity
            # 生气，愤怒，反对类（听我说谢谢你）：anger + annoyance + 0.5
            # aversion + Disapproval
            # 焦虑、渴望、尴尬类：disquietment + enbarrassment + Yearning
            # 害怕、怀疑（搞点搞笑音乐）：fear + Doubt / Confusion
            # 走神、无聊、疲劳（专注歌单）：disconnection，fatigue



        l_cur_emotions=[]
        for catagory_and_score in l_catagory_and_score:
            l_cur_emotions.append(  catagory_and_score_2_emotion(catagory_and_score)  )
        return l_cur_emotions
    def getStatistics(s):
        s.dataManager.getStatistics()
    def close(s):
        s.transitter.close()
        s.receiver.close()
        s.dataManager.close()
        # s.process_emotionRecognizer.close()#error

if __name__ == '__main__':

    app=App()




