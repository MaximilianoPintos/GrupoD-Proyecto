import sqlite3
import datetime
from tkinter import *
from tkinter import filedialog, messagebox, ttk


class Proveedores:

    db_name = 'BaseDatos.db' 

    def Inicio(self):
        # Ventana principal                                                
        ventana = Tk()
        self.icono = "@../GrupoD-Proyecto/Iconos/Registradora.xbm"
        ventana.iconbitmap(self.icono)
        ventana.resizable(0,0)
        ventana.config(bg = "#83D6A8")
        ox, oy = ventana.winfo_screenwidth()/2, ventana.winfo_screenwidth()/2
        ventana.geometry("=1300x244+%d+%d" % (ox-650, oy-450))
        self.titulo = "Proveedores"
        ventana.title(self.titulo)

        # Creacion de frame contenedor
        frame = LabelFrame(ventana, text = 'Carga proveedor: ')
        frame.config(bg = "#83D6A8", pady = 12)
        frame.grid(row = 0, column = 0, columnspan = 3, sticky = W + E)

        frame_tabla = LabelFrame(ventana, text = 'Proveedores: ')
        frame_tabla.config(bg = "#83D6A8")
        frame_tabla.grid(row = 0, column = 10, columnspan = 3, sticky = W + E)
        self.mensaje2 = Label(frame_tabla, text = '', font = ("arial 14"), bg = "#83D6A8")
        self.mensaje2.grid(row = 0, column = 0)

        val_num = (frame.register(self.lee_numero), '%S')
        val_str = (frame.register(self.lee_str), '%S')

        # Entrada Empresa
        Label(frame, text = 'Empresa: ', font = ("arial 14"), bg = "#83D6A8").grid(row = 1, column = 0)
        self.empresa = Entry(frame, validate = 'key', validatecommand = val_str)
        self.empresa.focus()
        self.empresa.grid(row = 1, column = 1)

        # Entrada CUIT Empresa
        Label(frame, text = 'CUIT Empresa: ', font = ("arial 14"), bg = "#83D6A8").grid(row = 2, column = 0)
        self.cuit_empresa = Entry(frame, validate = 'key', validatecommand = val_num)
        self.cuit_empresa.focus()
        self.cuit_empresa.grid(row = 2, column = 1)


        # Entrada Nombre-Contacto
        Label(frame, text = 'Nombre: ', font = ("arial 14"), bg = "#83D6A8").grid(row = 3, column = 0)
        self.nombre = Entry(frame, validate = 'key', validatecommand = val_str)
        self.nombre.focus()
        self.nombre.grid(row = 3, column = 1)

        # Entrada DNI
        Label(frame, text = 'DNI: ', font = ("arial 14"), bg = "#83D6A8").grid(row = 4, column = 0)
        self.dni = Entry(frame, validate = 'key', validatecommand = val_num)
        self.dni.focus()
        self.dni.grid(row = 4, column = 1)

        # Entrada Celular
        Label(frame, text = 'Celular: ', font = ("arial 14"), bg = "#83D6A8").grid(row = 5, column = 0)
        self.celular = Entry(frame, validate = 'key', validatecommand = val_num)
        self.celular.focus()
        self.celular.grid(row = 5, column = 1)

        # Entrada Correo
        Label(frame, text = 'Correo: ', font = ("arial 14"), bg = "#83D6A8").grid(row = 6, column = 0)
        self.correo = Entry(frame)
        self.correo.focus()
        self.correo.grid(row = 6, column = 1)

        # Entrada Fecha
        self.fecha = datetime.datetime.now().date()

        # Tabla
        self.tabla = ttk.Treeview(frame_tabla, height = 7, columns = ('#1','#2','#3','#4','#5', '#6'))
        self.tabla.grid(row = 0, column = 0, columnspan = 2, sticky= W)
        self.tabla.heading('#0', text = 'Fecha', anchor = CENTER)
        self.tabla.heading('#1', text = 'Empresa', anchor = CENTER)
        self.tabla.heading('#2', text = 'CUIT Empresa', anchor = CENTER)
        self.tabla.heading('#3', text = 'Nombre', anchor = CENTER)
        self.tabla.heading('#4', text = 'DNI', anchor = CENTER)
        self.tabla.heading('#5', text = 'Celular', anchor = CENTER)
        self.tabla.heading('#6', text = 'Correo', anchor = CENTER)

        self.tabla.column('#0', width = 100, stretch = False, anchor = CENTER)
        self.tabla.column('#1', width = 175, stretch = False, anchor = CENTER)
        self.tabla.column('#2', width = 115, stretch = False, anchor = CENTER)
        self.tabla.column('#3', width = 175, stretch = False, anchor = CENTER)
        self.tabla.column('#4', width = 75, stretch = False, anchor = CENTER)
        self.tabla.column('#5', width = 100, stretch = False, anchor = CENTER)
        self.tabla.column('#6', width = 215, stretch = False, anchor = CENTER)

        # Botones
        ttk.Button(frame, text = 'GUARDAR', command = self.cargar_datos).grid(row = 12, column = 1, sticky = W + E)
        boton_editar = ttk.Button(frame_tabla, text = 'EDITAR', command = self.editar)
        boton_editar.config(width = 58)
        boton_editar.grid(row = 10, column = 0)
        boton_borrar = ttk.Button(frame_tabla, text = 'BORRAR', command = self.borrar)
        boton_borrar.config(width = 58)
        boton_borrar.grid(row = 10, column = 1)

        self.obtener_dato()
        ventana.mainloop()

    # 'chekeo' de la tabla    
    def ejecuta_consulta(self, consulta, parametros = ()):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()    
            resultado = cursor.execute(consulta, parametros)
            conn.commit()
            return resultado
        raise Exception(' NO SE PUDO CONECTAR A LA BASE DE DATOS. ')

    # Limpia tabla
    def obtener_dato(self):
        graba = self.tabla.get_children()
        for elemento in graba:
            self.tabla.delete(elemento)
        consulta = 'SELECT * FROM Proveedores'
        filas_bd = self.ejecuta_consulta(consulta)
        for row in filas_bd:
            self.tabla.insert('', 0, text = row[1], values = (row[2], row[3], row[4], row[5], row[6], row[7]))

    # Validacion general (todos los campos estan llenos)
    def validacion(self):
        if (len(self.empresa.get()) != 0 and len(self.cuit_empresa.get()) != 0 and len(self.nombre.get()) != 0 and len(self.dni.get()) != 0 and len(self.celular.get()) != 0 and len(self.correo.get()) != 0):
            return TRUE
        else:
            return FALSE

    # Validacion Numeros
    @staticmethod
    def lee_numero(aux_0):
        return aux_0.isdigit()
        
    # Validacion Str
    @staticmethod
    def lee_str(aux_1):
        if aux_1.isalpha() or aux_1.isspace():
            return True
        else:
            return False

    # Funcion para cargar
    def cargar_datos(self):
        if self.validacion() == TRUE:
            consult = 'INSERT INTO Proveedores VALUES(NULL, ?, ?, ?, ?, ?, ?, ?)'
            parametros = (self.fecha, self.empresa.get(), self.cuit_empresa.get(), self.nombre.get(), self.dni.get(), self.celular.get(), self.correo.get())
            self.ejecuta_consulta(consult, parametros)
            self.obtener_dato()
            self.empresa.delete(0, END)
            self.cuit_empresa.delete(0, END)
            self.nombre.delete(0, END)
            self.dni.delete(0, END)
            self.celular.delete(0, END)
            self.correo.delete(0, END)

    # Funcion para borrar

    def borrar (self):
        
        if self.tabla.item(self.tabla.selection())['text'] == '':
            self.mensaje2['text'] = 'Por favor, seleccione un elemento'
            return
        empresa = self.tabla.item(self.tabla.selection())['values'][0]
        consulta = 'DELETE FROM Proveedores WHERE empresa = ?'
        self.ejecuta_consulta(consulta, (empresa, ))
        self.mensaje2['text'] = 'Se a eliminado a {} de tu lista de proveedores. '.format(empresa)
        self.obtener_dato()
    
    # Funcion para editar

    def editar (self):

        # Funcion editar valores
        self.mensaje2["text"] = ''
        if self.tabla.item(self.tabla.selection())["text"] == "":
            self.mensaje2["text"] = "Por favor, seleccione un elemento"
            return

        # tabla editar valores
        empresa = self.tabla.item(self.tabla.selection())["values"][0]
        cuit_empresa = self.tabla.item(self.tabla.selection())["values"][1]
        nombre = self.tabla.item(self.tabla.selection())["values"][2]
        dni = self.tabla.item(self.tabla.selection())["values"][3]
        celular = self.tabla.item(self.tabla.selection())["values"][4]
        correo = self.tabla.item(self.tabla.selection())["values"][5]

        self.ventana_de_edicion = Toplevel()
        self.ventana_de_edicion.title = ("Editar")
        self.ventana_de_edicion.config(background="#83D6A8")
        self.ventana_de_edicion.resizable(0, 0)
        self.ventana_de_edicion.config(bd=5)
        self.ventana_de_edicion.config(relief= "solid")

        #Frame Ventana Edicion
        frame69 = LabelFrame(self.ventana_de_edicion, text = '')
        frame69.config(bg = "#83D6A8")
        frame69.grid(row = 0, column = 0)

        val_num = (frame69.register(self.lee_numero), '%S')
        val_str = (frame69.register(self.lee_str), '%S')
    
        # Antiguo nombre empresa
        Label(frame69, text = 'Antigua empresa: ', font = ("arial 14"), bg = "#83D6A8").grid(row = 0, column = 1)
        Entry(frame69, textvariable = StringVar(self.ventana_de_edicion, value = empresa), state = 'readonly').grid(row = 0, column = 2)

        # Nuevo nombre empresa 
        Label(frame69, text = 'Nueva empresa: ', font = ("arial 14"), bg = "#83D6A8").grid(row = 0, column = 3)
        nuevo_nombre_empresa = Entry(frame69, validate = 'key', validatecommand = val_str)
        nuevo_nombre_empresa.grid(row = 0, column = 4)

        # Antiguo Cuit Empresa
        Label(frame69, text = 'Antiguo CUIT: ', font = ("arial 14"), bg = "#83D6A8").grid(row = 1, column = 1)
        Entry(frame69, textvariable = StringVar(self.ventana_de_edicion, value = cuit_empresa), state = 'readonly').grid(row = 1, column = 2)

        # Nuevo CUIT Empresa
        Label(frame69, text = 'Nuevo CUIT: ', font = ("arial 14"), bg = "#83D6A8").grid(row = 1, column = 3)
        nuevo_cuit_empresa = Entry(frame69, validate = 'key', validatecommand = val_num)
        nuevo_cuit_empresa.grid(row = 1, column = 4)

        # Antiguo nombre
        Label(frame69, text = 'Antiguo nombre: ', font = ("arial 14"), bg = "#83D6A8").grid(row = 2, column = 1)
        Entry(frame69, textvariable = StringVar(self.ventana_de_edicion, value = nombre), state = 'readonly').grid(row = 2, column = 2)

        # Nuevo Nombre
        Label(frame69, text = 'Nuevo nombre: ', font = ("arial 14"), bg = "#83D6A8").grid(row = 2, column = 3)
        nuevo_nombre = Entry(frame69, validate = 'key', validatecommand = val_str)
        nuevo_nombre.grid(row = 2, column = 4) 

        # Antiguo DNI
        Label(frame69, text = 'Antiguo DNI: ', font = ("arial 14"), bg = "#83D6A8").grid(row = 3, column = 1)
        Entry(frame69, textvariable = StringVar(self.ventana_de_edicion, value = dni), state = 'readonly').grid(row = 3, column = 2)

        # Nuevo DNI
        Label(frame69, text = 'Nuevo DNI: ', font = ("arial 14"), bg = "#83D6A8").grid(row = 3, column = 3)
        nuevo_dni = Entry(frame69, validate = 'key', validatecommand = val_num)
        nuevo_dni.grid(row = 3, column = 4)

        # Antiguo celular
        Label(frame69, text = 'Antiguo numero: ', font = ("arial 14"), bg = "#83D6A8").grid(row = 4, column = 1)
        Entry(frame69, textvariable = StringVar(self.ventana_de_edicion, value = celular), state = 'readonly').grid(row = 4, column = 2)

        # Nuevo celular
        Label(frame69, text = 'Nuevo celular', font = ("arial 14"), bg = "#83D6A8").grid(row = 4, column = 3)
        nuevo_celular = Entry(frame69, validate = 'key', validatecommand = val_num)
        nuevo_celular.grid(row = 4, column = 4)

        # Antiguo correo
        Label(frame69, text = 'Antiguo correo: ', font = ("arial 14"), bg = "#83D6A8").grid(row = 5, column = 1)
        Entry(frame69, textvariable = StringVar(self.ventana_de_edicion, value = correo), state = 'readonly').grid(row = 5, column = 2)

        # Nuevo correo
        Label(frame69, text = 'Nuevo correo', font = ("arial 14"), bg = "#83D6A8").grid(row = 5, column = 3)
        nuevo_correo = Entry(frame69)
        nuevo_correo.grid(row = 5, column = 4)

        ttk.Button(self.ventana_de_edicion, text = 'Guardar cambios', command = lambda: self.editar_valores(nuevo_nombre_empresa.get(),nuevo_cuit_empresa.get(), nuevo_nombre.get(), nuevo_dni.get(), nuevo_celular.get(), nuevo_correo.get(), empresa)).grid(row = 8, column = 0, sticky = W + E)
        self.ventana_de_edicion.mainloop()
        
    # Funcion para editar productos (dentro del boton, parte 2)
    def editar_valores(self, nuevo_nombre_empresa, nuevo_cuit_empresa, nuevo_nombre, nuevo_dni, nuevo_celular, nuevo_correo, empresa):
        consulta = 'UPDATE proveedores SET empresa = ?, Cuit_Empresa = ?, nombre = ?, dni = ?, celular = ?, correo = ? WHERE empresa = ?'
        parametros = (nuevo_nombre_empresa, nuevo_cuit_empresa, nuevo_nombre, nuevo_dni, nuevo_celular, nuevo_correo, empresa)
        self.ejecuta_consulta(consulta, parametros)
        self.ventana_de_edicion.destroy()
        self.obtener_dato()
