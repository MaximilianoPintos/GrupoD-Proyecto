import time
from tkinter import *
from tkinter import ttk
from io import open
import datetime
from tkinter import filedialog as FileDialog

#import PIL

#---------- Variables Globales ---------------
date = datetime.datetime.now() # Fecha/Hora


class Reportes:
    def __init__(self):
        self.titulo = "Reportes"
        #self.icono = "Proyecto/Iconos/Registradora.ico"
        self.resizable = False
        self.color = "#83D6A8"

    def Inicio(self):
        # Iniciar ventana
        ventana_reporte = Tk()
        self.ventana_reporte = ventana_reporte
        # Titulo
        ventana_reporte.title(self.titulo)
        # Tamaño de la ventana
        ox, oy = ventana_reporte.winfo_screenwidth(
        )/5, ventana_reporte.winfo_screenheight()/5
        ventana_reporte.geometry("=520x400+%d+%d" % (ox-150, oy-30))
        # Bloquear el tamaño
        if (self.resizable):
            ventana_reporte.resizable(1, 1)
        else:
            ventana_reporte.resizable(0, 0)
        # Agregar Icono
        #ventana_reporte.iconbitmap(self.icono)
        # Configuraciones
        self.ventana_reporte.config(
            bg=self.color
        )

        ###################### CONTENIDO ##########################
        # Encabezado
        Label(ventana_reporte, text="Por favor, indicanos el problema",
              font=("Arial", 20, "bold"), bg="#83D6A8").place(x=60, y=0)

        # Titulo problema label
        Label(ventana_reporte, text="Inicie Su Reclamo siguiendo el siguiente formato: \n - Fecha y Hora : \n - Reclamo: ", font=(
            "Arial", 15, "bold"), bg="#83D6A8").place(x=35, y=50)

        # Descripcion problema label
        Label(ventana_reporte, text="Descripcion: ", font=(
            "Arial", 15, "bold"), bg="#83D6A8").place(x=5, y=140)
        # Descripcion problema entry
        self.descripcion_entry = Text(ventana_reporte)
        self.descripcion_entry.config(
            width=37,
            height=9,
            bd=3,
            font=("Arial", 12)
        )
        self.descripcion_entry.place(x=135, y=140)

        #Boton enviar
        boton_enviar = Button(ventana_reporte, text = "Guardar", command = self.guardar_txt)
        boton_enviar.config(
            bd = 3,
            relief = RAISED,
            font = ("Arial",14),
            width = 7,
            cursor = "hand2"
        )
        boton_enviar.place(x = 250, y = 340)
        ventana_reporte.mainloop()

    def guardar_txt(self):
        direccion="C:/Users/Masi/Desktop/Python/ProyectoMI/Reportes/ "
        fichero = FileDialog.asksaveasfile(title="Guardar fichero", 
            mode="w", defaultextension=".txt")

        if fichero is not None:
            direccion = fichero.name
            contenido = self.descripcion_entry.get(1.0,'end-1c')
            fichero = open(direccion, 'w+')
            fichero.write(contenido)
            fichero.close()
        else:
            direccion = ""