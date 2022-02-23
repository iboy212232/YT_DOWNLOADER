import pytube
import os
print("Audio czy Wideo")
wybor=input("")
link = input("podaj link ")
katalog_dom = os.path.expanduser('~')

yt = pytube.YouTube(link) 
if wybor == "Audio" or wybor =="audio":
    yt.streams.filter(only_audio=True).first().download(katalog_dom+'\Downloads')
else:
    yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(katalog_dom+'\Downloads')