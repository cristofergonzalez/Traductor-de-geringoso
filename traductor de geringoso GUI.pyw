from tkinter import *

raiz=Tk()
raiz.title("Traductor de geringoso")
raiz.resizable(False,False)

#-----------------------Cuadro principal-------------------------#

miFrame=Frame(raiz)
miFrame.pack()
miFrame.config(bd=10)

#-----------------------Variables a utilizar---------------------#
entradaPantalla=StringVar()
etiquetaTraducida=StringVar()
etiqueta_2=StringVar()


entradaPantalla2=StringVar()
etiquetaTraducida2=StringVar()
etiqueta_3=StringVar()
#-----------------------Funciones--------------------------------#

def traducir(palabra):
    lista=[]
    for letra in palabra.lower():
        if letra in ["!","?"," ","a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]:
            lista.append(letra)
    for letra in lista:
        if letra == "a":
            a = lista.index(letra)
            lista[a] = "apa"
        elif letra == "e":
            a = lista.index(letra)
            lista[a] = "epe"
        elif letra == "i":
            a = lista.index(letra)
            lista[a] = "ipi"
        elif letra == "o":
            a = lista.index(letra)
            lista[a] = "opo"
        elif letra == "u":
            a = lista.index(letra)
            lista[a] = "upu"
    a = "".join(lista)
    etiquetaTraducida.set(a)
    etiqueta_2.set(palabra)
    entradaPantalla.set("")

def traducir_ge(palabra):
    lista=[]
    lista_final=[]
    for letra in palabra.lower():
        if letra in ["!","?"," ","a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]:
            lista.append(letra)
    for letra in lista:
        lista_final.append(letra)
        if letra=="a":
            a=lista.index(letra)
            del lista[int(a+1)]
            del lista[int(a+1)]
            lista[a:len(lista)]
        elif letra=="e":
            a=lista.index(letra)
            del lista[int(a+1)]
            del lista[int(a+1)]
            lista[a:len(lista)]
        elif letra=="i":
            a=lista.index(letra)
            del lista[int(a+1)]
            del lista[int(a+1)]
            lista[a:len(lista)]
        elif letra=="o":
            a=lista.index(letra)
            del lista[int(a+1)]
            del lista[int(a+1)]
            lista[a:len(lista)]
        elif letra=="u":
            a=lista.index(letra)
            del lista[int(a+1)]
            del lista[int(a+1)]
            lista[a:len(lista)]
    palabra_final = "".join(lista_final)
    etiquetaTraducida2.set(palabra_final)
    etiqueta_3.set(palabra)
    entradaPantalla2.set("")
"""--------------------------TRADUCIR DE ESPAÑOL A GERINGOSO---------------------------------"""
#-----------------------Entrada pantalla-------------------------#

Entrada=Entry(miFrame,width=100,textvariable=entradaPantalla)
Entrada.grid(row=0,column=1,pady=10,padx=10)
Entrada.config(justify="center")

#-----------------------Boton de Traducir-------------------------#

boton=Button(miFrame,text="Traducir",command=lambda:traducir(entradaPantalla.get()))
boton.grid(row=0,column=2)
boton.config(padx=20,pady=10,bd=3)

#-----------------------Texto de salida---------------------------#

etiqueta=Label(miFrame,textvariable=etiquetaTraducida)
etiqueta.grid(row=3,column=1)
etiqueta.config(padx=10,pady=10,font=("arial",10))

etiqueta2=Label(miFrame,textvariable=etiqueta_2)
etiqueta2.grid(row=3,column=0)
etiqueta2.config(padx=10,pady=10,font=("arial",10))

etiqueta3=Label(miFrame,text="Texto Traducido en Geringoso: ")
etiqueta3.grid(row=2,column=1)
etiqueta3.config(padx=10,pady=10,font=("Times",14))


etiqueta4=Label(miFrame,text="Texto a Traducir en Español: ")
etiqueta4.grid(row=2,column=0)
etiqueta4.config(padx=10,pady=10,font=("Times",14))

#-----------------------------------------------------------------------------------------------#

"""-----------------------------------TRADUCIR DE GERINGOSO A ESPAÑOL--------------------------"""
#-----------------------Entrada pantalla-------------------------#

Entrada=Entry(miFrame,width=100,textvariable=entradaPantalla2)
Entrada.grid(row=5,column=1,pady=10,padx=10)
Entrada.config(justify="center")

#-----------------------Boton de Traducir-------------------------#

boton=Button(miFrame,text="Traducir",command=lambda:traducir_ge(entradaPantalla2.get()))
boton.grid(row=5,column=2)
boton.config(padx=20,pady=10,bd=3)

#-----------------------Texto de salida---------------------------#

etiqueta=Label(miFrame,textvariable=etiquetaTraducida2)
etiqueta.grid(row=7,column=1)
etiqueta.config(padx=10,pady=10,font=("Verdana",10))

etiqueta2=Label(miFrame,textvariable=etiqueta_3)
etiqueta2.grid(row=7,column=0)
etiqueta2.config(padx=10,pady=10,font=("Arial",10))

etiqueta3=Label(miFrame,text="Texto Traducido en Español: ")
etiqueta3.grid(row=6,column=1)
etiqueta3.config(padx=10,pady=10,font=("Arial",14))


etiqueta4=Label(miFrame,text="Texto a Traducir en Geringoso: ")
etiqueta4.grid(row=6,column=0)
etiqueta4.config(padx=10,pady=10,font=("Arial",14))

raiz.mainloop()