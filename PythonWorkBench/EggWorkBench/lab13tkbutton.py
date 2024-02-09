import tkinter as tk 
from tkinter import ttk, messagebox


def ingresar():
    lista_nombres.insert(tk.END, caja_nombre.get())
    saludo.config(text="Hola, " + caja_nombre.get() + "!")
    caja_nombre.delete(0, tk.END)

def borrar():
    lista_nombres.delete(tk.END)

def salir():
    if messagebox.askyesno(title="Salir", message="¿Desea salir?"):
        ventana_principal.destroy()

ventana_principal = tk.Tk()
ventana_principal.title("Ventana principal")
ventana_principal.config(height=255, width=510)

caja_nombre = ttk.Entry()
caja_nombre.place(x=20, y=10, width=380)

boton_ingresar = ttk.Button(text="Ingresar", command=ingresar)
boton_ingresar.place(x=410, y=10)

boton_borrar = ttk.Button(text="Borrar", command=borrar)
boton_borrar.place(x=410, y=35)

boton_salir = ttk.Button(text="Salir", command=salir)
boton_salir.place(x=410, y=225)

lista_nombres = tk.Listbox()
lista_nombres.place(x=20, y=60, width=470)

saludo = ttk.Label()
saludo.place(x=20, y=35)

ventana_principal.mainloop()