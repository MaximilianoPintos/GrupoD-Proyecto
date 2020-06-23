from tkinter import *


class Registro: 
    def __init__(self):
        self.titulo = "Registro de empleados"
        self.color = "#83D6A8"
        self.icono = "@/home/martin/Escritorio/GrupoD-Proyecto/Iconos/Registradora.xbm"

    def Inicio(self):

        ventanaRegistro = Tk()
        # Tamaño de la ventana
        ox,oy=ventanaRegistro.winfo_screenwidth()/5,ventanaRegistro.winfo_screenheight()/5
        ventanaRegistro.geometry("=700x400+%d+%d" % (ox--60,oy-20) )
        ventanaRegistro.title(self.titulo)
        ventanaRegistro.resizable(False, False)
        ventanaRegistro.configure(background = self.color)
        ventanaRegistro.iconbitmap(self.icono)

        #Encabezado
        encabezado = Label(ventanaRegistro, text = "Registro de nuevo empleado" ) 
        encabezado.config(
            fg = "black",
            bg = "#83D6A8",
            font = ("Arial", 18),
            padx = 10,
            pady = 10
            )
        encabezado.place(x=175, y=0)

        #Nombre 
        texto = Label(ventanaRegistro, text = "Nombre:")
        texto.config(
            bg = "#83D6A8",
            font = "Arial 10 bold"
        )
        texto.place(x=50, y=75)

        nombreIn = Entry(ventanaRegistro)

        nombreIn.place(x=200, y=75)


        #Apellido
        texto = Label(ventanaRegistro, text = "Apellido:")
        texto.config(
            bg = "#83D6A8",
            font = "Arial 10 bold"
        )
        texto.place(x=50, y=125)

        apellidoIn = Entry(ventanaRegistro)
        apellidoIn.place(x=200, y=125)


        #Documento
        texto = Label(ventanaRegistro, text = "N° de documento:")
        texto.config(
            bg = "#83D6A8",
            font = "Arial 10 bold"
        )
        texto.place(x=50, y=175)
        documentoIn = Entry(ventanaRegistro)
        documentoIn.place(x=200,y=175)



        #Teléfono
        texto = Label(ventanaRegistro, text = "Teléfono:")
        texto.config(
            bg = "#83D6A8",
            font = "Arial 10 bold"
        )
        texto.place(x= 375, y=75)
        telefonoIn = Entry(ventanaRegistro)
        telefonoIn.place(x=500, y= 75)

        #Dirección
        texto = Label(ventanaRegistro, text = "Dirección:")
        texto.config(
            bg = "#83D6A8",
            font = "Arial 10 bold"
        )
        texto.place(x=375, y=125)
        direccionIn = Entry(ventanaRegistro)
        direccionIn.place(x=500, y=125)

        #E-mail
        texto = Label(ventanaRegistro, text = "E-mail:")
        texto.config(
            bg = "#83D6A8",
            font = "Arial 10 bold"
        )
        texto.place(x=375, y=175)
        correoIn = Entry(ventanaRegistro)
        correoIn.place(x=500, y=175)

        #Boton ingresar

        botonRegitrar = Button(ventanaRegistro, text = "Registrar empleado")
        botonRegitrar.config(
            font = "Arial 10 bold",
            bg= "darkgray",
            relief = "solid",
            padx = 70,
            pady= 3        
            )
        botonRegitrar.place(x=225, y=300)

        #Boton regresar
        botonVolver = Button(ventanaRegistro, text = "Volver")
        botonVolver.config(
            font = "Arial 10 bold",
            bg= "darkgray",
            relief = "solid",
            padx = 112,
            pady= 3,
            command = ventanaRegistro.destroy       
            )
        botonVolver.place(x=225, y=350)


        ventanaRegistro.mainloop()