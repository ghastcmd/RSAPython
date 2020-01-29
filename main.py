from tkinter import *
from subguis import *

root = Tk()

backBgColor = '#701905'

bgColor = '#701905'
fgColor = 'white'
fontSpec = 'Arial 10 bold'
activeBg = '#e0e0e0'

topLabel = 'Programa de criptografia em RSA'

canvas = Canvas(root, width=270, height=250)
canvas.pack()

frame = Frame(root)
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

frameTop = Frame(frame)
frameTop.place(rely=0.0, relwidth=1.0)

title = Label(frameTop, text=topLabel, bg=backBgColor, pady=5, fg=fgColor, font='Times-new-roman 10 bold')
title.pack(fill=X)

frameBot = Frame(frame)
frameBot.place(rely=0.35, relwidth=1.0)

button1 = Button(frameBot, text='Gerar chave pública', 
    bg=bgColor, fg=fgColor, font=fontSpec, activebackground=activeBg,
    command=genkey)
button1.pack(fill=X)
button2 = Button(frameBot, text='Criptografar mensagem', 
    bg=bgColor, fg=fgColor, font=fontSpec, activebackground=activeBg,
    command=cryptmens)
button2.pack(fill=X)
button3 = Button(frameBot, text='Descriptografar mensagem', 
    bg=bgColor, fg=fgColor, font=fontSpec, activebackground=activeBg,
    command=decptmens)
button3.pack(fill=X)

root.resizable(width=False, height=False)
root.mainloop()