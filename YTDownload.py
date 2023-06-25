# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 13:11:05 2023

@author: Jagadeesh Damarla
"""

# import youtube_dl
import yt_dlp as youtube_dl


playList = ["https://www.youtube.com/playlist?list=PLjhrDIztP9pf8SpkyZm7XpycUNwp1u8hz"]
ytLink = "https://www.youtube.com/watch?v={}"

dlPath = r"C://Users//DELL//Downloads"

ydl = youtube_dl.YoutubeDL({'dump_single_json': False,
                            'extract_flat' : True,
                            'format': 'bestaudio',  #use it if you want audio only
                            'outtmpl' : dlPath + '/%(title)s.%(ext)s'
                            })

for playlist in playList:

    with  ydl:
        playlist_dict = ydl.extract_info(playlist, download=True)
        for video in playlist_dict["entries"]:
            # print(video["id"])
            print(ytLink.format(video["id"]))
            ydl.download([ytLink.format(video["id"])])
                
        