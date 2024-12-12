import os
from PIL import Image as im
from PIL import ImageTk
from tkinter import Tk,Label,Frame
from tkinter.constants import *
class BeautifulButton(Label):#原生Button太丑了，用Label
    def __init__(self,root, text , command,height=1 ,fg="white",bg="black",   font=("宋体", 30)):
        Label.__init__(self ,root,height=height , fg=fg ,bg=bg, text=text , font=font )
        self.bind('<Button-1>',command)
class GUI:
    def __init__(s,onClickStatistics ,onClose ):
        # 创建窗口
        root =  Tk()
        # 设置标题
        root.title(f'Emotion')
        root.state('zoomed')
        root["bg"] = "Black"

        frame_lb = Frame(root)
        frame_lb.pack(side=RIGHT, fill=Y)


        message_label = Label(frame_lb, height=2, fg="black", text="initializing", font=("黑体", 30))
        message_label.pack(side=LEFT, fill=Y)

        frame_btn = Frame(root)
        frame_btn.pack(side=BOTTOM, fill=X)
        btn_add = BeautifulButton(frame_btn, text="setting", command=onClickStatistics)
        btn_add.grid(sticky=NSEW,padx=(5,5),pady=(5,5) )
        btn_remove = BeautifulButton(frame_btn, text="show data", command=onClickStatistics)
        btn_remove.grid(row=0, column=1, sticky=NSEW,padx=(5,5),pady=(5,5) )

        pic_label = Label(root)
        pic_label.pack(side=TOP, expand=True, fill=BOTH)
        #退出时持久化
        root.protocol('WM_DELETE_WINDOW', s.close)


        ###
        import ctypes
        # 告诉操作系统使用程序自身的dpi适配
        ctypes.windll.shcore.SetProcessDpiAwareness(1)
        # 获取屏幕的缩放因子
        ScaleFactor = ctypes.windll.shcore.GetScaleFactorForDevice(0)
        # 设置程序缩放
        root.tk.call('tk', 'scaling', ScaleFactor / 75)

        # 必须在这之后才能显示图片
        root.update()
        s.max_w = pic_label.winfo_width()
        s.max_h = pic_label.winfo_height()
        ###self
        s.onClose=onClose
        s.onClickStatistics=onClickStatistics
        s.root=root
        s.pic_label=pic_label
        s.message_label=message_label

    def setPic(s,path):  # 调用前请确保该图片存在
        global pic
        raw_pic = im.open(path)
        # 调整图片
        w, h = raw_pic.size
        if (w > s.max_w):
            raw_pic = raw_pic.resize((s.max_w, int(h / w * s.max_w)))
        w, h = raw_pic.size
        if (h > s.max_h):
            raw_pic = raw_pic.resize((int(w / h * s.max_h), s.max_h))
        # 显示图片
        pic = ImageTk.PhotoImage(raw_pic)
        s.pic_label["image"] = pic

    def setLabel(s,l_curEmotion, curMusicName):#l_curEmotion:[每张脸的emotion,……]
        text=""
        for  curEmotion in l_curEmotion:
            text+="\n"
            for key  in curEmotion:
                text=text+f"{key}:{round(curEmotion[key],4)}\n"
        text+="\n\ncurrent Music Name: {}".format(curMusicName)
        s.message_label.configure(text=text, fg="black",bg="Azure")

    def update(s,curEmotion,labeled_image,curMusicName):
        s.setPic(labeled_image)
        s.setLabel(curEmotion,curMusicName)
    def run(self ):
        self.root.mainloop()
    def close(self):
        self.onClose()
        self.root.destroy()
    def onClickStatistics(self):
        self.onClickStatistics()

if __name__ == '__main__':
    def tt(*args):
        print("t")
    gui = GUI(onClickStatistics=tt, onClose=tt)

    import  threading
    thread_gui = threading.Thread(target= gui.run)
    thread_gui.start()
    gui.update(curEmotion={"happy":0.1,"peace":0,"sad":0,"angry":0,"anxious":0.5, "fear":0,"bored":0.15}
                ,labeled_image=r"E:\APP_projects_and_files\py\工创V  服务端\EmotionRecognizer\emotic-main\images\trump.gif")



