from tkinter import *
from tkinter import filedialog
from pygame import mixer

root = Tk()
root.title('Pemutar Musik')
root.config(background='lightgreen')

mixer.init()

#untuk membuat Label / judul 
Label(root, text='Pemutar Musiku', bg='lightgreen', font='NORMAL 40').grid(row=0, coloumn=0,
      coloumnspan=3, pady=10)

#cari
def cari():
    file = filedialog.askopenfilename(filetypes=[('mp3' , '*.mp3')]) # untuk mendapatkan lagu yang akan diputar 
    if file == "":
        return
    mixer.music.load(file)
    t.config(state=NORMAL)
    t.delete(1.0, END)
    t.insert(END, file)
    t.config(state=DISABLED)

b = Button(root, text='Cari', font='Normal 25', command=cari, relief=RIDGE, bg=10, activebackground='lightblue')
b.grid(row=1, column=1, ipadx=30, pady=5)

t = Text(root, font='Normal 15', bg='lightgreen', wrap=WORD, height=3, width=50)
t.grid(row=2, columnspan=3, pady=15)
t.config(state=DISABLED)


#pause
def pause():
    pass
b1 = Button(root, text='Pause', font="Normal 25", command=pause, relief=RiDGE, bd=10, activebackground='lightblue')
b1.grid(row=3, column=0, padx=15, ipadx=15)

#Play
def play():
    mixer.music.play(-1)
b2= Button(root, text='Mainkan', font='Normal 25', command=play, relief=RIDGE, bd=10, activebackground='lightblue')
b2.grid(row=3, column=1, padx=10)


#unpause
def unpause():
    mixer.music.unpause()
b3 = Button(root, text='Unpause', font='Normal 25', command=unpause, relief=RIDGE, bd=10, activebackground='lightblue')
b2.grid(row=3, column=1, padx=10)


#berhenti 
def stop():
    mixer.music.stop()
b3 = Button(root, text='Berhenti', font='Normal 25', command=stop, relief=RIDGE, bd=10, activebackground='lightblue')
b2.grid(row=4, column=1, padx=10, pady=20)

root.mainloop()
