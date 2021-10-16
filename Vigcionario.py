from tkinter import *
import json
from difflib import get_close_matches
from tkinter import messagebox
import pyttsx3

#Functionality

def search():
    data=json.load(open('data.json'))
    word=enter_word_entry.get()
    if word in data:
        meaning=data[word]
        for item in meaning:
            text_area.insert(END,u'\u2022'+item)

    elif len(get_close_matches(word,data.keys()))>0:
        close_match = get_close_matches(word,data.keys())[0]
        print(close_match)
        res=messagebox.askyesno('Confirm', 'Did you mean '+close_match+' instead?')
        if res == True:
            enter_word_entry.delete(0,END)
            enter_word_entry.insert(END,close_match)

            meaning=data[close_match]
            for item in meaning:
                text_area.insert(END,u'\u2022'+item)

def clear_box():
    enter_word_entry.delete(0,END)
    text_area.delete(0,END)

def listen():
    global engine
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[2].id)
    engine.say(text_area.get(1.0,END))
    engine.runAndWait()

#GUI
root = Tk()

root.geometry('1000x626+100+30')

root.title('Diccionario de hablar')


bg_image = PhotoImage(file='background2.png')
bg_label=Label(root, image=bg_image)
bg_label.place(x=0, y=0)

enter_word_label = Label(root, text='Diccionario de Vig (Vigccionario)', font=('castellar',15), foreground='red3')
enter_word_label.place(x=530, y=20)

enter_word_entry= Entry(root, font=('arial', 23,'bold'), justify=CENTER, bd=15, relief=GROOVE)
enter_word_entry.place(x=510, y=80)

search_image = PhotoImage(file='search.png')
search_button = Button(root,image=search_image,bd=0, bg='whitesmoke', cursor='hand2', activebackground='whitesmoke', command=search)
search_button.place(x=510, y=156)

clear_image=PhotoImage(file='exit.png')
clear_button = Button(root, image=clear_image,bd=0, bg='whitesmoke', cursor='hand2', command=clear_box)
clear_button.place(x=620, y=156)

meaning_label = Label(root,text='Search/Buscar', font=('arial',10),fg='black')
meaning_label.place(x=510,y=260)

meaning_label_two = Label(root,text='Clear/Eliminar', font=('arial',10),fg='black')
meaning_label_two.place(x=620,y=260)

meaning_label_three = Label(root,text='Listen/Escuchar', font=('arial',10),fg='black')
meaning_label_three.place(x=730,y=260)

text_area=Entry(root,font=('arial',18,'bold'), bd=15, relief=GROOVE)
text_area.place(x=510,y=300)

audio_image=PhotoImage(file='mic.png')
audio_button = Button(root, image=audio_image,bd=0,bg='whitesmoke', command=listen)
audio_button.place(x=730, y=156)

root.mainloop()
