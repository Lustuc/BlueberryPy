#Required libraries...
import tkinter as tk
from tkinter import ttk
import pyfirmata
import time
#Initialize arduino board...
board = pyfirmata.Arduino('/dev/ttyACM0')
BUTTONS = []
#Initialize tkinter window...
root = tk.Tk()
root.geometry('400x400')
root.title('Arduino Interface')
root.resizable(True,True)
#Define images...
onI = tk.PhotoImage(file='on.png')
offI = tk.PhotoImage(file='off.png')
#Define action when a button is pressed...
def onClick(i):
    global BUTTONS, board
    if board.digital[13-i].read() == 0:
        BUTTONS[i].configure(image=onI)
        board.digital[13-i].write(1)
    else:
        BUTTONS[i].configure(image=offI)
        board.digital[13-i].write(0)
#Show buttons and title...
ttk.Label(root, text='PINS disponibles:',font=("Helvetica",16)).place(relx=0.5, rely=0.1)
for i in range(6):
    BUTTONS.append(ttk.Button(root, text=str(i), image = offI, compound=tk.LEFT, command=lambda I=i: onClick(I)))
    BUTTONS[i].place(relx=0.5, rely=0.2+0.1*i, relwidth=0.2, relheight=0.1)
#Run app...
root.mainloop()


