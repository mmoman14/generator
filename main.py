import string
from random import randint, choice
from tkinter import *
import webbrowser


def open_tik_tok_account():
    webbrowser.open_new("https://www.tiktok.com/signup/phone-or-email/phone")


def open_google_account():
    webbrowser.open_new("https://www.google.com")


def open_facebook_account():
    webbrowser.open_new("https://www.facebook.com")


def generate_password():
    password_min = 6
    password_max = 12
    all_chars = string.ascii_letters+string.punctuation+string.digits
    password = "".join(choice(all_chars) for x in range(randint(password_min, password_max)))
    password_entry.delete(0, END)
    password_entry.insert(0, password)


# Main
window = Tk()

# Configuration
window.title("Generator of password")
window.config(background='#4065A4')
window.minsize(480, 340)
window.geometry("1280x1024")

# Frame principale
frame = Frame(window, bg='#4065A4')

# Création d'une sous boite
right_frame = Frame(frame, bg='#4065A4')


# Création de l'image
width = 720
height = 720
image = PhotoImage(file="R.png").zoom(35).subsample(32)
canvas = Canvas(window, width=width, height=height, bg='#4065A4', bd=0, highlightthickness=0)
canvas.create_image(width/2, height/2, image=image)
canvas.grid(row=0, column=0, sticky=W)
canvas.pack(expand=YES)


# Creer un titre
label_title = Label(right_frame, text="Password", font=("Helvetica", 20), bg='#4065A4', fg='white')
label_title.pack()

# Créer un champs/entrée/input
password_entry = Entry(right_frame, font=("Helvetica", 20), bg='#4065A4', fg='white')
password_entry.pack(fill=X)


# Créer un bouton
generate_password_button = Button(right_frame, text="Génerer", font=("Helvetica", 20), bg='#4065A4', fg='white', command=generate_password)
generate_password_button.pack()

# Création d'une barre de menu
menu_bar = Menu(window)

# Créer un contenu menu 1
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Nouveau", command=generate_password)
file_menu.add_command(label="Quitter", command=window.quit)
menu_bar.add_cascade(label="Fichier", menu=file_menu)

# Créer un contenu menu 2
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Facebook", command=open_facebook_account)
file_menu.add_command(label="Tik Tok", command=open_tik_tok_account)
file_menu.add_command(label="Google", command=open_google_account)
menu_bar.add_cascade(label="Réseau sociaux", menu=file_menu)

# affiche
window.config(menu=menu_bar)

# On place la sous boite
right_frame.grid(row=0, column=1, sticky=W)

# Afficher la frame
frame.pack(expand=YES)

# Afficher
window.mainloop()
