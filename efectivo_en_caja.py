from tkinter import *
from tkinter import ttk
import sqlite3
from PIL import ImageTk, Image
import PIL


class Efectivo:
    db_nombre = 'Proyecto\BaseDatos.db'
    def __init__(self):
        self.titulo = "Dinero"
        self.icono = "Proyecto/Iconos/Registradora.ico"
        self.resizable = False
        self.color = "#83D6A8"

    def Inicio(self):
        # Iniciar ventana
        ventana_efectivo = Tk()
        self.ventana_efectivo = ventana_efectivo
        # Titulo
        ventana_efectivo.title(self.titulo)
        # Tamaño de la ventana
        ox, oy = ventana_efectivo.winfo_screenwidth(
        )/5, ventana_efectivo.winfo_screenheight()/5
        ventana_efectivo.geometry("=500x250+%d+%d" % (ox--150, oy--30))
        # Bloquear el tamaño
        if (self.resizable):
            ventana_efectivo.resizable(1, 1)
        else:
            ventana_efectivo.resizable(0, 0)
        # Agregar Icono
        ventana_efectivo.iconbitmap(self.icono)
        # Configuraciones
        self.ventana_efectivo.config(
            bg=self.color
        )
        #### CONTENIDO ####
        Label(ventana_efectivo, text="Efectivo en caja:",
              font=("Arial", 26, "bold"), bg="#83D6A8").place(x = 110, y = 20)

        self.marco = LabelFrame(ventana_efectivo)
        self.marco.config(
            width = 400,
            height = 100,
            bg = "#83D6A8",
            bd = 5,
        )
        self.marco.place(x =50, y = 80)

        self.label_marco = Label(self.marco)
        self.label_marco.config(
            font=("arial 30 bold"),
            bg = "#83D6A8",
            bd = 5
        )
        self.label_marco.place(x =143, y = 10)


               # Connect to database
        db = sqlite3.connect(self.db_nombre)
        c = db.cursor()
        c.execute("SELECT SUM(Precio) FROM Ventas")
        total = c.fetchall()
        self.label_marco.config(
            font=("Arial",30,"bold"),
            bg = "#83D6A8",
            text= total
            )
        c.close()

        ventana_efectivo.mainloop()