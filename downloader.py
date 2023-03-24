from pytube import YouTube
from sys import argv
from pytube.cli import on_progress
import os
dwpth=os.getcwd()+"\Video"
link=argv[1]

video = YouTube(link, on_progress_callback=on_progress)
descr = video.description
info = descr[:75] + (descr[75:] and '..')
yd_vid = video.streams.get_highest_resolution()
#yd_aud = video.streams.get_audio_only()
print(video.title)
print(info)

user_input = ''
user_input = input(
        'Yes or No  ')
if user_input == 'Yes':
        print('Downloading video...')
        yd_vid.download(dwpth)

quit()

#user_input = ''

#while True:
#    user_input = input(
#        'Pick one: 1) Video | 2) Audio ')

#    if user_input == '1' or "Video" or "video":
#        print('Downloading video...')
 #       yd_vid.download("C:/Users/Bruno/Documents/Youtube downloader/Video")
 #       yd_vid.on_progress
 #       break
 #   elif user_input == '2' or "Audio" or "audio":
 #       print('Downloading audio...')
 #       yd_aud.download("C:/Users/Bruno/Documents/Youtube downloader/Audio")
  #      break
