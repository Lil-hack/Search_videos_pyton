import numpy as np
import cv2
import imagehash
from PIL import Image
import time
import json
import sys
import io

def video_to_pHash(video_name, uuid=0):

    cap = cv2.VideoCapture(video_name)
    keys = 'uuid', 'hash', 'frame'
    mas_hash = []
    i=0
    while True:
        i=i+1
        ret, frame = cap.read()

        if not ret:
            break
        img = Image.fromarray(frame)
        hash = imagehash.phash(img, 8)

        values=uuid,str(hash),i
        video_item = dict(zip(keys, values))

        mas_hash.append(video_item)

    np_data = np.asarray(mas_hash)

    return np.unique(np_data)


start_time = time.time()
print(video_to_pHash('Whatsapp Love Status Video2017(20Sec).mp4',0))
print("--- %s seconds main ---" % (time.time() - start_time))