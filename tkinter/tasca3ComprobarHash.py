from tkinter import *
from tkinter import messagebox
import hashlib

def registrar():

    usuari = crearUsuari.get("1.0", "end-1c")
    pw = crearPw.get("1.0", "end-1c")

    hash_pw = hashlib.sha256(pw.encode()).hexdigest()

    with open("usuaris.txt", 'a') as f:
        f.write(f"{usuari}:{hash_pw}\n")

    m = 'usuari i pw guardats correctament'
    messagebox.showinfo(message=m)

def comprobar():
    cUsuari = comprobarUsuari.get("1.0", "end-1c")
    cPw = comprobarPw.get("1.0", "end-1c")

    cHash_pw = hashlib.sha256(cHash_pw.encode()).hexdigest()

    open("usuaris.txt", "r")

raiz = Tk()
raiz.title("Python HASH")
raiz.geometry("610x200")
raiz.resizable(True, True)  

# Frame per CREAR USUARI
frame_crear = Frame(raiz, bd=2, relief="groove", padx=10, pady=10)
frame_crear.grid(row=0, column=0, padx=20, pady=20)

Label(frame_crear, text="CREAR USUARI").grid(row=0, column=0, columnspan=2, pady=(0,10))
Label(frame_crear, text="Usuari: ").grid(row=1, column=0, sticky="e", padx=5, pady=5)
crearUsuari = Text(frame_crear, width=15, height=1, font=("Consolas", 12))
crearUsuari.grid(row=1, column=1, padx=5, pady=5)

Label(frame_crear, text="Contrasenya: ").grid(row=2, column=0, sticky="e", padx=5, pady=5)
crearPw = Text(frame_crear, width=15, height=1, font=("Consolas", 12))
crearPw.grid(row=2, column=1, padx=5, pady=5)

btn1 = Button(frame_crear, text="Entrar", command=registrar)
btn1.grid(row=3, column=0, columnspan=2, pady=10)

# Frame per COMPROBAR USUARI
frame_comprobar = Frame(raiz, bd=2, relief="groove", padx=10, pady=10)
frame_comprobar.grid(row=0, column=1, padx=20, pady=20)

Label(frame_comprobar, text="CREAR USUARI").grid(row=0, column=0, columnspan=2, pady=(0,10))
Label(frame_comprobar, text="Usuari: ").grid(row=1, column=0, sticky="e", padx=5, pady=5)
comprobarUsuari = Text(frame_comprobar, width=15, height=1, font=("Consolas", 12))
comprobarUsuari.grid(row=1, column=1, padx=5, pady=5)

Label(frame_comprobar, text="Contrasenya: ").grid(row=2, column=0, sticky="e", padx=5, pady=5)
comprobarPw = Text(frame_comprobar, width=15, height=1, font=("Consolas", 12))
comprobarPw.grid(row=2, column=1, padx=5, pady=5)

btn1 = Button(frame_comprobar, text="Comprobar", command=comprobar)
btn1.grid(row=3, column=0, columnspan=2, pady=10)

raiz.mainloop()
