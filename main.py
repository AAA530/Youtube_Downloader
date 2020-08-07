from pytube import YouTube
import pytube
import sys
import eel

eel.init("Frontend")

@eel.expose
def alert_value(x):
    return x


def percent(tem, total):
    perc = (float(tem) / float(total)) * float(100)
    return perc


def progress_function(stream, chunk, bytes_remaining):
    q = int(round((1 - bytes_remaining / video.filesize) * 100, 3))
    print(q, '% done...')
    eel.progress(q)

    


def convert_to_aac(stream, file_handle):
    print("Download completed")
    

# input() #sys.argv[1]  #'https://www.youtube.com/watch?v=v2-9rIL_f4w'
@eel.expose
def start(video_link):
    link_video = video_link


    yt = YouTube(link_video,
                on_progress_callback=progress_function)

    yt.register_on_complete_callback(convert_to_aac)
    # print(link_video)
    # yt = YouTube(link_video)

    title = yt.title
    streams = yt.streams.filter(progressive=True).order_by('resolution').desc()
    print(streams)

    print("Enter number 1 to " + str(len(streams)))
    i = 1 #int(input())
    print(streams[i-1])
    global video
    video = streams[i - 1]
    video.download(r'C:\Users\asus\Desktop\Youtube')



eel.start("index.html",size=(500,500))




# stream = yt.streams.filter(res='720p').first()
# print(yt.streams.filter(progressive='True'))
# stream.download(r'C:\Users\asus\Desktop\Youtube')
