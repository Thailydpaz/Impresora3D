import tkinter as tk
from tkinter import *
from tkinter import messagebox
import os
#from tkinter import filedialog
#import RPi.GPIO as GPIO
#import time

def abrePrograma():
    ruta = "C:\\Program Files\\Repetier-Host\\RepetierHost.exe"
    os.system('"' + ruta + '"')

def abrePrograma1():
    ruta = "C:\\Program Files (x86)\\Arduino\\arduino.exe"
    os.system('"' + ruta + '"')

def abrePrograma2():
    ruta = "C:\\Users\\Niteowl\\Desktop\\Nueva carpeta (5)\\pronterface.exe"
    os.system('"' + ruta + '"')

def salirAplicacion():
    #messagebox.askquestion("Salir", "¿Deseas salir de la aplicacion?")
    valor=messagebox.askokcancel("Salir", "¿Deseas salir de la aplicacion?")
    if valor==True:
        root.destroy()
root=tk.Tk()

#imagen y titulo
root.title("Interfaz Grafica: Impresora 3D")
root.iconbitmap("cat.ico")


miFrame=Frame(root, width=904, height=508)

miFrame.pack()

Fondo=PhotoImage(file="3d_2.gif")
Fondo1= Label(root, image=Fondo).place(x=0, y=0, relwidth=1, relheight=1)

boton1= Button (root, text= "Repetier", command=abrePrograma,bg="white",bd=5, fg="black", activebackground="white", relief= "sunken")
boton1.place(x=30, y=40)

boton2= Button (root, text= "Arduino", command=abrePrograma1,bg="white", bd=5, fg="black", activebackground="white", relief= "sunken")
boton2.place(x=30, y=90)

boton1= Button (root, text= "Pronterface", command=abrePrograma2,bg="white",bd=5, fg="black", activebackground="white", relief= "sunken")
boton1.place(x=30, y=140)

boton1= Button (root, text= "Salir", command=salirAplicacion,bg="white",bd=5, fg="black", activebackground="white", relief= "sunken")
boton1.place(x=30, y=190)


#menu.add_command(label="Salir", command=salirAplicacion)

root.mainloop()
