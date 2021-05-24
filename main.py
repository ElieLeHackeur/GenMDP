from tkinter import *
import string
from random import randint, choice

def generate_password():
    password_min = 8
    password_max = 8
    all_chars = string.ascii_letters + string.punctuation + string.digits
    password = "".join(choice(all_chars) for x in range (randint(password_min, password_max)))
    password_entry.delete(0, END)
    password_entry.insert(0, password)

def generate_password2():
    password_min = 8
    password_max = 8
    all_chars = string.ascii_letters
    password = "".join(choice(all_chars) for x in range (randint(password_min, password_max)))
    password_entry.delete(0, END)
    password_entry.insert(0, password)

def generate_password3():
    password_min = 8
    password_max = 8
    all_chars = string.ascii_letters + string.digits
    password = "".join(choice(all_chars) for x in range (randint(password_min, password_max)))
    password_entry.delete(0, END)
    password_entry.insert(0, password)



window = Tk()
window.title("Generateur de mdp")
window.geometry("720x480")
window.minsize(1000, 600)
window.wm_attributes("-topmost", 1)
window.configure(bg = '#4065A4')

frame = Frame(window, bg='#4065A4')



salut = Label(frame, text="Le mdp va etre generer ici", font=("Helvetica", 20), bg='#4065A4', fg='white')
salut.pack()

password_entry = Entry(frame, text="Mot de passe", font=("Helvetica", 20), bg='#4065A4', fg='white')
password_entry.pack()

Moche = Label(frame, text="Appuyez sur le boutton ci-dessous pour générer un mdp avec des lettres, ponctuations et caracteres speciaux", font=("Helvetica", 20), bg='#4065A4', fg='white')
Moche.pack()

button = Button(frame, text="generer", font=("Helvetica", 20), bg='#4065A4', fg='red', command=generate_password)
button.pack(fill=X)

Moche = Label(frame, text="Appuyez sur le boutton ci-dessous pour générer un mdp avec uniquement des lettres", font=("Helvetica", 20), bg='#4065A4', fg='white')
Moche.pack()

button = Button(frame, text="generer", font=("Helvetica", 20), bg='#4065A4', fg='red', command=generate_password2)
button.pack(fill=X)

Moche = Label(frame, text="Appuyez sur le boutton ci-dessous pour générer un mdp avec des lettres et des chiffres", font=("Helvetica", 20), bg='#4065A4', fg='white')
Moche.pack()

button = Button(frame, text="generer", font=("Helvetica", 20), bg='#4065A4', fg='red', command=generate_password3)
button.pack(fill=X)

frame.pack(expand=YES)


window.mainloop()
