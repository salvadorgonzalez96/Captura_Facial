#Developer
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import subprocess
import os

dataPath = '/home/salvador/Tarea/'
dataCap = dataPath+'captura.py'
dataEnt = dataPath+'entrenando.py'
dataRec = dataPath+'reconocimiento.py'

#Crear Ventana
ventana=tk.Tk()
ventana.title("Tarea 2o Parcial")
ventana.geometry("450x330")

#Texto Principal
titulo = Label(ventana, text="OPENCV",font="Poppins").place(x=10,y=10)

#Cargar Imagenes
img_on=PhotoImage(file="on.gif")
img_off=PhotoImage(file="off.gif")

def actualizar():
    pf=open("/home/salvador/Tarea/estado.txt","r")
    for linea in pf:
        campo=linea.split("\n")
        campof=campo[0]
        if(campof=="1"):
            on_btn=Button(ventana,image=img_on).place(x=150,y=150)
            ventana.after(1000,actualizar)
        if(campof=="0"):            
            off_btn=Button(ventana,image=img_off).place(x=150,y=150)
            ventana.after(1000,actualizar)

actualizar()

def encender():
    print("Encendido")
    os.system("cat /home/salvador/Tarea/estado.txt")
    os.system("sudo /./home/salvador/Tarea/encender.sh")

def apagar():
    print("Apagado")
    os.system("cat /home/salvador/Tarea/estado.txt")
    os.system("sudo /./home/salvador/Tarea/apagar.sh")

def ejecutar_captura():
    subprocess.Popen(["/usr/bin/python3",dataCap])

def ejecutar_entrenamiento():
    subprocess.Popen(["/usr/bin/python3",dataEnt])

def ejecutar_reconocimiento():
    subprocess.Popen(["/usr/bin/python3",dataRec])

#Crear botones
captura_btn = Button(ventana, text="Captura", command=ejecutar_captura)
captura_btn.place(x=10, y=50)

entrenamiento_btn = Button(ventana, text="Entrenamiento", command=ejecutar_entrenamiento)
entrenamiento_btn.place(x=100, y=50)

reconocimiento_btn = Button(ventana, text="Reconocimiento", command=ejecutar_reconocimiento)
reconocimiento_btn.place(x=240, y=50)

on_btn=Button(ventana,image=img_on,command=encender).place(x=150,y=150)
off_btn=Button(ventana,image=img_off,command=apagar).place(x=150,y=150)

#on_btn = Button(ventana,text="ON",command=encender).place(x=100, y=150)
#off_btn = Button(ventana,text="OFF",command=apagar).place(x=100, y=150)

ventana.mainloop()