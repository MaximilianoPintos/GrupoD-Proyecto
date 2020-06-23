from tkinter import *
from tkinter import ttk
import PIL
from PIL import Image
from PIL import ImageTk
from datetime import *
import time
import sqlite3
from tkinter import messagebox
from tkinter import filedialog
import datetime
import os 
import random


lista_producto = []
precio_product = []
cantidad_producto = []
id_producto = []
precio_Unitario = []
descuentos = []

date = datetime.datetime.now()
date2= datetime.datetime.now().date()
class Ventas:
    db_nombre = 'BaseDatos.db'  # Llamado a la base de datos

    def __init__(self, *args, **kwargs):
        self.titulo = "Ventas"
        self.icono = "./Iconos/Registradora.ico"
        self.resizable = False
        self.color = "#83D6A8"

    def Inicio(self):
        # Iniciar ventana
        ventana_ventas = Tk()
        self.ventana_ventas = ventana_ventas
        # Titulo
        ventana_ventas.title(self.titulo)
        # Tamaño de la ventana
        ox, oy = ventana_ventas.winfo_screenwidth()/5, ventana_ventas.winfo_screenheight()/5
        ventana_ventas.geometry("=1300x650+%d+%d" % (ox-200, oy-100))
        # Bloquear el tamaño
        if (self.resizable):
            ventana_ventas.resizable(1, 1)
        else:
            ventana_ventas.resizable(0, 0)
        # Agregar Icono
        ventana_ventas.iconbitmap(self.icono)
        # Configuraciones
        self.ventana_ventas.config(
            bg=self.color
        )

    ################################### CONTENIDO DE LA VENTANA #####################################
        ################# FRAMES #####################
        # Frame Izquierda
        self.frame1 = LabelFrame(ventana_ventas)
        self.frame1.config(
            bg="#83D6A8",
            bd=5,
            height=400,
            width=570
        )
        self.frame1.place(x=10, y=10)
        # Frame Derecha
        frame2 = LabelFrame(ventana_ventas)
        frame2.config(
            bg="#83D6A8",
            bd=5,
            height=440,
            width=700
        )
        frame2.place(x=590, y=10)
        # Frame Izquierda abajo
        self.frame3 = LabelFrame(ventana_ventas)
        self.frame3.config(
            bg="#83D6A8",
            bd=5,
            height=230,
            width=570
        )
        self.frame3.place(x=10, y=410)
        # Frame 2 Derecha abajo
        frame4 = LabelFrame(ventana_ventas)
        frame4.config(
            bg="#83D6A8",
            bd=5,
            height=185,
            width=350
        )
        frame4.place(x=590, y=453)
        # Frame 2 Izquierda abajo
        frame5 = LabelFrame(ventana_ventas)
        frame5.config(
            bg="#83D6A8",
            bd=5,
            height=185,
            width=350
        )
        frame5.place(x=940, y=453)
        ################ CONTENIDO DE FRAMES ####################
        ######### IZQUIERDA ##############
        label1 = Label(self.frame1, text="P.R.S Ventas")
        label1.config(
            bg="#83D6A8",
            font=("Arial", 30)
        )
        label1.place(x=80, y=20)
        # Imagen
        ancho = 140
        largo = 70
        img = PIL.Image.open("./Iconos/Loguito.jpg")
        img.thumbnail((ancho, largo), Image.ANTIALIAS)
        render = PIL.ImageTk.PhotoImage(img, master=ventana_ventas)
        label_imagen = Label(self.frame1, image=render,
                             width=ancho, height=largo)
        label_imagen.config(
            bg="#83D6A8"
        )
        label_imagen.place(x=320, y=0)

        # id
        Label(self.frame1, text="Código: ", font=(
            "Arial", 20, "bold"), bg="#83D6A8").place(x=0, y=90)
        # Entry
        self.campo_id = Entry(self.frame1)
        self.campo_id.config(
            width=20,
            justify="center",
            font=("Arial", 15)
        )
        self.campo_id.place(x=120, y=95)
        ######## Botones id ##################
        # Boton buscar
        boton_buscar = Button(self.frame1, text="Buscar",
                              command=self.BuscarProducto)
        boton_buscar.config(
            font=("Arial", 12),
            relief=RAISED,
            bd=3,
            width=8,
            cursor="hand2"
        )
        boton_buscar.place(x=360, y=92)
        # Boton lista
        boton_lista = Button(self.frame1, text="Lista ID",
                             command=self.ListaId)
        boton_lista.config(
            font=("Arial", 12),
            relief=RAISED,
            bd=3,
            width=8,
            cursor="hand2"
        )
        boton_lista.place(x=450, y=92)
        ################# Resultados de busqueda ###################
        # Nombre producto
        self.nombre_producto = Label(self.frame1, text="Nombre:", font=(
            "Arial", 15, "bold"), bg="#83D6A8")
        self.nombre_producto.place(x=0, y=145)
        # Precio producto
        self.precio_producto = Label(self.frame1, text="Precio  :", font=(
            "Arial", 15, "bold"), bg="#83D6A8")
        self.precio_producto.place(x=2, y=175)
        
        # Cantidad de productos
        self.cantidad_producto = Label(self.frame1, text="Ingrese Cantidad: ",
                                       font=("Arial", 17, "bold"), bg="#83D6A8")
        self.cantidad_producto.place(x=0, y=220)
        # Entry
        self.campo_cantidad = Entry(self.frame1)
        self.campo_cantidad.config(
            width=15,
            justify="center",
            font=("Arial", 15)
        )
        self.campo_cantidad.place(x=210, y=223)

        # Descuento
        Label(self.frame1, text="Descuento (%): ", font=(
            "Arial", 18, "bold"), bg="#83D6A8").place(x=0, y=270)
        # Entry
        self.campo_descuento = Entry(self.frame1)
        self.campo_descuento.config(
            width=15,
            justify="center",
            font=("Arial", 15)
        )
        self.campo_descuento.place(x=210, y=273)

        # Boton Agregar Venta
        boton_agregar_venta = Button(
        self.frame1, text="Agregar", command=self.AgregarVenta)
        boton_agregar_venta.config(
            width=49,
            relief=RAISED,
            font=("Arial", 14),
            bd=3,
            cursor="hand2"
        )
        boton_agregar_venta.place(x=4, y=345)
        # Paga con
        Label(self.frame3, text="Paga con: ", font=(
            "Arial", 18, "bold"), bg="#83D6A8").place(x=1, y=3)

        # Entry
        self.campo_pagacon = Entry(self.frame3)
        self.campo_pagacon.config(
            width=25,
            justify="center",
            font=("Arial", 15)
        )
        self.campo_pagacon.place(x=140, y=7)

        # Boton Vuelto
        boton_vuelto = Button(self.frame3, text="Calcular vuelto", command = self.PagaCon)
        boton_vuelto.config(
            width=13,
            relief=RAISED,
            bd=3,
            font=("Arial", 12),
            cursor="hand2"
        )
        boton_vuelto.place(x=425, y=5)

        # Su vuelto
        self.vuelto= Label(self.frame3, text="Su vuelto es: ", font=(
            "Arial", 17, "bold"), bg="#83D6A8")
        self.vuelto.place(x=1, y=60)
        # Boton limpiar vuelto
        boton_limpiar_vuelto = Button(self.frame3, text="Limpiar", command = self.LimpiarVuelto)
        boton_limpiar_vuelto.config(
            relief=RAISED,
            bd=3,
            font=("Arial", 15),
            width=50,
            cursor="hand2"
        )
        boton_limpiar_vuelto.place(x=0, y=177)
        ######################## DERECHA ###############################
        # Tabla
        self.tabla = ttk.Treeview(frame2, height=20, columns=(
            '#1', '#2', '#3', '#4'), selectmode="browse")
        self.tabla.place(x=0, y=0)

        self.tabla.heading('#0', text="id", anchor=CENTER)
        self.tabla.heading('#1', text="Descripción", anchor=CENTER)
        self.tabla.heading('#2', text="Cantidad", anchor=CENTER)
        self.tabla.heading('#3', text="Precio unitario", anchor=CENTER)
        self.tabla.heading('#4', text="Precio total", anchor=CENTER)

        self.tabla.column("#0", width=50, stretch=False, anchor=CENTER)
        self.tabla.column("#1", width=340, stretch=False, anchor=CENTER)
        self.tabla.column("#2", width=95, stretch=False, anchor=CENTER)
        self.tabla.column("#3", width=100, stretch=False, anchor=CENTER)
        self.tabla.column("#4", width=100, stretch=False, anchor=CENTER)

        # Descuentos
        self.labelDescuento = Label(frame4, text="Descuentos: ", font=(
            "Arial", 15, "bold"), bg="#83D6A8")
        self.labelDescuento.place(x=0, y=0)
        # Total
        self.Total = Label(frame4, text="TOTAL: ", font=(
            "Arial", 17, "bold"), bg="#83D6A8")
        self.Total.place(x=0, y=80)

        # Botones Frame 4

        # Boton Confirmar
        boton_confirmar = Button(frame4, text="Confirmar Venta", command = self.ConfirmarVenta)
        boton_confirmar.config(
            bd=3,
            relief=RAISED,
            width=24,
            font=("Arial", 17),
            cursor="hand2"
        )
        boton_confirmar.place(x=4, y=125)

        # Botones Frame 5
        # Boton Ticket
        boton_recibo = Button(frame5, text="Generar Recibo", command = self.generar_factura)
        boton_recibo.config(
            bd=3,
            relief=RAISED,
            width=24,
            font=("Arial", 17),
            cursor="hand2"
        )
        boton_recibo.place(x=4, y=9)
        # Boton borrar
        boton_borrar = Button(frame5, text="Borrar Venta", command = self.BorrarVenta)
        boton_borrar.config(
            bd=3,
            relief=RAISED,
            width=24,
            font=("Arial", 17),
            cursor="hand2"
        )
        boton_borrar.place(x=4, y=65)
        # Boton Salir
        boton_salir = Button(frame5, text="Salir",
                             command=ventana_ventas.destroy)
        boton_salir.config(
            bd=3,
            relief=RAISED,
            width=24,
            font=("Arial", 17),
            cursor="hand2"
        )
        boton_salir.place(x=4, y=124)

        self.ventana_ventas.mainloop()

    ################################### FUNCIONES ##################################################
    def EjecutarConsulta(self, consulta, parametros=()):
        # Base de datos
        with sqlite3.connect(self.db_nombre) as conn:
            cursor = conn.cursor()
            result = cursor.execute(consulta, parametros)
            conn.commit()
            return result
        raise Exception("No se pudo conectar con la DB")

    def ObtenerProducto(self):
        # limpiando tabla
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        # Consulta de datos
        consulta = 'SELECT * FROM Productos'
        self.filasBD = self.EjecutarConsulta(consulta)
        # relleno de datos
        for row in self.filasBD:
            self.tree.insert('', 9999, text=row[0], values=(
                row[1], row[2], row[3]))

    def ListaId(self):
        ventana_buscar = Toplevel()
        ventana_buscar.iconbitmap(self.icono)
        ventana_buscar.config(
            background="#83D6A8",
            relief=SOLID,
            bd=3
        )
        ventana_buscar.resizable(0, 0)
        # Tamaño de la ventana
        ox, oy = ventana_buscar.winfo_screenwidth()/2, ventana_buscar.winfo_screenheight()/2
        ventana_buscar.geometry("=593x234+%d+%d" % (ox-300, oy-200))
        # tabla
        self.tree = ttk.Treeview(
            ventana_buscar, height=10, columns=('#1', '#2', '#3'))
        self.tree.grid(row=0, column=0, columnspan=2)
        self.tree.heading("#0", text="id", anchor=CENTER)
        self.tree.heading("#1", text="Nombre", anchor=CENTER)
        self.tree.heading("#2", text="Stock", anchor=CENTER)
        self.tree.heading("#3", text="Precio", anchor=CENTER)

        self.tree.column("#0", width=50, stretch=False, anchor=CENTER)
        self.tree.column("#1", width=340, stretch=False, anchor=CENTER)
        self.tree.column("#2", width=95, stretch=False, anchor=CENTER)
        self.tree.column("#3", width=100, stretch=False, anchor=CENTER)
        self.ObtenerProducto()
        ventana_buscar.mainloop()

    def BuscarProducto(self, *args, **kwargs):

        self.obtener_id = self.campo_id.get()
        consulta = "SELECT * FROM Productos WHERE id=?"
        result = self.EjecutarConsulta(consulta, (self.obtener_id, ))
        self.r = result.fetchone()
        # If para revisar si el ID ingresado existe en la base de datos , de lo contrario larga error
        if self.r is not None:
            self.get_id = self.r[0]
            self.obtener_nombre = self.r[1]
            self.obtener_precio = self.r[3]
            self.obtener_stock = self.r[2]
            self.nombre_producto.configure(
                text="Nombre: " + str(self.obtener_nombre))
            self.precio_producto.configure(
                text="Precio: $" + str(self.obtener_precio))
        else:
            messagebox.showerror(
                "Error", "Este producto no existe en la base de datos.", parent = self.ventana_ventas)

    def AgregarVenta(self, *args, **kwargs):
        try:
            self.cantidad_valor = int(self.campo_cantidad.get())
            if (self.cantidad_valor > int(self.obtener_stock)):
                self.msj = messagebox.showinfo(
                    "Error", "La cantidad deseada supera el stock disponible.", parent = self.ventana_ventas)
            elif (self.cantidad_valor == 0):
                self.msj = messagebox.showinfo(
                    "Error", "Debes ingresar una cantidad.", parent = self.ventana_ventas)
            else:
                self.d_porc = (((float(self.cantidad_valor) * float(self.obtener_precio))
                                * float(self.campo_descuento.get())) / 100)               
                self.precio_final = ((float(self.cantidad_valor) * float(
                    self.obtener_precio)) - float(self.d_porc))

                lista_producto.append(self.obtener_nombre)
                precio_product.append(self.precio_final)
                cantidad_producto.append(self.cantidad_valor)
                id_producto.append(self.obtener_id)
                precio_Unitario.append(self.obtener_precio)
                descuentos.append(self.d_porc)
                
                self.contador = 0
                
                # Limpiando tabla
                records = self.tabla.get_children()
                for element in records:
                    self.tabla.delete(element)
                
            for self.p in lista_producto:

                self.tabla.insert('', 10, text=(str(id_producto[self.contador])), values=(str(lista_producto[self.contador]), str(
                    cantidad_producto[self.contador]), str(precio_Unitario[self.contador]), str(precio_product[self.contador])))
                descuentos[self.contador]
                self.contador += 1

                # configuracion total
                self.Total.configure(
                    text="Total: $" + str(sum(precio_product)))

                self.labelDescuento.configure(
                    text= "Descuento: $"+ str(sum(descuentos))
                )

                #Limpar
                self.campo_id.delete(0,END)
                self.campo_id.focus()
                self.campo_cantidad.delete(0,END)
                self.campo_descuento.delete(0,END)
                self.nombre_producto.configure(text = "Nombre: ")
                self.precio_producto.configure(text = "Precio: ")
        except:
            messagebox.showerror("Error", "Revisa los datos ingresados", parent = self.ventana_ventas)

    def PagaCon(self):
        self.cantidad_dada = float(self.campo_pagacon.get())
        self.nuestro_total= float(sum(precio_product))
        self.calculo = self.cantidad_dada - self.nuestro_total
        self.vuelto.configure(text = "")
        self.vuelto= Label(self.frame3, text="Su vuelto es: $ " + str(self.calculo), font=(
            "Arial", 17, "bold"), bg="#83D6A8")
        self.vuelto.place(x=1, y=60)

    def LimpiarVuelto(self):
        self.campo_pagacon.delete(0,END)
        self.vuelto.configure(text = "")
        self.vuelto= Label(self.frame3, text="Su vuelto es: ", font=(
            "Arial", 17, "bold"), bg="#83D6A8")
        self.vuelto.place(x=1, y=60)

    def BorrarVenta(self):
        #Funcion para limpiar la venta por algun error de tipeo o algo por el estilo.
        #Limpiando tabla
        records = self.tabla.get_children()
        for element in records:
            self.tabla.delete(element)

        del(lista_producto[:])
        del(id_producto[:])
        del(cantidad_producto[:])
        del(precio_product[:])
        del(descuentos[:])

        # configuracion total
        self.Total.configure(
            text="Total: " )

        self.labelDescuento.configure(
            text= "Descuento:")

    def ConfirmarVenta(self):
        try:
            # Crear factura de venta unica
            self.cont= 0
            for i in lista_producto:
                #actualizando stock
                sql = "UPDATE Productos SET stock=stock-? WHERE id=?"
                self.EjecutarConsulta(sql, (cantidad_producto[self.cont], id_producto[self.cont]))
                
                # insertar en BD transaccion
                sql2 = "INSERT INTO Ventas (descripcion, cantidad, precio, date) VALUES (?,?,?,?)"
                self.EjecutarConsulta(sql2, (lista_producto[self.cont], cantidad_producto[self.cont], precio_product[self.cont], date.strftime('%d/%m/%Y  %H:%M:%S')))
                self.cont +=1

                #Limpiando tabla
                records = self.tabla.get_children()
            for element in records:
                self.tabla.delete(element)  
                        
                del(lista_producto[:])
                del(id_producto[:])
                del(cantidad_producto[:])
                del(precio_product[:])  
                del(descuentos[:])

                #Limpar
                self.campo_id.delete(0,END)
                self.campo_id.focus()
                self.campo_cantidad.delete(0,END)
                self.campo_descuento.delete(0,END)
                self.nombre_producto.configure(text = "Nombre: ")
                self.precio_producto.configure(text = "Precio: ")
                self.campo_pagacon.delete(0,END)
                self.vuelto.configure(text = "")
                self.vuelto= Label(self.frame3, text="Su vuelto es: ", font=(
                    "Arial", 17, "bold"), bg="#83D6A8")
                self.vuelto.place(x=1, y=60)
                self.Total.configure(
                    text="Total: " )
                self.labelDescuento.configure(
                    text= "Descuento:")
                messagebox.showinfo("Perfecto", "Venta realizada con exito", parent = self.ventana_ventas) 
        except:
            messagebox.showinfo("Ciudado", "No hay ninguna venta", parent = self.ventana_ventas)  
       
    def generar_factura(self):
            # Ruta
        ruta = "C:/Users/Usuario/Desktop/GrupoD-Proyecto/Facturas/" + str(date2)
        if not os.path.exists(ruta):
            os.makedirs(ruta)

        # Plantilla
        empresa = "\t\t\t\tMinimarket de Amigos S.A\n"
        direccion = "\t\t\t\tMendoza, Argentina\n"
        contacto = "\t\t\t\tContacto: 2614705854\n\n"
        factura= "\t\t\t\t\tFactura\n\n"
        dt="\t\t\t\t\t" + str(date2) + "\n"

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
        messagebox.showinfo("Excelente", "Factura Generada Con Exito!", parent = self.ventana_ventas)