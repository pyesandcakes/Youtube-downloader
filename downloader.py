from pytube import YouTube
from sys import argv
from pytube.cli import on_progress
import os
dwpth_vid=os.getcwd()+"\Video"
dwpth_aud=os.getcwd()+"\Audio"
link=argv[1]
print("Searching...")
video = YouTube(link, on_progress_callback=on_progress)
audio = YouTube(link, on_progress_callback=on_progress)
descr = video.description
info = descr[:100] + (descr[100:] and '..')
yd_vid = video.streams.get_highest_resolution()
yd_aud = audio.streams.get_audio_only()
print(video.title)
print(info)

user_input = ''
user_input = input('Pick one: 1) Video | 2) Audio ')

if user_input == '1':
        print('Downloading video...')
        yd_vid.download(dwpth_vid)
        yd_vid.on_progress
       
elif user_input == '2':
        print('Downloading audio...')
        yd_aud.download(dwpth_aud)
        yd_aud.on_progress
quit()

