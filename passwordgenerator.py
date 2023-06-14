from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk
import random, pyperclip
from cryptography.fernet import Fernet
from PIL import ImageTk, Image  

window = ThemedTk(theme = "equilux")
window.configure(themebg = "equilux")
window.geometry("500x220")

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
digits = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()"

def copy(event=0):
    pyperclip.copy(passwordtxb.get())
def generate_password(event=0):
    global random_pass
    passwordtxb.config(state=ACTIVE)
    passwordtxb.delete(0, END)
    random_pass = []
    length = lengthcombo.get()
    length = int(length)
    strength = rb.get()
    if strength == "L":
        for i in range(length):
            digit = str(random.choice(lower))
            passwordtxb.insert("1",digit)
    if strength == "M":
        for i in range(length):
            digit = str(random.choice(upper))
            passwordtxb.insert("1",digit)
    if strength == "S":
        for i in range(length):
            digit = str(random.choice(digits))
            passwordtxb.insert("1",digit)

    passwordtxb.config(state=DISABLED)
def encrypt_Fernet(event=0):
    global password
    Encyptiontxb.config(state=ACTIVE)
    Encyptiontxb.delete(0,END)

        #magic
    key = Fernet.generate_key()
    fernet = Fernet(key)

    password = passwordtxb.get()

    password_but_with_Nord_VPN = fernet.encrypt(password.encode())
    print(len(password_but_with_Nord_VPN))
    Encyptiontxb.insert(1,password_but_with_Nord_VPN)
    Encyptiontxb.config(state=DISABLED)
def decrypt(event=0):
    global password
    Encyptiontxb.config(state=ACTIVE)
    Encyptiontxb.delete(0, END)
    password = passwordtxb.get()
    Encyptiontxb.insert(1, password)
    Encyptiontxb.config(state=DISABLED)
def encrypt_Ceasar(event=0):
    n = 12
    Encyptiontxb.config(state=ACTIVE)
    Encyptiontxb.delete(0, END)
    password = passwordtxb.get()
    password_but_with_Nord_VPN = ""
    for i in range(len(password)):

        digit = password[i]

        #CHR translates from interger to letter
        #ORD translates from letter to interger

        if ord(digit) + n > 21:
            password_but_with_Nord_VPN += chr((ord(digit) + n))
        else:
            n = 0
            password_but_with_Nord_VPN += chr((ord(digit) + n))
    Encyptiontxb.insert(1, password_but_with_Nord_VPN)
    Encyptiontxb.config(state=DISABLED)

#instructions / info

passwordlbl = ttk.Label(window,text= "Password:",font=("Calibri",12))
passwordlbl.grid(column=0,row=0)

lengthlbl = ttk.Label(window,text= "Length:",font=("Calibri",12))
lengthlbl.grid(column=0,row=1)

encryptlbl = ttk.Label(window,text= "Encrypt:",font=("Calibri",12))
encryptlbl.grid(column=0,row=2)


#Buttons

copy_button = ttk.Button(window,text= "Copy",command=copy)
copy_button.grid(column=2,row=0)

generate_button = ttk.Button(window,text= "Generate",command=generate_password)
generate_button.grid(column=3,row=0)

encrypt_button = ttk.Button(window,text= "Encrypt Fernet",command=encrypt_Fernet)
encrypt_button.grid(column=2,row=2)

encrypt_button = ttk.Button(window,text= "Encrypt Ceasar",command=encrypt_Ceasar)
encrypt_button.grid(column=2,row=3)

decrypt_button = ttk.Button(window,text= "Decrypt",command=decrypt)
decrypt_button.grid(column=3,row=2)

#Radiobutton

rb = StringVar()
rb.set("Radio2")
rb.set("L")
radio1_Low = ttk.Radiobutton(window, text="Low",value="L",variable= rb)
radio2_Medium = ttk.Radiobutton(window, text="Medium",value="M",variable= rb)
radio3_Strong = ttk.Radiobutton(window, text="Strong",value="S",variable= rb)

radio1_Low.grid(column=2,row=1)
radio2_Medium.grid(column=3,row=1)
radio3_Strong.grid(column=4,row=1)

all_radios = [radio1_Low,radio2_Medium,radio3_Strong]

#Comboboxes

lengthcombo = ttk.Combobox(window)
lengthcombo["values"] = (6,8,10,12)
lengthcombo.current(0)
lengthcombo.grid(column=1,row=1)

#Textboxes

passwordtxb = ttk.Entry(window)
passwordtxb.grid(column=1,row=0)
passwordtxb.config(state=DISABLED)

Encyptiontxb = ttk.Entry(window)
Encyptiontxb.grid(column=1,row=2)
Encyptiontxb.config(state=DISABLED)

logo = PhotoImage(file="projects/logo.png")
label2 = Label(window, image=logo, bg='#464646')
label2.grid(column=0,row=5,columnspan=4)

window.title("Password Generator")
window.mainloop()
