from tkinter import *
import random

def pelaaVuoro(peliTila):
    kirjain = random.choice('qwertyuiopasdfghjklzxcvbnm')
    
    peliTila['kirjain'] = kirjain
    peliTila['teksti']['text'] = kirjain+"\n"+str(peliTila['pisteet'])
    peliTila['teksti'].after(1000,pelaaVuoro, peliTila)
    
frame = Frame()
frame.pack()

teksti = Label(frame, text = " ", font = "Courier 12 ")
teksti.pack()

peliTila = {'pisteet': 0,
            'teksti': teksti,
            'kirjain': ' '
            }
def tarkista(e):
    print(peliTila['kirjain'], e.char)
    if peliTila['kirjain'] == e.char:
        peliTila['pisteet'] += 1

frame.bind('<KeyPress>', tarkista)
frame.focus_set()
frame.after(500,pelaaVuoro,peliTila)
frame.mainloop()
            
