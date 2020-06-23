from tkinter import *


class Registro: 

    db_name = 'BaseDeDatos.db' 

    def ventana(self):

        ventanaRegistro = Tk()
        ventanaRegistro.geometry("700x400")
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
        
        #Validar
        frameValidar = LabelFrame(ventanaRegistro, text = '')
        frameValidar.config(bg = "#83D6A8")
        val_num = (frameValidar.register(self.lee_numero), '%S')
        val_str = (frameValidar.register(self.lee_str), '%S')

        #Nombre 
        texto = Label(ventanaRegistro, text = "Nombre:")
        texto.config(
            bg = "#83D6A8",
            font = "Arial 10 bold"
        )
        texto.place(x=50, y=75)
        self.nombreIn = Entry(ventanaRegistro, validate = 'key', validatecommand = val_str)
        self.nombreIn.focus()
        self.nombreIn.place(x=200, y=75)


        #Apellido
        texto = Label(ventanaRegistro, text = "Apellido:")
        texto.config(
            bg = "#83D6A8",
            font = "Arial 10 bold"
        )
        texto.place(x=50, y=125)

        self.apellidoIn = Entry(ventanaRegistro, validate = 'key', validatecommand = val_str)
        self.apellidoIn.focus()
        self.apellidoIn.place(x=200, y=125)

        #Documento
        texto = Label(ventanaRegistro, text = "N° de documento:", validate = 'key', validatecommand = val_num)
        texto.config(
            bg = "#83D6A8",
            font = "Arial 10 bold"
        )
        texto.place(x=50, y=175)
        self.documentoIn = Entry(ventanaRegistro)
        self.documentoIn.focus()
        self.documentoIn.place(x=200,y=175)

        #Teléfono
        self.texto = Label(ventanaRegistro, text = "Teléfono:", validate = 'key', validatecommand = val_num)
        self.texto.config(
            bg = "#83D6A8",
            font = "Arial 10 bold"
        )
        texto.place(x= 375, y=75)
        self.telefonoIn = Entry(ventanaRegistro)
        self.telefonoIn.focus()
        self.telefonoIn.place(x=500, y= 75)

        #Dirección
        texto = Label(ventanaRegistro, text = "Dirección:")
        texto.config(
            bg = "#83D6A8",
            font = "Arial 10 bold"
        )
        texto.place(x=375, y=125)
        self.direccionIn = Entry(ventanaRegistro, validate = 'key', validatecommand = val_str)
        self.direccionIn.focus()
        self.direccionIn.place(x=500, y=125)

        #E-mail
        texto = Label(ventanaRegistro, text = "E-mail:")
        texto.config(
            bg = "#83D6A8",
            font = "Arial 10 bold"
        )
        texto.place(x=375, y=175)
        self.correoIn = Entry(ventanaRegistro, validate = 'key', validatecommand = val_str)
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
            command = llenar_tabla
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
    
    #Validar enteros
    @staticmethod
    def lee_numero(aux_0):
        return aux_0.isdigit()
        
    # Validacion Strings
    @staticmethod
    def lee_str(aux_1):
        if aux_1.isalpha() or aux_1.isspace():
            return True
        else:
            return False


    def validarCampos(self):
        if (len(self.nombreIn.get()) != 0 and len(self.apellidoIn.get()) != 0 and len(self.documentoIn.get()) != 0 and len(self.telefonoIn.get()) != 0 and len(self.direccionIn.get()) != ):
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
        self.ejecutar(consulta, parametros)