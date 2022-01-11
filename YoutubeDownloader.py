from tkinter import *
from pytube import YouTube

main = Tk()
main.geometry('500x400')
main.resizable(0,0) #Boolean
main.title('Youtube Video Downloader')

Label(main,text = 'Youtube Video Downloader', font='Arial 15').pack()

path = StringVar()
Label(main, text = 'Specify full path to download to:', font = 'Arial 15').place(x=130, y=60)
pathEnter = Entry(main, width = 70, textvariable= path).place(x=32, y=90)

link = StringVar()
Label(main, text = 'Paste YouTube link here:', font = 'Arial 15').place(x=134, y=120)
linkEnter = Entry(main, width = 70, textvariable= link).place(x=32, y=150)

def VideoDownloader():
    url = YouTube(str(link.get()))
    video = url.streams.first()
    video.download(output_path=str(path.get()))
    Label(main, text = 'Downloaded video', font = 'Arial 15').place(x=160, y=320)

def AudioDownloader():
    url = YouTube(str(link.get()))
    audio = url.streams.get_audio_only()
    audio.download(output_path=str(path.get()))
    Label(main, text = 'Downloaded audio', font = 'Arial 15').place(x=160, y=350)

Button(main, text = 'Download Video', font = 'Arial 15', bg= 'orange', command = VideoDownloader).place(x=160, y=210)
Button(main, text = 'Download Audio', font = 'Arial 15', bg= 'orange', command = AudioDownloader).place(x=162, y=280)

main.mainloop()