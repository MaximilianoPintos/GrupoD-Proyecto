from tkinter import *
from tkinter import ttk
from datetime import date
from datetime import datetime
from Efectivo_en_caja import *
import sqlite3
import time


class Retiro:

    bd_name = 'BaseDatos.db'

    def Inicio(self):
        self.titulo = "Retiros"
        self.icono = "./Iconos/Registradora.ico"
        self.resizable = False
        self.color = "#83D6A8"

        # Iniciar ventana
        ventana_retiro = Tk()
        self.ventana_retiro = ventana_retiro

        # Titulo
        ventana_retiro.title(self.titulo)

        # Tamaño de la ventana
        ox, oy = ventana_retiro.winfo_screenwidth()/5, ventana_retiro.winfo_screenheight()/5
        ventana_retiro.geometry("=400x200+%d+%d" % (ox--220, oy--70))

        # Bloquear el tamaño
        if (self.resizable):
            ventana_retiro.resizable(1, 1)
        else:
            ventana_retiro.resizable(0, 0)

        # Agregar Icono
        ventana_retiro.iconbitmap(self.icono) 

        # Configuraciones
        self.ventana_retiro.config(
            bg=self.color
        )

        validacion_str = ()

        ############################ CONFIGURACIONES DE LA VENTANA #####################################
        # Label Cantidad Retiro
        Label(ventana_retiro, text="Cantidad de retiro: ",
              font=("Arial", 14, "bold"), bg="#83D6A8").place(x=30, y=4)
        # Entry cantidad retiro
        self.cantidad_retiro = Entry(ventana_retiro)
        self.cantidad_retiro.config(
            font=("Arial", 12),
            width=15,
            bd=2,
            justify="center"
        )
        self.cantidad_retiro.place(x=230, y=6)

        # Label Nombre empleado
        Label(ventana_retiro, text="Nombre empleado: ",
              font=("Arial", 14, "bold"), bg="#83D6A8").place(x=30, y=38)
        # Entry Mombre empleado
        self.nombre_empleado = Entry(ventana_retiro)
        self.nombre_empleado.config(
            font=("Arial", 12),
            width=15,
            bd=2,
            justify="center"
        )
        self.nombre_empleado.place(x=230, y=40)

        # Label fecha
        Label(ventana_retiro, text="Fecha: ",
              font=("Arial", 14, "bold"), bg="#83D6A8").place(x=70, y=72)
        # Entry fecha
        self.fecha_actual = datetime.now()
        formato = self.fecha_actual.strftime('%d / %m / %Y')
        self.fecha = Label(ventana_retiro, text = formato)
        self.fecha.config(
            bg = "#83D6A8",
            font = ("Arial", 14)
        )
        self.fecha.place(x=240,y=72)

        # Label hora
        Label(ventana_retiro, text="Hora: ",
              font=("Arial", 14, "bold"), bg="#83D6A8").place(x=75, y=105)
        # Entry hora
        def times():
            current_time = time.strftime('Hora: %H:%M')
            hora.config(
            text = current_time,
            bg = "#83D6A8",
            font = ("Arial", 14)
            )
            hora.after(200,times)

        hora = Label(ventana_retiro)
        times()
        hora.place(x=250, y=108)

        ################# BOTONES #######################
        #Boton aceptar
        boton_retiro = Button(ventana_retiro, text="Aceptar", command = self.cargar_datos)
        boton_retiro.config(
            width = 40,
            bd = 3,
            relief = RAISED,
            font = ("Arial",13, "bold"),
            cursor = "hand2"
        )
        boton_retiro.place(x= 0, y = 165)

        ventana_retiro.mainloop()

        # Validacion todos los campos llenos
    def validacion(self):
        if (len(self.nombre_empleado.get()) != 0 and len(self.cantidad_retiro.get()) != 0):
            return TRUE
        else:
            return FALSE

    # 'Chekeo' de la tabla
    def ejecuta_consulta(self, consulta, parametros = ()):
        with sqlite3.connect(self.bd_name) as conn:
            cursor = conn.cursor()    
            resultado = cursor.execute(consulta, parametros)
            conn.commit()
            return resultado
        raise Exception(' NO SE PUDO CONECTAR A LA BASE DE DATOS. ')

    def cargar_datos(self):
        if self.validacion() == TRUE:
            consult = 'INSERT INTO Retiros VALUES(NULL, ?, ?, ?)'
            parametros = (self.nombre_empleado.get(), self.cantidad_retiro.get(), self.fecha_actual)
            self.ejecuta_consulta(consult, parametros)
            self.nombre_empleado.delete(0, END)
            self.cantidad_retiro.delete(0, END)
            self.ventana_retiro.destroy()
    # Validacion Str
    @staticmethod
    def lee_str(aux_1):
        if aux_1.isalpha() or aux_1.isspace():
            return True
        else:
            return False