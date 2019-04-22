import download_video as dv
from video_to_images import video_to_pHash


url='https://www.youtube.com/watch?v=lsdrBOZ2Plc'
file_name=dv.download_video(url)
np_array_hash=video_to_pHash(file_name)

dv.delete_video(file_name)
