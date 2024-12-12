from time import sleep


class AudioManager:
    def __init__(s,transitter):
        s.transitter=transitter
        s.emotionName_history=[]
        s.emotionName_2_musicList={
            "happy": ["高兴时歌曲1","高兴时歌曲2"],
            "peace":["peace时歌曲1","peace时歌曲2"],
            "sad": ["sad1","sad2"],
            "angry": ["angry1","angry2"],
            "anxious": ["anxious1","anxious2"],
            "fear": ["fear1","fear2"],
            "bored": ["bored1","bored2"],
        }
        s.INTERVAL=5
        s.curMusicName=""
    def __push(s,cur_emotions):
        emotion=cur_emotions[0]
        max_v=max(list(emotion.values()))
        emotionName=""
        for k,v in emotion.items():
            if(v==max_v):
                emotionName=k
                break
        s.emotionName_history.append(emotionName)#只取一个人的emotion，且取emotion中最大值对应表情名

    def __update(s):
        def emotionName_2_MusicName(emotionName):
            import random
            musicList=s.emotionName_2_musicList[emotionName]
            return musicList[random.randint(0,len(musicList))-1     ]#randint:闭区间，即：a <= N <= b


        lasted_emotionName=s.emotionName_history[-1]
        if(len(s.emotionName_history)==1):
            s.curMusicName=emotionName_2_MusicName(lasted_emotionName)
        if(len(s.emotionName_history)<=s.INTERVAL):
            return
        if(lasted_emotionName==s.emotionName_history[-s.INTERVAL-1]):
            return
        flag_update=True

        for emotionName in s.emotionName_history[-s.INTERVAL:]:
            if(not emotionName==lasted_emotionName):
                flag_update=False
                break
        if(flag_update):
            s.curMusicName=emotionName_2_MusicName(lasted_emotionName)
    def push_and_getCurAudio(s,cur_emotions):
        s.__push(cur_emotions)
        s.__update()
        return s.curMusicName
    def run(self):
        while(1):
            sleep(0.9)
