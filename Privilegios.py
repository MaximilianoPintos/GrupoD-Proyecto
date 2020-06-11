from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import sqlite3
import datetime
#avance 1---
 
class privilegios:

    db_nombre = 'ProyectoMI.py/BaseDeDatos.db'  # Llamado a la base de datos

    def __init__(self):
        vent_privilegios = Tk()
        vent_privilegios.title("Privilegios")
        vent_privilegios.resizable(0,0)
        vent_privilegios.config(bg="#83D6A8")

        # Centrado de ventana en pantalla
        ox, oy = vent_privilegios.winfo_screenwidth(
        )/2, vent_privilegios.winfo_screenheight()/2
        vent_privilegios.geometry("=450x300+%d+%d" % (ox-550, oy-300))
        
        frame1= LabelFrame(vent_privilegios, text="PERSONAL", font=("arial 18 bold"),bg="#83D6A8")
        frame1.grid(row=0,column=0, padx=30)

        tabla = ttk.Treeview(frame1, height=4, columns=('#1', '#2'),selectmode="browse")
        tabla.grid(row=0,column=0)
        
        tabla.heading("#0", text="NOMBRE", anchor=CENTER )
        tabla.heading("#1", text="APELLIDO", anchor=CENTER)
        tabla.heading("#2", text="RANGO", anchor=CENTER)

        tabla.column("#0", width = 130 , stretch=NO, anchor=CENTER)
        tabla.column("#1", width = 130 , stretch=NO, anchor=CENTER)
        tabla.column("#2", width = 130 , stretch=NO, anchor=CENTER)
        
        Label(vent_privilegios, text="Actualizar Permiso", bg="#83D6A8",font=("arial 18 bold")).place(x=120,y=150)
        
        checkbox_value = BooleanVar(vent_privilegios)
        checkbox = Radiobutton(vent_privilegios,text="EMPLEADO / ", value=1, bg="#83D6A8", font = ("arial 10 bold") ,variable=checkbox_value)
        checkbox.place(x=100, y=183)

        checkbox2 = Radiobutton(vent_privilegios,text="ADMINISTRADOR", value=2, bg="#83D6A8" , font=("arial 10 bold") ,variable=checkbox_value)
        checkbox2.place(x=210, y=183)

        boton_act = Button(vent_privilegios, text="Actualizar", width=30,font=("arial 12 bold"))
        boton_act.config(bd=2,relief="solid")
        boton_act.place(x=80, y=220)

        vent_privilegios.mainloop()