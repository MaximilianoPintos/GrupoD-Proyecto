from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import sqlite3 
import datetime
import os 
import random

#---------- Variables Globales ---------------
date= datetime.datetime.now().date()

lista_producto = []
precio_product = []
cantidad_producto = []
id_producto = []
precio_Unitario = []
descuentos = []

def generar_factura(self):
            # Ruta
        ruta = "C:/Users/Masi/Desktop/Respaldo codigos/ramdon/Facturas/" + str(date)
        if not os.path.exists(ruta):
            os.makedirs(ruta)

        # Plantilla
        empresa = "\t\t\t\tMinimarket de Amigos S.A\n"
        direccion = "\t\t\t\tMendoza, Argentina\n"
        contacto = "\t\t\t\tContacto: 2614705854\n\n"
        factura= "\t\t\t\t\tFactura\n\n"
        dt="\t\t\t\t\t" + str(date) + "\n"

        tabla = "\t-----------------------------------------------------------------\n\t\tS.A\t\tProducto\t\tCantidad\t\tPrecio\t\t\t\t\n"
        tabla2 = "\t-----------------------------------------------------------------"
        final = empresa + direccion + contacto + factura + dt + "\n" + tabla + tabla2

        # abrir archivo
        nombre_archivo = str(ruta) + " " +  str(random.randrange(0,9999)) + ".rtf"
        archivo= open(nombre_archivo, "w")
        archivo.write(final)

        # factura dinamica

        r = 1
        i = 0
        for t in lista_producto:
            archivo.write("\n\t\t" + str(r) + "\t\t" + str(lista_producto[i]+ "       ")[:15] + "\t\t" + str(cantidad_producto[i]) + "\t\t" + str(precio_product[i]))
            i += 1
            r += 1
        archivo.write("\n\n\n\n\t-----------------------------------------------------------------\n")
        archivo.write("\n\t\t\t\t\t\t\t\t\tTotal : $ " + str(sum(precio_product)))
        archivo.write("\n\n\t\t\t\t\t\t\t\tGracias Por Su Compra.\n")
        archivo.write("\t-----------------------------------------------------------------\n")
        archivo.close()
        messagebox.showinfo("Excelente", "Factura Generada Con Exito!")