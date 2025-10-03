#----------------------------------------------------------------
# Una finestra amb textbox, buttons i labels amb grid
#----------------------------------------------------------------
from tkinter import *
from tkinter import messagebox

def identi():
    m = "login " + t1.get("1.0", "end")
    messagebox.showinfo(message=m, title="Saludo")
   


raiz = Tk()
raiz.title("Python HASH")
raiz.resizable(True, True)  

# Frame contenidor
register = Frame(raiz, width=400, height=300, bg="lightblue")
register.pack(side=LEFT, padx=20, pady=20)  


login = Frame(raiz, width=400, height=300, bg="lightgreen")
login.pack(side=RIGHT, padx=20, pady=20)  


# Label usuari
Label(register, text="Usuari").grid(row=0, column=0, padx=5, pady=5, sticky="e")
Label(login, text="login").grid(row=1, column=1, padx=5, pady=5, sticky="e")

# Caixa de text usuari
t1 = Text(register, width=15, height=1, font=("Consolas", 12))
t1.grid(row=1, column=0, padx=5, pady=5)

# Botó login
button1 = Button(register, text="Login", command=identi)
button1.grid(row=0, column=2, padx=10, pady=5)

# Loop principal
raiz.mainloop()
