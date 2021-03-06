from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import sqlite3
import datetime


class Productos:
    db_nombre = 'BaseDatos.db'  # Llamado a la base de datos
    # --------------------------------------------------------------------------------------------------------------------------------------------
    def Inicio(self):
        ventana_stock = Tk()
        ventana_stock.config(bg="#83D6A8")
        ventana_stock.resizable(0, 0)
        ventana_stock.title("Control de Stock")
        self.icono = "@../GrupoD-Proyecto/Iconos/Registradora.xbm"
        ventana_stock.iconbitmap(self.icono)

        # ------------ Centrado de Ventana en pantalla ------------
        ox, oy = ventana_stock.winfo_screenwidth(
        )/2, ventana_stock.winfo_screenheight()/2
        ventana_stock.geometry("=1260x580+%d+%d" % (ox-600, oy-300))
        # ---------------------------------------------------------
                    
        # ---------------- Frame Cargar Productos ----------------------------------------------------------------------

        frame1 = LabelFrame(ventana_stock, text="Cargar Productos.",font=("arial 10 bold"), bg="#83D6A8")
        frame1.grid(row=0, column=0, columnspan=3, pady=20,padx=50)
        vcmd = (frame1.register(self.on_entry_validate), '%P') # Comando de validacion de entry

        # ID PRODUCTO  - frame1
        Label(frame1, text="ID Producto: ", font=("arial 10 bold"), bg="#83D6A8").grid(row=0, column=0,sticky=W+E, pady=2)
        self.id_prod = Label(frame1, text= "Autoasignado",width=20, justify = CENTER, font=("arial 15"))
        self.id_prod.config(bd=3, relief = "solid")
        self.id_prod.grid(row=1,column=0,pady=10,padx=10)
        

        # Input Descripcion - frame1
        Label(frame1, text="Descripcion: ",font=("arial 10 bold"), bg="#83D6A8").grid(row=2, column=0,sticky=W+E, pady=2)
        self.descripcion = Entry(frame1,width=20, justify=CENTER,font=("arial 15"))
        self.descripcion.focus()
        self.descripcion.config(bd=3, relief = "solid")
        self.descripcion.grid(row=3, column=0,pady=10)

        # Input Stock - frame1
        Label(frame1, text="Stock Producto: ", font=("arial 10 bold"), bg="#83D6A8").grid(row=4, column=0,sticky=W+E, pady=2)
        self.stock = Entry(frame1, validate="key", validatecommand=vcmd, width=20, justify = CENTER, font=("arial 15"))
        self.stock.config(bd=3, relief = "solid")
        self.stock.grid(row=5,column=0,pady=10)

        # Input Precio Costo - frame1 
        Label(frame1, text="Precio Costo: ", font=("arial 10 bold"), bg="#83D6A8").grid(row=6,column=0,sticky=W+E, pady=2)
        self.precio_costo = Entry(frame1, validate="key", validatecommand=vcmd, width=20, justify = CENTER, font=("arial 15"))
        self.precio_costo.config(bd=3, relief = "solid")
        self.precio_costo.grid(row=7,column=0, pady=10)

        # Input Precio Venta - frame1 
        Label(frame1, text="Precio Venta: ", font=("arial 10 bold"), bg="#83D6A8").grid(row=8,column=0,sticky=W+E, pady=2)
        self.precio_venta = Entry(frame1, validate="key", validatecommand=vcmd, width=20, justify = CENTER, font=("arial 15"))
        self.precio_venta.config(bd=3, relief = "solid")
        self.precio_venta.grid(row=9,column=0, pady=10)

                # Input Precio Venta - frame1 
        Label(frame1, text="Categoria: ", font=("arial 10 bold"), bg="#83D6A8").grid(row=10,column=0,sticky=W+E, pady=2)
        self.combo = ttk.Combobox(frame1, state="readonly", width=18, font=("arial 15"), justify=CENTER)
        self.combo["values"] = ["Bebidas", "Bebidas Alcoholicas", "Golosinas", "Comestibles", "Cigarrillos", "Otros"]
        self.combo.grid(row = 11, column = 0, pady=2)

        # Boton Carga Producto
        self.btn_cargar = Button(frame1, text="Cargar Producto", cursor="hand2",font=("arial 10 bold"),bg="silver", command= self.insertar_producto)
        self.btn_cargar.grid(row=12, columnspan=2, pady=15)
        self.btn_cargar.config(bd=5,relief="raised")

        # ------------------------------------------------------------------------------------------------------------------

        # -------------------- Frame Cargar Productos ----------------------------------------------------------------------

        frame2 = LabelFrame(ventana_stock,text="Tabla de Productos",font=("arial 10 bold"), bg="#83D6A8")
        frame2.grid(row=0, column=4, columnspan=3, pady=10)

        # Mensaje error al cargar
        self.mensaje = Label(frame2, text="", fg="red",font=("arial 10 bold"), bg="white")
        self.mensaje.config(bd=2, relief = "solid")
        self.mensaje.grid(row=0, column=4, columnspan=3, sticky=W + E)

        # Tabla
        self.tablax = ttk.Treeview(frame2, height=20, columns=('#1', '#2', '#3', '#4', '#5'),selectmode = "browse")
        self.tablax.grid(row=1, column=4, columnspan=3, pady=5)

        self.tablax.heading("#0", text="ID", anchor=CENTER )
        self.tablax.heading("#1", text="DESCRIPCION", anchor=CENTER)
        self.tablax.heading("#2", text="STOCK", anchor=CENTER)
        self.tablax.heading("#3", text="PRECIO COSTO", anchor=CENTER)
        self.tablax.heading("#4", text="PRECIO VENTA", anchor=CENTER)    
        self.tablax.heading("#5", text="CATEGORIA", anchor=CENTER)    

        self.tablax.column("#0", width = 50 , stretch=False, anchor=CENTER)
        self.tablax.column("#1", width = 350, stretch=False, anchor=CENTER)
        self.tablax.column("#2", width = 100, stretch=False, anchor=CENTER)
        self.tablax.column("#3", width = 130, stretch=False, anchor=CENTER)
        self.tablax.column("#4", width = 130, stretch=False, anchor=CENTER)
        self.tablax.column("#5", width = 130, stretch=False, anchor=CENTER)

        # Boton Eliminar, Editar
        self.btn_eliminar = Button(frame2, text="ELIMINAR", cursor="hand2",bg="silver",font=("arial 10 bold"), command = self.eliminar_producto)
        self.btn_eliminar.grid(row=7, column=5, sticky=W+E)
        self.btn_eliminar.config(bd=5,relief="raised")

        self.btn_editar = Button(frame2, text="EDITAR", cursor="hand2",bg="silver",font=("arial 10 bold"), command= self.editar_producto)
        self.btn_editar.grid(row=7, column=6, sticky=W+E)
        self.btn_editar.config(bd=5,relief="raised")
        self.obtener_producto()
        # ------------------------------------------------------------------------------------------------------------------
        ventana_stock.mainloop()
    # --------------------------------------------------------------------------------------------------------------------------------------------
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
        records = self.tablax.get_children()
        for element in records:
            self.tablax.delete(element)
        # Consulta de datos
        consulta = 'SELECT * FROM Productos'
        filasBD = self.ejecuta_consulta(consulta)
        # relleno de datos
        for row in filasBD:
            self.tablax.insert('', 9999, text=row[0], values=(row[1], row[2], (f"$ {row[3]}"), (f"$ {row[4]}"), row[5]))  
    # --------------------------------------------------------------------------------------------------------------------------------------------
    # --------------------------- funcion cargar productos ---------------------------------------------------------------------------------------
    def insertar_producto(self):
        # Insertar Producto boton ventana agregar / quitar Producto
 
        if len(str(self.descripcion.get())) != 0 and len(str(self.stock.get())) != 0 and len(str(self.precio_costo.get())) != 0 and len(str(self.precio_venta.get())) != 0:
            consult = 'INSERT INTO Productos VALUES(NULL, ?, ?, ?, ?, ?)'
            parametros = (self.descripcion.get(), self.stock.get(), self.precio_costo.get(), self.precio_venta.get(), self.combo.get(), )
            self.ejecuta_consulta(consult, parametros)
            self.mensaje['text'] = 'Producto {} agregado correctamente'.format(self.descripcion.get())
            self.descripcion.delete(0, END)
            self.stock.delete(0, END)
            self.precio_costo.delete(0, END)
            self.precio_venta.delete(0, END)
            self.combo.set("")
        else:
            self.mensaje['text'] = 'Todos los campos son requeridos'
        self.obtener_producto()    
    # --------------------------------------------------------------------------------------------------------------------------------------------
    # --------------------------- funcion eliminar productos -------------------------------------------------------------------------------------    
    def eliminar_producto(self):

        # Eliminar producto de base de datos
        self.mensaje["text"] = ''
        if self.tablax.item(self.tablax.selection())["text"] == "":
            self.mensaje["text"] = "Por favor, seleccione un elemento"
            return

        nombre = self.tablax.item(self.tablax.selection())["values"][0]
        consulta = 'DELETE FROM Productos WHERE nombre = ?'
        self.ejecuta_consulta(consulta, (nombre,))
        self.mensaje["text"] = "El elemento {} fue eliminado correctamente".format(
            nombre)
        self.obtener_producto()        
    # --------------------------------------------------------------------------------------------------------------------------------------------    
    # --------------------------- Ventana Edicion de productos -----------------------------------------------------------------------------------
    def editar_producto(self):

        # Funcion editar producto de base de datos
        self.mensaje["text"] = ''
        if self.tablax.item(self.tablax.selection())["text"] == "":
            self.mensaje["text"] = "Por favor, seleccione un elemento"
            return
        # tabla editar producto
        id = self.tablax.item(self.tablax.selection())["text"]
        descripcion = self.tablax.item(self.tablax.selection())["values"][0]
        stock = self.tablax.item(self.tablax.selection())["values"][1]
        p_costo = self.tablax.item(self.tablax.selection())["values"][2]
        p_venta = self.tablax.item(self.tablax.selection())["values"][3]

        self.ventana_editar = Toplevel()
        self.ventana_editar.title = ("Editar Producto")
        self.ventana_editar.config(background="#83D6A8")
        self.ventana_editar.resizable(0, 0)
        self.ventana_editar.config(bd=5)
        self.ventana_editar.config(relief= "solid")

        #Centrar Ventana en pantalla
        ox,oy=self.ventana_editar.winfo_screenwidth()/2,self.ventana_editar.winfo_screenheight()/2
        self.ventana_editar.geometry("=700x550+%d+%d" % (ox-200,oy-280) )

        frame2 = LabelFrame(self.ventana_editar, text="Actualizar Productos.",font=("arial 10 bold"), bg="#83D6A8")
        frame2.grid(row=0, column=4, columnspan=3, padx=40,pady=20)
        vcmd = (frame2.register(self.on_entry_validate), '%P') # Comando de validacion de entry

        # ID anterior
        Label(frame2, text="ID Anterior: ",font=("arial 10 bold"), bg="#83D6A8").grid(row=0, column=0, sticky=W+E, pady=2)
        Entry(frame2, textvariable=StringVar(
            self.ventana_editar, value=id), width="20",state="readonly",font=("arial 15"), justify="center").grid(row=1, column=0,pady=10)

        # ID Nuevo
        Label(frame2, text="ID Nueva: ",font=("arial 10 bold"), bg="#83D6A8").grid(row=0, column=1,sticky=W+E, columnspan=2,pady=2)
        id_nueva = Entry(frame2, validate="key", validatecommand=vcmd,width="20",font=("arial 15"), justify="center")
        id_nueva.grid(row=1, column=1,columnspan=2,pady=10)

        # descripcion anterior
        Label(frame2, text="Descripcion Anterior: ",font=("arial 10 bold"), bg="#83D6A8").grid(row=2, column=0, sticky=W+E, pady=2)
        Entry(frame2, textvariable=StringVar(
            self.ventana_editar, value=descripcion) ,width="20",font=("arial 15"), state="readonly", justify="center").grid(row=3, column=0,pady=10)

        # descripcion Nuevo
        Label(frame2, text="Descripcion Nueva: ",font=("arial 10 bold"), bg="#83D6A8").grid(row=2, column=1,sticky=W+E, columnspan=2,pady=2)
        descripcion_nuevo = Entry(frame2, width="20",font=("arial 15"), justify="center")
        descripcion_nuevo.grid(row=3, column=1,columnspan=2,pady=10)

        # Stock anterior
        Label(frame2, text="Stock Anterior: ",font=("arial 10 bold"), bg="#83D6A8").grid(row=4, column=0, sticky=W+E,padx=80, pady=2)
        Entry(frame2, textvariable=StringVar(
            self.ventana_editar, value=stock), width="20",font=("arial 15"), state="readonly", justify="center").grid(row=5, column=0,pady=10)

        # Stock Nuevo
        Label(frame2, text="Stock Nuevo: ",font=("arial 10 bold"), bg="#83D6A8").grid(row=4, column=1,sticky=W+E,padx=80,pady=2)
        stock_nuevo = Entry(frame2, validate="key", validatecommand=vcmd, width="20",font=("arial 15"), justify="center")
        stock_nuevo.grid(row=5, column=1,pady=10)

        # Precio de Costo anterior
        Label(frame2, text="Precio Costo Anterior: ",font=("arial 10 bold"), bg="#83D6A8").grid(row=6, column=0, sticky=W+E,padx=80, pady=2)
        Entry(frame2, textvariable=StringVar(
            self.ventana_editar, value=p_costo),width="20",font=("arial 15"), state="readonly", justify="center").grid(row=7, column=0,pady=10)

        # Precio de Costo Nuevo
        Label(frame2, text="Costo Nuevo: ",font=("arial 10 bold"), bg="#83D6A8").grid(row=6, column=1,sticky=W+E,padx=100,pady=2)
        precio_costo = Entry(frame2, validate="key", validatecommand=vcmd, width="20",font=("arial 15"), justify="center")
        precio_costo.grid(row=7, column=1,pady=10)

        # Precio de venta anterior
        Label(frame2, text="Precio Venta Anterior: ",font=("arial 10 bold"), bg="#83D6A8").grid(row=8, column=0, sticky=W+E, pady=2)
        Entry(frame2, textvariable=StringVar(
            self.ventana_editar, value=p_venta) ,width="20",font=("arial 15"), state="readonly", justify="center").grid(row=9, column=0,pady=10)

        # Precio de Venta Nuevo
        Label(frame2, text="Precio Venta Nuevo: ",font=("arial 10 bold"), bg="#83D6A8").grid(row=8, column=1,sticky=W+E,pady=2)
        precio_venta = Entry(frame2, validate="key", validatecommand=vcmd, width="20",font=("arial 15"), justify="center")
        precio_venta.grid(row=9, column=1,pady=10)

        # Combo box 
        Label(frame2, text="Categoria: ", font=("arial 10 bold"), bg="#83D6A8").grid(row=10,column=1,sticky=W+E, pady=2)
        combo = ttk.Combobox(frame2, state="readonly", width=18, font=("arial 15"), justify=CENTER)
        combo["values"] = ["Bebidas", "Bebidas Alcoholicas", "Golosinas", "Comestibles", "Cigarrillos", "Otros"]
        combo.grid(row = 11,column= 1, pady=2)

        # Boton actualizar
        self.btn_actualizar = Button(frame2, text="Actualizar Producto", cursor="hand2",font=("arial 10 bold"),bg="silver",
        command=lambda: self.editando(id_nueva.get(), descripcion_nuevo.get(), stock_nuevo.get(), precio_costo.get(), precio_venta.get(),combo.get() ,id))
        self.btn_actualizar.grid(row=12, columnspan=2, sticky=W + E, pady=15)
        self.btn_actualizar.config(bd=5,relief="raised")
    # --------------------------------------------------------------------------------------------------------------------------------------------
    # --------------------------- Funcion de Actualizacion en base de datos ----------------------------------------------------------------------
    def editando(self, id_nueva, descripcion_nuevo, stock_nuevo, precio_costo,precio_venta,combo, id):

        self.mensaje["text"] = ''
        if self.tablax.item(self.tablax.selection())["text"] == "":
            self.mensaje["text"] = "Por favor, seleccione un elemento"
            return     
        descripcion1 = self.tablax.item(self.tablax.selection())["values"][0]
        consulta = "UPDATE Productos SET id = ?, Nombre = ? , Stock = ? ,Precio_costo = ?, Precio_venta = ?, Categoria = ?  WHERE id =?"
        parametros = (id_nueva, descripcion_nuevo,
                      stock_nuevo, precio_costo , precio_venta, combo, id)
        self.ejecuta_consulta(consulta, parametros)
        self.ventana_editar.destroy()
        self.mensaje["text"] = 'El elemento {} a sido actualizado con exito'.format(descripcion1)
        self.obtener_producto()
    # --------------------------------------------------------------------------------------------------------------------------------------------
    # ------------ Validaciones ------------
    @staticmethod
    def on_entry_validate(S):
        if not S:
            return True
        if "." in S and len(S.split(".")[-1]) > 2:
            return False
        try:
            float(S)
        except ValueError:
            return False
        return True        
    # ---------------------------------------------------------
