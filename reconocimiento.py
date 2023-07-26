#Developer
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import cv2
import os
#from tarea2parcial import actualizar

ruta = '/home/salvador/Tarea/Data' 
imagen = os.listdir(ruta)
print('imagen=',imagen)
modelo = cv2.face.EigenFaceRecognizer_create()
#modelo = cv2.face.LBPHFaceRecognizer_create()
# Leyendo el modelo
modelo.read('modelo.xml')

cap = cv2.VideoCapture('Salvador.mkv')
#cap = cv2.VideoCapture('zoe.mp4')
faceClassif = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
while True:
    ret,frame = cap.read()
    if ret == False: break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    auxFrame = gray.copy()
    faces = faceClassif.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in faces:
        rostro = auxFrame[y:y+h,x:x+w]
        rostro = cv2.resize(rostro,(150,150),interpolation= cv2.INTER_CUBIC)
        result = modelo.predict(rostro)
        cv2.putText(frame,'{}'.format(result),(x,y-5),1,1.3,(255,255,0),1,cv2.LINE_AA)
        
        # EigenFaces
        if result[1] < 5700:
            os.system("sudo echo 1 > /home/salvador/Tarea/estado.txt")
           
            cv2.putText(frame,'{}'.format(imagen[result[0]]),(x,y-25),2,1.1,(0,255,0),1,cv2.LINE_AA)
            cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
            #os.system("sudo /./home/gizsa2/on.sh &")
        else:
            os.system("sudo echo 0 > /home/salvador/Tarea/estado.txt")
            #print("Desconocido")
            #messagebox.showwarning("Error","Rostro no Identificado")
            cv2.putText(frame,'Desconocido',(x,y-20),2,0.8,(0,0,255),1,cv2.LINE_AA)
            cv2.rectangle(frame, (x,y),(x+w,y+h),(0,0,255),2)
       
    cv2.imshow('frame',frame)
    k = cv2.waitKey(1)
    if k == 27:
        break
cap.release()
messagebox.showinfo("Exito","Rostro Identificado")
cv2.destroyAllWindows()

print("Reconocimiento Finalizada")
