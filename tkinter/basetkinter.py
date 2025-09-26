#----------------------------------------------------------------
# Una finestra amb textbox, buttons i labels
#-----------------------------------------------------------------
# Previament s'ha d'instalar la llibreria tkinter, alerta les
# diferents versions.

from tkinter import *
from tkinter import messagebox

#Primer s'han de definir les funcions dels events

def identi():
    m="Hola "+t1.get("1.0","end")
    messagebox.showinfo(message=m, title="Saludo")
    #ha de confirmar que l'usuari és com el que es guarda al file on es va crear
    #i que la contrasenya genera el mateix hash

#Crear objecte arrel, tipus tkinter
raiz=Tk()

#Defineix el comportament de la finestra
raiz.title("Python HASH")
raiz.resizable (False, False) #tamany fix

#A dins de la finestra crea un frame
miFrame=Frame(raiz, width=400, height=300)
miFrame.pack()

Label (miFrame, text="Usuari").place(x=10,y=50)

#usuari
t1=Text(raiz)
t1.place(x=10,y=70) 
t1.config(width=15,height=1, font=("Consolas",12))


#botó identificar-se
button1 = Button(raiz, text="Login", command=identi)
button1.place (x=160,y=70)


#Aqui fa un loop fins que es tanca la finestra
raiz.mainloop()
