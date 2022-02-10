from tkinter import *
from pytube import YouTube

display=Tk()
display.geometry('500x300')
display.resizable(0,0)
display.title('Youtube_Video Downloader')

Label(display,text='Youtube_Video Downloader',font='arial 20 bold').pack()


link=StringVar()
Label(display,text='Paste your link Here: ',font='arial 15 bold').place(x=160,y=60)
link_enter = Entry(display,width=70,textvariable=link).place(x=32,y=90)

def Downloader():
    url=YouTube(str(link.get()))
    video = url.streams.get_highest_resolution()
    video.download()
    Label(display,text='Downloaded',font='arial 15').place(x=180,y=210)

Button(display,text='Download',font='arial 15 bold',bg='pale violet red',padx=2 , command=Downloader).place(x=180,y=150)
display.mainloop()