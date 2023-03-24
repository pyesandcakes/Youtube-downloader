from pytube import YouTube
from pytube.cli import on_progress
import os
from pytube import Channel
from pytube import Playlist

dwpth_vid=os.getcwd()+"\Video"
dwpth_vid_pl=os.getcwd()+"\Video\Playlists"
dwpth_aud_pl=os.getcwd()+"\Audio\Playlists"
dwpth_aud=os.getcwd()+"\Audio"

one_input=""
one_input=input("Download: 1) One Video | 2) Whole Channel | 3) Playlist ")
if one_input == "2":
        print("Channel download currently not working. WiP")
        # ch_link = input("Input channel URL ")+"/videos"
        # c= Channel(ch_link)
        # dwpth_vid_chan=os.getcwd()+"\Video"+"\ "+c.channel_name
        # print("Downloading from",c.channel_name)
        # for video in c.videos:
        #         video.register_on_progress_callback(on_progress)
        #         c=video.streams.get_highest_resolution()
        #         print(video.title)
        #         print()
        #         c.download(dwpth_vid_chan)
        #         print()
        #         c.on_progress
        #         print()
                
if one_input == "1":
        link=input("Insert URL ")
        print("Searching...")
        vid = YouTube(link, on_progress_callback=on_progress)
        audio = YouTube(link, on_progress_callback=on_progress)
        descr = vid.description
        info = descr[:100] + (descr[100:] and '..')
        yd_vid = vid.streams.get_highest_resolution()
        yd_aud = audio.streams.get_audio_only()
        print(vid.title)
        print(info)
        user_input = ''
        user_input = input('Pick one: 1) Video | 2) Audio ')
        if user_input == '1':
                print('Downloading video...')
                yd_vid.download(dwpth_vid)
                yd_vid.on_progress
                print("\n Download finished. \n Find files in", dwpth_vid)
        elif user_input == '2':
                print('Downloading audio...')
                yd_aud.download(dwpth_aud)
                yd_aud.on_progress
                print("\n Download finished. \n Find files in", dwpth_aud)
if one_input == "3":
        pl_link=input("Insert playlist URL ")
        print("Searching...")
        pl_str = Playlist(pl_link)
        print("Found",pl_str.title)
        pth=pl_str.title
        pth=pth.replace(" ", "")
        print(pl_str.length,"videos found.")
        user_input = ''
        user_input = input('Pick one: 1) Video | 2) Audio ')
        if user_input == '1':
                print('Downloading videos...')
                dwpth_vid_pl +="\\"+pth
                for video in pl_str.videos:
                        video.register_on_progress_callback(on_progress)
                        pl_str=video.streams.get_highest_resolution()
                        print(video.title)
                        print()
                        pl_str.download(dwpth_vid_pl)
                        print()
                        pl_str.on_progress
                        print()
                print("\n Download finished. \n Find files in", dwpth_vid_pl)
        elif user_input == '2':
                print('Downloading audio...')
                dwpth_aud_pl +="\\"+pth
                for video in pl_str.videos:
                        video.register_on_progress_callback(on_progress)
                        pl_str=video.streams.get_audio_only()
                        print(video.title)
                        print()
                        pl_str.download(dwpth_aud_pl)
                        print()
                        pl_str.on_progress
                        print()
                print("\n Download finished. \n Find files in", dwpth_aud_pl)
input()