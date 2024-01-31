# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 17:59:51 2024

@author: Aidan
"""

from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image


root = Tk()
root.geometry("600x600")
root.config(background = "black")


etq_imagen = Label(root, bg="white", highlightthickness=5)
etq_imagen.place(relx=0.5, rely=0.5, anchor=CENTER)


img_path=""
def openFile():
    global img_path
    img_path = filedialog.askopenfilename(title="Abrir archivo de texto", filetypes=[("Image Files","*.jpg *.gif *.jpg *.png *.jpeg")])
    print(img_path)
    im = Image.open(img_path)
    img = ImageTk.PhotoImage(im)
    etq_imagen["image"] = img
    img.close()


def rotateImage():
    global img_path
    im = Image.open(img_path)
    img = ImageTk.PhotoImage(im.rotate(180))
    etq_imagen["image"] = img
    print(img_path)
    img.close()
    
btn=Button(root,text="Abrir imagen",font= ("Times New Roman0", 12),bg="grey",fg="white", command=openFile, relief=SOLID, padx=15, pady=10)
btn.place(relx=0.5,rely=0.1,anchor=CENTER)


btn1=Button(root,text="Rotar imagen",font= ("Times New Roman0", 12),bg="grey",fg="white", command=rotateImage, relief=SOLID, padx=15, pady=10)
btn1.place(relx=0.5,rely=0.85,anchor=CENTER)


etq_footer = Label(root,text="Creado por el equipo de BYJU'S FutureSchool", bg="black", fg="white")
etq_footer.place(relx=0.5, rely=0.95, anchor=CENTER)


root.mainloop()
