from pytube import YouTube
import pytube
import sys


def percent(tem, total):
    perc = (float(tem) / float(total)) * float(100)
    return perc


def progress_function(stream, chunk, bytes_remaining):
    print(round((1-bytes_remaining/video.filesize)*100, 3), '% done...')


def convert_to_aac(stream, file_handle):
    print("Download completed")
    sys.stdout.flush()

link_video = sys.argv[1]  #'https://www.youtube.com/watch?v=v2-9rIL_f4w'


yt = YouTube(link_video,
             on_progress_callback=progress_function,
             register_on_complete_callback=convert_to_aac)


title = yt.title
streams = yt.streams.filter(progressive=True).order_by('resolution').desc()
print(streams)

print("Enter number 1 to " + str(len(streams)))
i = 1 #int(input())
print(streams[i-1])
video = streams[i - 1]
video.download(r'C:\Users\asus\Desktop\Youtube')






# stream = yt.streams.filter(res='720p').first()
# print(yt.streams.filter(progressive='True'))
# stream.download(r'C:\Users\asus\Desktop\Youtube')
