from tkinter import *

ventana = Tk()
ventana.title("Cathaysa's Calculator")
ventana.geometry("600x300")

mensaje = Label(ventana, text="¿Necesitas sumar algo?")
mensaje.place(x=20, y=10)
mensaje.pack()

etiqueta1 = Label(ventana, text="Primer numero:", bg="pink")
etiqueta1.place(x=60, y=60)
etiqueta_escribir1 = Entry(ventana, bg="pink")
etiqueta_escribir1.place(x=180, y=60)


etiqueta2 = Label(ventana, text="Segundo numero:", bg="lightblue")
etiqueta2.place(x=60, y=100)
etiqueta_escribir2 = Entry(ventana, bg="lightblue")
etiqueta_escribir2.place(x=180, y=100)

resultado = Label(ventana, text="Resultado:", bg="lightgreen")
resultado.place(x=60, y=140)
etiqueta_escribir3 = Entry(ventana, bg="lightgreen")
etiqueta_escribir3.place(x=180, y=140)

def suma():
    text1 = etiqueta_escribir1.get()
    text2 = etiqueta_escribir2.get()
    resultado = float(text1) + float(text2)
    etiqueta_escribir3.insert(0, resultado)

boton_calcular = Button(ventana, text="Sumar", bg="gray", command=suma)
boton_calcular.place(x=400, y=100)



ventana.mainloop()