import numpy as np
import cv2, pafy
import time
import youtube_dl

def get_photo_fromYT(url, frame):
    # url = "https://www.youtube.com/watch?v=seI9H18ZvgE"
    videoPafy = pafy.new(url)
    best = videoPafy.getbest()

    cap = cv2.VideoCapture(best.url)
    cap.set(25, frame)
    ret, frame = cap.read()


    return frame

#print(get_photo_fromYT("https://www.youtube.com/watch?v=helu9J9uf9Y",500))