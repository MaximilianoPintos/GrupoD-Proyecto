from tkinter import *

ventana = Tk()
ventana.geometry("700x400")
ventana.title("Login sistema de ventas")
ventana.configure(background = "#83D6A8")
ventana.resizable(0, 0)

#Usuario 
texto = Label(ventana, text = "Usuario:")
texto.config(
    bg = "#83D6A8",
    font = "Arial 10 bold"

)
texto.pack(anchor = CENTER)

usuarioIn = Entry(ventana)
usuarioIn.pack()

#Contraseña
texto = Label(ventana, text = "Contraseña: ")
texto.config(
    font = "Arial 10 bold",
    bg = "#83D6A8",
   
)
texto.pack()
contraIn = Entry(ventana, show = "*")
contraIn.pack()
botonIn = Button(ventana, text = "Ingresar")
botonIn.config(
    font = "Arial 10 bold",
    bg= "darkgray",
    relief = "solid",
    
)
botonIn.pack()
ventana.mainloop()
