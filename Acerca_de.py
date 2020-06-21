from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from datetime import date
from datetime import datetime
import time
import PIL


class AcercaDe:
    def __init__(self):
        self.titulo = "Acerca De"
        self.icono = "./Iconos/Registradora.ico"
        self.resizable = False
        self.color = "#83D6A8"

    def Inicio(self):
        # Iniciar ventana
        ventana_acercade = Tk()
        self.ventana_acercade = ventana_acercade
        # Titulo
        ventana_acercade.title(self.titulo)
        # Tamaño de la ventana
        ox, oy = ventana_acercade.winfo_screenwidth(
        )/5, ventana_acercade.winfo_screenheight()/5
        ventana_acercade.geometry("=800x600+%d+%d" % (ox--50, oy-100))
        # Bloquear el tamaño
        if (self.resizable):
            ventana_acercade.resizable(1, 1)
        else:
            ventana_acercade.resizable(0, 0)
        # Agregar Icono
        ventana_acercade.iconbitmap(self.icono)
        # Configuraciones
        self.ventana_acercade.config(
            bg=self.color
        )

        ######################### CONTENIDO ########################################
        # Label
        Label(ventana_acercade, text="P.R.S VENTAS", font=(
            "Arial", 30, "bold"), bg="#83D6A8").place(x=150, y=60)
        # Imagen
        ancho = 200
        largo = 150
        img = PIL.Image.open("./Iconos/Loguito.jpg")
        img.thumbnail((ancho, largo), Image.ANTIALIAS)
        render = PIL.ImageTk.PhotoImage(img, master=ventana_acercade)
        label_imagen = Label(ventana_acercade, image=render,
                             width=ancho, height=largo)
        label_imagen.config(
            bg="#83D6A8"
        )
        label_imagen.place(x=440, y=0)

        #### INFORMACION ###
        # Info ventas
        ventas = LabelFrame(ventana_acercade)
        ventas.config(
            text="Ventas",
            width=800,
            height=60,
            bd=2,
            font=("Arial", 12, "bold"),
            bg="#83D6A8"
        )
        ventas.place(x=0, y=170)
        
        info_ventas = Label(ventas)
        info_ventas.config(
            text = ('Esta ventana contiene todo lo necesario para'
                    ' realizar las actividadades diaras de ventas en el'
                    ' comercio.'),
            wraplength = 800,
            font= ("Arial",12,"bold"),
            bd = 3,
            bg = "#83D6A8"
        )
        info_ventas.place(x=0,y=0)

        # Info Proveedores
        proveedores = LabelFrame(ventana_acercade)
        proveedores.config(
            text="Proveedores",
            width=800,
            height=70,
            bd=2,
            font=("Arial", 12, "bold"),
            bg="#83D6A8"
        )
        proveedores.place(x=0, y=230)

        info_prov= Label(proveedores)
        info_prov.config(
            text = ('Aqui encontraremos información acerca de todos los'
                    ' proovedores registrados en el comercio, como también'
                    ' la opción de agregar o quitar.'),
            wraplength = 800,
            font= ("Arial",12,"bold"),
            bd = 3,
            bg = "#83D6A8"
        )
        info_prov.place(x=0,y=0)

        # Info Productos
        productos = LabelFrame(ventana_acercade)
        productos.config(
            text="Productos",
            width=800,
            height=70,
            bd=2,
            font=("Arial", 12, "bold"),
            bg="#83D6A8"
        )
        productos.place(x=0, y=300)

        info_prod= Label(productos)
        info_prod.config(
            text = ('Esta pestaña contiene información sobre el stock del'
                    ' comercio, precios, descripciones y otros elementos'
                    ' útiles a la hora de cargar, editar o eliminar stock.'),
            wraplength = 800,
            font= ("Arial",12,"bold"),
            bd = 3,
            bg = "#83D6A8"
        )
        info_prod.place(x=0,y=0)

        # Info Efectivo en caja
        efectivo = LabelFrame(ventana_acercade)
        efectivo.config(
            text="Efectivo en caja",
            width=800,
            height=70,
            bd=2,
            font=("Arial", 12, "bold"),
            bg="#83D6A8"
        )
        efectivo.place(x=0, y=370)

        info_efec= Label(efectivo)
        info_efec.config(
            text = ('Aquí,de manera muy sensilla, se podrá consultar el'
                    ' dinero en efectivo que se encuentra en caja hasta'
                    ' el momento.'),
            wraplength = 800,
            font= ("Arial",12,"bold"),
            bd = 3,
            bg = "#83D6A8"
        )
        info_efec.place(x=0,y=0)

        # Info Ultimos movimientos
        movimientos = LabelFrame(ventana_acercade)
        movimientos.config(
            text="Ultimos movimientos",
            width=800,
            height=70,
            bd=2,
            font=("Arial", 12, "bold"),
            bg="#83D6A8"
        )
        movimientos.place(x=0, y=440)

        info_mov= Label(movimientos)
        info_mov.config(
            text = ('Ventana donde podrán visualizarse las ultimas venta'
                    ' realizadas por orden de llegada.'
                    ),
            wraplength = 800,
            font= ("Arial",12,"bold"),
            bd = 3,
            bg = "#83D6A8"
        )
        info_mov.place(x=0,y=0)

        ventana_acercade.mainloop()
