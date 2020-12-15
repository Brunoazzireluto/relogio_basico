from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk() #instanciando o objeto na raiz do tkinter
root.title('Relógio') #dando um titúlo ao projeto

def relogio():  
    horario = strftime('%H:%M:%S') # puxando o horario do sitema operacinal
    label.config(text=horario) #definindo o texto a ser mostrado
    label.after(1000,relogio) #definindo a atualização da janela

label = Label(root, font=('Helvetica', 70), background='#000', foreground='#00ffff') #definindo interface grafíca
label.pack(anchor='center')

relogio()

mainloop()

