# IMPORT ALL REQUIRED MODULES AND PACKAGES
from tkinter import *
import pyttsx3

# TEXT TO SPEECH CONVERSION FUNCTION
def convert():
    text = txt.get()
    engine.say(text)
    engine.runAndWait()
# MAIN APPLICATION 
main = Tk()
main.title('Text to Speech')
main.geometry('300x200')
main.resizable(0,0)

# VOICE SETTINGS
engine = pyttsx3.init('espeak')
voices = engine.getProperty('voices')
speed = engine.setProperty("rate",150)
engine.setProperty('voice','voices[0].id')

# WIDGETS
frame = Frame(main,padx=10,pady=10)
frame.pack(expand=True)

lbl = Label(frame,text='Enter Text:')
lbl.grid(row=1,column=1,sticky=W)

txt = Entry(frame,justify=LEFT)
txt.grid(row=1,column=2,sticky=W)

frame_1 = Frame(main,padx=20,pady=10)
frame_1.pack(expand=True)

btn = Button(frame_1,text='Speak', padx=20, bg='blue',fg='white',command=convert)
btn.grid(row=1,column=3,sticky=W)
ex = Button(frame_1,text='Exit', padx=20, bg='red',fg='white',command=exit)
ex.grid(row=1,column=5,sticky=W)

# END APPLICATION
main.mainloop()