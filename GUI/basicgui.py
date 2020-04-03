import tkinter as tk
from tkinter.ttk import *
from tkinter import *
HEIGHT = 600
WIDTH = 815

root = tk.Tk()
root.minsize(815,700)
root.maxsize(865,700)
root.title("MPy3 Player")

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

titleText = Label(root, text = "MPy3 Player V1.0")
titleText.place(relx=0.415, rely=0.05)

background_image = tk.PhotoImage(file='discodancing.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg='#87ceeb',bd=5)
frame.place(relx=0.5, rely=0.15, relwidth=0.75, relheight=0.075, anchor='n')

label = tk.Label(frame, text="Rick Astley - Never gonna give you up", bg='white')
label.place(relwidth=0.65, relheight=1)

label1 = tk.Label(frame, text="Current Song", bg='white')
label1.place(relx=0.7, relwidth=0.3, relheight=1)

lowerFrame = tk.Frame(root, bg='#87ceeb', bd=10)
lowerFrame.place(relx=0.5, rely=0.25, relwidth=0.8, relheight=0.6, anchor='n')

label3 = tk.Label(lowerFrame, bg='black')
label3.place(relwidth=1, relheight=1)

#figure out a for loop for this
song1Frame = tk.Label(lowerFrame, bg='white')
song1Frame.place(relwidth=1, relheight=0.07)

song2Frame = tk.Label(lowerFrame, bg='white')
song2Frame.place(relwidth=1, relheight=0.07, rely=0.075)
#just testing this area, maybe build a for loop or something?


buttonFramePrevious = tk.Frame(root, bg='white')
buttonFramePrevious.place(relx=0.35, rely=0.95, relwidth=0.1, relheight=0.05, anchor='s')

buttonFramePause = tk.Frame(root, bg='white')
buttonFramePause.place(relx=0.5, rely=0.95, relwidth=0.1, relheight=0.05, anchor='s')

buttonFrameNext = tk.Frame(root, bg='white')
buttonFrameNext.place(relx=0.65, rely=0.95, relwidth=0.075, relheight=0.05, anchor='s')

buttonPrevious = tk.Button(buttonFramePrevious, text="Previous", bg='#2F4F4F', fg='white', bd= 5)
buttonPrevious.pack(side="left", fill='x')
buttonPause = tk.Button(buttonFramePause, text="Pause", bg='#2F4F4F', fg='white', bd= 5)
buttonPause.pack(side="left", fill='x')
buttonNext = tk.Button(buttonFrameNext, text="Next", bg='#2F4F4F', fg='white', bd= 5)
buttonNext.pack(side="left", fill='x')

root.mainloop()