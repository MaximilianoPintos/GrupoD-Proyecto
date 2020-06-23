from tkinter import *
import sqlite3


class Registro: 

    db_name = 'BaseDatos.db' 

    def Inicio(self):

        ventanaRegistro = Tk()
        # Tamaño de la ventana
        ox, oy = ventanaRegistro.winfo_screenwidth()/5, ventanaRegistro.winfo_screenheight()/5
        ventanaRegistro.geometry("=700x400+%d+%d" % (ox--90, oy--50))
        ventanaRegistro.title("Nuevo empleado")
        ventanaRegistro.resizable(False, False)
        ventanaRegistro.configure(background = "#83D6A8" )

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
        self.texto1 = Label(ventanaRegistro, text = "Nombre:")
        self.texto1.config(
            bg = "#83D6A8",
            font = "Arial 10 bold"
        )
        self.texto1.place(x=50, y=75)
        self.nombreIn = Entry(ventanaRegistro)
        self.nombreIn.focus()
        self.nombreIn.place(x=200, y=75)


        #Apellido
        self.texto2= Label(ventanaRegistro, text = "Apellido:")
        self.texto2.config(
            bg = "#83D6A8",
            font = "Arial 10 bold"
        )
        self.texto2.place(x=50, y=125)

        self.apellidoIn = Entry(ventanaRegistro)
        self.apellidoIn.focus()
        self.apellidoIn.place(x=200, y=125)

        #Documento
        self.texto3 = Label(ventanaRegistro, text = "Documento:")
        self.texto3.config(
            bg = "#83D6A8",
            font = "Arial 10 bold"
        )
        self.texto3.place(x=50, y=175)
        self.documentoIn = Entry(ventanaRegistro)
        self.documentoIn.focus()
        self.documentoIn.place(x=200,y=175)

        #Teléfono
        self.texto4 = Label(ventanaRegistro, text= "Telefono")
        self.texto4.config(
            bg = "#83D6A8",
            font = "Arial 10 bold"
        )
        self.texto4.place(x= 375, y=75)
        self.telefonoIn = Entry(ventanaRegistro)
        self.telefonoIn.focus()
        self.telefonoIn.place(x=500, y= 75)

        #Dirección
        self.texto5 = Label(ventanaRegistro, text = "Dirección:")
        self.texto5.config(
            bg = "#83D6A8",
            font = "Arial 10 bold"
        )
        self.texto5.place(x=375, y=125)
        self.direccionIn = Entry(ventanaRegistro)
        self.direccionIn.focus()
        self.direccionIn.place(x=500, y=125)

        #E-mail
        self.texto6 = Label(ventanaRegistro, text = "E-mail:")
        self.texto6.config(
            bg = "#83D6A8",
            font = "Arial 10 bold"
        )
        self.texto6.place(x=375, y=175)
        self.correoIn = Entry(ventanaRegistro)
        self.correoIn.focus()
        self.correoIn.place(x=500, y=175)



        #Boton ingresar

        botonRegistrar = Button(ventanaRegistro, text = "Registrar empleado")
        botonRegistrar.config(
            font = "Arial 10 bold",
            bg= "darkgray",
            relief = "solid",
            padx = 70,
            pady= 3,
            command = self.llenar_tabla
            )
        botonRegistrar.place(x=225, y=300)

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
    
    def validarCampos(self):
        if (len(self.nombreIn.get()) != 0 and len(self.apellidoIn.get()) != 0 and len(self.documentoIn.get()) != 0 and len(self.telefonoIn.get()) != 0 and len(self.direccionIn.get()) != 0):
            return TRUE
        else:
            return FALSE
    
    def ejecutar(self, consulta, parametros = ()):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()    
            resultado = cursor.execute(consulta, parametros)
            conn.commit()
            return resultado
        raise Exception('Error')
    
    def llenar_tabla(self):
        if self.validarCampos() == TRUE:
            consulta = 'INSERT INTO Personal VALUES(NULL, ?, ?, ?, ?, ?, ?)'
            parametros = (self.nombreIn.get(), self.apellidoIn.get(), self.documentoIn.get(), self.telefonoIn.get(), self.correoIn.get(), self.direccionIn.get())
            self.nombreIn.delete(0,END)
            self.apellidoIn.delete(0,END)
            self.documentoIn.delete(0,END)
            self.telefonoIn.delete(0,END)
            self.direccionIn.delete(0,END)
            self.correoIn.delete(0,END)

            self.ejecutar(consulta, parametros)
            