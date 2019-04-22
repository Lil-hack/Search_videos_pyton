import  pytube
import time
import threading
import sys,os

def download_video(url):

    # Определяем путь к папке
    SAVE_PATH = sys.path[0] or os.path.dirname(os.path.realpath(sys.argv[0])) or os.getcwd()
    yt = pytube.YouTube(url)
    stream = yt.streams.filter(progressive=True, file_extension='mp4').first()
    stream.download(SAVE_PATH)

    return stream.default_filename

def delete_video(file_name):
    SAVE_PATH = sys.path[0] or os.path.dirname(os.path.realpath(sys.argv[0])) or os.getcwd()

    try:
        os.remove(SAVE_PATH+'\\'+file_name)
    except OSError:
       print(OSError)

    return


if __name__ == '__main__':
    start_time = time.time()
    llist_url=[]
    llist_url.append('https://www.youtube.com/watch?v=jQcN57VFITA')


    threads = []
    for i in range(1):
        t = threading.Thread(target=download_video, args=(llist_url[i],))
        threads.append(t)
        t.start()



    # SAVE_PATH = "/Users/Administrator/PycharmProjects/youtube_video"  # to_do
    #
    # link = "https://www.youtube.com/watch?v=kS2t0kvIMmw"
    # yt = pytube.YouTube(link)
    # stream = yt.streams.first()
    # stream.download(SAVE_PATH)
    print("--- %s seconds ---" % (time.time() - start_time))
