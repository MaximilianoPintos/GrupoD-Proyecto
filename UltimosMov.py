from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import sqlite3
import datetime


class Movimientos:
    db_nombre = 'BaseDatos.db'  # Llamado a la base de datos
    def Inicio(self):
        movimientos = Tk()
        movimientos.config(bg="#83D6A8")
        movimientos.resizable(0, 0)
        movimientos.title("Ultimos movimientos")
        self.icono = "@/home/martin/Escritorio/GrupoD-Proyecto/Iconos/Registradora.xbm"
        movimientos.iconbitmap(self.icono)

        # ------------ Centrado de Ventana en pantalla ------------
        ox, oy = movimientos.winfo_screenwidth(
        )/2, movimientos.winfo_screenheight()/2
        movimientos.geometry("=800x490+%d+%d" % (ox-430, oy-300))

        #################### Tablita ##############################
        espacio = Frame(movimientos)
        espacio.config(
            width=730,
            height=408
        )
        espacio.place(x=30, y=10)

        # Tabla
        self.tabla = ttk.Treeview(espacio, height=19, columns=(
            '#1', '#2'), selectmode="browse")
        self.tabla.place(x=0, y=0)

        self.tabla.heading("#0", text="FECHA Y HORA ", anchor=CENTER)
        self.tabla.heading("#1", text="N° DE TICKET", anchor=CENTER)
        self.tabla.heading("#2", text="DESCRIPCION", anchor=CENTER)

        self.tabla.column("#0", width=200, stretch=False, anchor=CENTER)
        self.tabla.column("#1", width=150, stretch=False, anchor=CENTER)
        self.tabla.column("#2", width=376, stretch=False, anchor=CENTER)


        ############## BOTONES ###################################


        boton_salir = Button(movimientos, text="Salir",
                             command=movimientos.destroy)
        boton_salir.config(
            bd=3,
            relief=RAISED,
            width=35,
            font=("Arial", 17),
            cursor="hand2"
        )
        boton_salir.place(x=180, y=435)
        self.obtener_producto()
        movimientos.mainloop()

    # --------------------------- Funcion Ejecutar consulta a base de datos ----------------------------------------------------------------------
    def ejecuta_consulta(self, consulta, parametros=()):
        # Base de datos
        with sqlite3.connect(self.db_nombre) as conn:
            cursor = conn.cursor()
            result = cursor.execute(consulta, parametros)
            conn.commit()
            return result
        raise Exception("No se pudo conectar con la DB")
    # --------------------------------------------------------------------------------------------------------------------------------------------
    # --------------------------- funcion obtener productos --------------------------------------------------------------------------------------
    def obtener_producto(self):
        # limpiando tabla
        records = self.tabla.get_children()
        for element in records:
            self.tabla.delete(element)
        # Consulta de datos
        consulta = 'SELECT * FROM Ventas'
        filasBD = self.ejecuta_consulta(consulta)
        # relleno de datos
        for row in filasBD:
            self.tabla.insert('', 9999, text=row[4], values=(row[0],row[1]))