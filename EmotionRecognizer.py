from time import sleep
from Utils import *
from Types import *
from EmotionRecognition.myDetect import detect_1_image
from  Utils import *
class EmotionRecognizer:
    def __init__(self):
        pass
    def run(self, queue_reader,queue_writer):
        while(1):
            received_image=queue_reader.get(block=True)


            # sleep(0.5)
            # catagory_and_score=[('Affection', 0.04973757266998291), ('Anger', 0.02718622237443924), ('Annoyance', 0.030253415927290916), ('Anticipation', 0.1748184859752655), ('Aversion', 0.02683388441801071), ('Confidence', 0.12836091220378876), ('Disapproval', 0.02994699217379093), ('Disconnection', 0.06535092741250992), ('Disquietment', 0.03013644367456436), ('Doubt/Confusion', 0.039525486528873444), ('Embarrassment', 0.024798080325126648), ('Engagement', 0.5389661192893982), ('Esteem', 0.04029819369316101), ('Excitement', 0.13987866044044495), ('Fatigue', 0.03002157062292099), ('Fear', 0.02148306928575039), ('Happiness', 0.2587452828884125), ('Pain', 0.025066174566745758), ('Peace', 0.0740569606423378), ('Pleasure', 0.08617840707302094), ('Sadness', 0.032596178352832794), ('Sensitivity', 0.028783222660422325), ('Suffering', 0.02878359705209732), ('Surprise', 0.03023453988134861), ('Sympathy', 0.03721519932150841), ('Yearning', 0.037629153579473495)]
            #
            # labeled_image=r"E:\APP_projects_and_files\py\工创V  服务端\EmotionRecognizer\emotic-main\images\trump.gif"
            #


            l_catagory_and_score,labeled_image=detect_1_image(*(received_image.get_path_and_img0()))
            # l_catagory_and_score=   [ [('Affection', 0.04973757266998291), ('Anger', 0.02718622237443924), ('Annoyance', 0.030253415927290916), ('Anticipation', 0.1748184859752655), ('Aversion', 0.02683388441801071), ('Confidence', 0.12836091220378876), ('Disapproval', 0.02994699217379093), ('Disconnection', 0.06535092741250992), ('Disquietment', 0.03013644367456436), ('Doubt/Confusion', 0.039525486528873444), ('Embarrassment', 0.024798080325126648), ('Engagement', 0.5389661192893982), ('Esteem', 0.04029819369316101), ('Excitement', 0.13987866044044495), ('Fatigue', 0.03002157062292099), ('Fear', 0.02148306928575039), ('Happiness', 0.2587452828884125), ('Pain', 0.025066174566745758), ('Peace', 0.0740569606423378), ('Pleasure', 0.08617840707302094), ('Sadness', 0.032596178352832794), ('Sensitivity', 0.028783222660422325), ('Suffering', 0.02878359705209732), ('Surprise', 0.03023453988134861), ('Sympathy', 0.03721519932150841), ('Yearning', 0.037629153579473495)]]
            # labeled_image=None



            DEBUG(labeled_image)

            queue_writer.put(   (l_catagory_and_score,labeled_image)  )