import tkinter as tk
from tkinter import messagebox
from cocomoBasico import CocomoBasicoApp
from cocomoIntermedio import COCOMOIntermedioApp

def mostrar_cocomo_basico():
    new_window = tk.Toplevel(root)
    app = CocomoBasicoApp(new_window)
    
def mostrar_cocomo_intermedio():
    new_window = tk.Toplevel(root)
    app = COCOMOIntermedioApp(new_window)

def salir():
    root.quit()

# Crear la ventana principal
root = tk.Tk()
root.title("Modelo COCOMO")
root.geometry("1000x500")
root.configure(bg="#9ccc65")  # Cambiar el color de fondo

# Crear el mensaje de bienvenida
welcome_label = tk.Label(root, text="Bienvenidos al software de aplicación de modelos",
                         font=("Helvetica", 16), bg="#9ccc65")
welcome_label.pack(pady=20)

# Crear un frame para los botones
button_frame = tk.Frame(root, bg="#9ccc65")
button_frame.pack(pady=20)

# Crear el botón para COCOMO BÁSICO
btn_basico = tk.Button(button_frame, text="COCOMO BÁSICO", command=mostrar_cocomo_basico,
                       font=("Helvetica", 12), bg="#c5e1a5", fg="black", padx=20, pady=10)
btn_basico.grid(row=0, column=0, padx=10)

# Crear el botón para COCOMO INTERMEDIO
btn_intermedio = tk.Button(button_frame, text="COCOMO INTERMEDIO", command=mostrar_cocomo_intermedio,
                           font=("Helvetica", 12), bg="#c5e1a5", fg="black", padx=20, pady=10)
btn_intermedio.grid(row=0, column=1, padx=10)

# Crear el botón de salida
btn_salir = tk.Button(button_frame, text="Salir", command=salir,
                      font=("Helvetica", 12), bg="#ff8a80", fg="black", padx=20, pady=10)
btn_salir.grid(row=1, columnspan=2, pady=20)

# Iniciar el bucle principal de la interfaz
root.mainloop()
