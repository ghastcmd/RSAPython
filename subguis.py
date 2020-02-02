from tkinter import *
from encryption import *

fontspec = 'Arial 10 bold'
redcolor = '#701905'

def genkey():
  subgui = Tk()
  subgui.title('Gere chave pública')
  subgui.geometry('300x300')
  label = Label(subgui, text='Gera a chave pública', font=fontspec, bg=redcolor, fg='white')
  label.pack(fill=X)

  frame = Frame(subgui)

  labeltxt1 = Label(frame, text='Número primo(p): ')
  labeltxt2 = Label(frame, text='Número primo(q): ')
  labeltxt3 = Label(frame, text='Expoente(e): ')
  labeltxt1.grid(row=0, column=0)
  labeltxt2.grid(row=1, column=0)
  labeltxt3.grid(row=2, column=0)

  txtwidth = 23

  txt1 = Text(frame, height=1, width=txtwidth)
  txt2 = Text(frame, height=1, width=txtwidth)
  txt3 = Text(frame, height=1, width=txtwidth)
  txt1.grid(row=0, column=1)
  txt2.grid(row=1, column=1)
  txt3.grid(row=2, column=1)

  frame.pack()

  def generatekey():
    p = parse_int(txt1.get(0.0, 'end'))
    q = parse_int(txt2.get(0.0, 'end'))
    e = parse_int(txt3.get(0.0, 'end'))

    # It's reversed because it's inserting at the start of buffer
    d = get_dec(p[0], q[0], e[0])
    text.delete(0.0, 'end')
    text.insert(0.0, d)
    text.insert(0.0, 'A chave de descriptografia(d) é: ')
    text.insert(0.0, '\n')
    text.insert(0.0, p[0] * q[0])
    text.insert(0.0, 'A chave pública(n) é : ')

    with open('public_key.txt', 'w+') as arc:
      arc.write(f'A chave pública(n) é: {p[0] * q[0]}\n')
      arc.write(f'A chave de privada de descriptografia(d) é: {d}')

  button = Button(subgui, text='Gerar', bg=redcolor, fg='white', font=fontspec,
    command=generatekey)
  button.pack(fill=X)

  text = Text(subgui)
  text.pack()


  subgui.mainloop()

def cryptmens():
  subgui = Tk()
  subgui.title('Criptografe mensagem')
  subgui.geometry('300x300')
  label = Label(subgui, text='Cyptografe uma mensagem\n(somente caracteres maiúsculos)',
    font=fontspec, bg=redcolor, fg='white')
  label.pack(fill=X)
  

  boxesframe = Frame(subgui)
  
  framelabel1 = Label(boxesframe, text='Expoente(e): ')
  framelabel1.grid(row=0)
  framelabel2 = Label(boxesframe, text='Chave pública(n): ')
  framelabel2.grid(row=1)

  txtInputWidth = 13

  frametext1 = Text(boxesframe, height=1, width=txtInputWidth)
  frametext1.grid(row=0, column=1)
  frametext2 = Text(boxesframe, height=1, width=txtInputWidth)
  frametext2.grid(row=1, column=1)

  def crypt():
    string = text.get(0.0, 'end')
    string = string[:-1]
    text.delete(0.0, 'end')

    e = parse_int(frametext1.get(0.0, 'end'))
    n = parse_int(frametext2.get(0.0, 'end'))

    nums = string_enc(string, e[0], n[0])

    with open('encrypted_msg.txt', 'w+') as arc:
      for a in nums:
        arc.write(f'{a} ')

    for a in reversed(nums):
      text.insert(0.0, a)
      text.insert(0.0, ' ')
    text.delete(0.0)

  button = Button(boxesframe, text='Criptografar', font=fontspec, bg=redcolor, 
    fg='white', pady=8, command=crypt)
  button.grid(row=0, column=2, rowspan=2, sticky=E)

  boxesframe.pack()

  labelmsg = Label(subgui, text='Digite a mensagem: ', font=fontspec, bg=redcolor, 
    fg='white')
  labelmsg.pack(fill=X)

  text = Text(subgui)
  text.pack(fill=X)
  subgui.mainloop()

def decptmens():
  subgui = Tk()
  subgui.title('Decripte mensagem')
  subgui.geometry('300x300')
  label = Label(subgui, text='Descriptografe uma mensagem\n(somente números inteiros serão considerados)',
    font=fontspec, bg=redcolor, fg='white')
  label.pack(fill=X)
  
  boxesframe = Frame(subgui)
  
  framelabel1 = Label(boxesframe, text='Chave privada d: ')
  framelabel1.grid(row=0)
  framelabel2 = Label(boxesframe, text='Chave pública n: ')
  framelabel2.grid(row=1)

  txtInputWidth = 10

  frametext1 = Text(boxesframe, height=1, width=txtInputWidth)
  frametext1.grid(row=0, column=1)
  frametext2 = Text(boxesframe, height=1, width=txtInputWidth)
  frametext2.grid(row=1, column=1)

  def decrypt():
    string = text.get(0.0, 'end')
    string = string[:-1]
    text.delete(0.0, 'end')

    d = parse_int(frametext1.get(0.0, 'end'))
    n = parse_int(frametext2.get(0.0, 'end'))

    letters = string_dec(string, d[0], n[0])

    with open('decrypted_msg.txt', 'w+') as arc:
      for a in letters:
        arc.write(f'{a}')

    for a in reversed(letters):
      text.insert(0.0, a)

  button = Button(boxesframe, text='Descriptografar', font=fontspec, bg=redcolor, 
    fg='white', pady=8, command=decrypt)
  button.grid(row=0, column=2, rowspan=2)

  boxesframe.pack()

  labelmsg = Label(subgui, text='Digite a mensagem criptografada: ', font=fontspec, 
    bg=redcolor, fg='white')
  labelmsg.pack(fill=X)

  text = Text(subgui)
  text.pack(fill=X)
  subgui.mainloop()


if __name__ == '__main__':
  genkey()
  cryptmens()
  decptmens()