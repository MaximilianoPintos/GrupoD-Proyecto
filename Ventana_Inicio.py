from tkinter import *
from PIL import Image, ImageTk
from datetime import date
from datetime import datetime
import time
from Ventana_Ventas import *
from tkinter import messagebox

ventas = Ventas()


class Programa:
    def __init__(self):
        self.titulo = "Sistema de ventas"
        self.icono = "./Iconos/Registradora.ico"
        self.resizable = False
        self.color = "#83D6A8"

    def Inicio(self):
        # Iniciar ventana
        ventana_principal = Tk()
        self.ventana_principal = ventana_principal
        # Titulo
        ventana_principal.title(self.titulo)
        # Tamaño de la ventana
        ox,oy=ventana_principal.winfo_screenwidth()/5,ventana_principal.winfo_screenheight()/5
        ventana_principal.geometry("=960x650+%d+%d" % (ox-50,oy-100) )
        # Bloquear el tamaño
        if (self.resizable):
            ventana_principal.resizable(1, 1)
        else:
            ventana_principal.resizable(0, 0)
        # Agregar Icono
        ventana_principal.iconbitmap(self.icono)
        # Configuraciones
        self.ventana_principal.config(
            bg=self.color
        )
        #######################################################################################
        #Frame logo
        frame1 = LabelFrame(self.ventana_principal, text = "Opciones Usuario")
        frame1.config(
            bg = "#83D6A8",
            bd = 5,
            width = 200,
            height = 500,
            font = ("Arial",14)
        )
        frame1.place(x = 40, y = 120)
        #Frame Menú
        frame2 = LabelFrame(self.ventana_principal, text = "Menú de opciones")
        frame2.config(
            bg = "#83D6A8",
            bd = 5,
            width = 660,
            height = 500,
            font =("Arial",14)
        )
        frame2.place(x = 260, y = 120)
        #Frame franja
        frame3 =Frame(self.ventana_principal)
        frame3.config(
            bg = "#4089D1",
            bd = 3,
            width = 880,
            height = 50
        )
        frame3.place(x = 40, y = 15)
        
        
        # Imagen
        #Dimensiones globales
        global ancho
        global largo
        ancho = 185
        largo = 150
        
        imagen = Image.open("./Iconos/Loguito.jpg")
        imagen.thumbnail((ancho, largo), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(imagen)
        label_imagen =Label(frame1, image=render,
              width=ancho, height=largo)
        label_imagen.config(
            bg = "#83D6A8"
        )
        label_imagen.place(x=0, y=0)
        
        #################  Botones Frame1 ############################
        boton_retiro = Button(frame1, text="Retiro")#command = retiro.Inicio
        boton_retiro.config(
            font=("Arial", 14),
            relief=RAISED,
            padx=43,
            pady = 2,
            bd=3

        )
        boton_retiro.place(x = 18, y = 160)
        ############################################################
        boton_reporte = Button(frame1, text="Reportes")#command = reporte.Inicio
        boton_reporte.config(
            font=("Arial", 14),
            relief=RAISED,
            padx=29,
            pady = 2,
            bd=3

        )

        boton_reporte.place(x = 18, y = 220)

        ##############################################################  
        boton_empleados = Button(frame1, text="Empleados")
        boton_empleados.config(
            font=("Arial", 14),
            relief=RAISED,
            padx=19,
            pady = 2,
            bd=3

        )
        boton_empleados.place(x = 19, y = 280)
        ##############################################################  
        boton_salir = Button(frame1, text="Salir", command = quit)
        boton_salir.config(
            font=("Arial", 14),
            relief=RAISED,
            padx=50,
            pady = 2,
            bd=3

        )
        
        boton_salir.place(x = 19, y = 340)

        ################## Botones Frame 2 ############################
        #Boton Ventas
        ancho = 140
        largo = 140
        img_boton = Image.open("./Iconos/carrito.jpg")
        img_boton.thumbnail((ancho, largo), Image.ANTIALIAS)
        render1 = ImageTk.PhotoImage(img_boton)
        boton = Button(frame2,image = render1, text = "Ventas", compound = "top",command = ventas.Inicio)
        boton.config(
            font = ("Arial", 14),
            width = 150,
            height = 160,
            relief = RAISED,
            bd = 4
        )
        boton.place(x = 20, y =50)
        #Boton Proveedores
        ancho = 140
        largo = 140
        img_boton2 = Image.open("./Iconos/Proveedores.jpg")
        img_boton2.thumbnail((ancho, largo), Image.ANTIALIAS)
        render2 = ImageTk.PhotoImage(img_boton2)
        boton = Button(frame2,image = render2, text = "Proveedores", compound = "top")#command = proveedores.Inicio
        boton.config(
            font = ("Arial", 14),
            width = 150,
            height = 160,
            relief = RAISED,
            bd = 4
        )
        boton.place(x = 240, y =50)
        
        #Boton Stock
        ancho = 140
        largo = 140
        img_boton3 = Image.open("./Iconos/Productos.jpg")
        img_boton3.thumbnail((ancho, largo), Image.ANTIALIAS)
        render3 = ImageTk.PhotoImage(img_boton3)
        boton = Button(frame2,image = render3, text = "Productos", compound = "top")#command = produtos.Inicio
        boton.config(
            font = ("Arial", 14),
            width = 150,
            height = 160,
            relief = RAISED,
            bd = 4
        )
        boton.place(x = 460 , y =50)

        #Boton Dinero en Caja
        ancho = 140
        largo = 120
        img_boton5 = Image.open("./Iconos/Caja Fuerte.png")
        img_boton5.thumbnail((ancho, largo), Image.ANTIALIAS)
        render5 = ImageTk.PhotoImage(img_boton5)
        boton = Button(frame2,image = render5, text = "Efectivo en Caja", compound = "top")#command = efectivo.Inicio
        boton.config(
            font = ("Arial", 14),
            width = 150,
            height = 160,
            relief = RAISED,
            bd = 4
        )
        boton.place(x = 20 , y =270)

        #Boton Ultimos Movimientos
        ancho = 140
        largo = 120
        img_boton6 = Image.open("./Iconos/Ultimos Movimientos.jpg")
        img_boton6.thumbnail((ancho, largo), Image.ANTIALIAS)
        render6 = ImageTk.PhotoImage(img_boton6)
        boton = Button(frame2,image = render6,text = "Movimientos",compound = "top")#command =movimientos.Inicio 
        boton.config(
            font = ("Arial", 14),
            width = 150,
            height = 160,
            relief = RAISED,
            bd = 4
        )
        boton.place(x = 240 , y =270)
        
        #Boton Acerca De
        ancho = 140
        largo = 120
        img_boton8 = Image.open("./Iconos/AcercaDe.png")
        img_boton8.thumbnail((ancho, largo), Image.ANTIALIAS)
        render8 = ImageTk.PhotoImage(img_boton8)
        boton = Button(frame2,image = render8,text = "Acerca de",compound = "top")#command = acercade.Inicio
        boton.config(
            font = ("Arial", 14),
            width = 150,
            height = 160,
            relief = RAISED,
            bd = 4
        )
        boton.place(x = 460 , y =270)

        ###################### Textos ##############################
        texto = Label(self.ventana_principal, text = "NOMBRE DEL NEGOCIO")
        texto.config(
            bg ="#83D6A8",
            font = ("Arial", 20)
        )
        texto.place(x = 530,y=75)
        ###################### Fecha y hora ########################
        ###### Fecha #########
        fecha_actual = datetime.now()
        formato = fecha_actual.strftime('Fecha: %d / %m / %Y')
        fecha = Label(frame3, text = formato)
        fecha.config(
            bg = "#4089D1",
            font = ("Arial", 14)
        )
        fecha.place(x=210,y=0)
        ####### Hora ############
        def times():
            current_time = time.strftime('Hora: %H:%M:%S')
            hora.config(
            text = current_time,
            bg = "#4089D1",
            font = ("Arial", 14)
            )
            hora.after(200,times)

        hora = Label(frame3)
        hora.place(x= 450,y=0)
        times()
        self.ventana_principal.mainloop()

