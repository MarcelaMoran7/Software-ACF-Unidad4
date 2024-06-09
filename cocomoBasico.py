import tkinter as tk
from tkinter import messagebox

class CocomoBasicoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("COCOMO BASICO")

        # Crear un marco principal para contener todo
        self.marco_principal = tk.Frame(root)
        self.marco_principal.pack(fill="both", expand=True)

        # Crear un marco para el texto centrado
        self.marco_texto_centrado = tk.Frame(self.marco_principal)
        self.marco_texto_centrado.pack(fill="both", expand=True)

        # Texto para introducir datos - Parte 1
        self.texto_introducir_1 = tk.Label(self.marco_texto_centrado, text="INGRESE LOS DATOS NECESARIOS PARA CALCULAR")
        self.texto_introducir_1.pack()

        # Separadores entre secciones
        self.linea_separadora_1 = tk.Frame(self.marco_principal, height=2, width=1000, bd=1, relief="sunken")
        self.linea_separadora_1.pack(fill="x", padx=10, pady=10)

        self.linea_separadora_2 = tk.Frame(self.marco_principal, height=2, width=1000, bd=1, relief="sunken")
        self.linea_separadora_2.pack(fill="x", padx=10, pady=10)

        # Crear un marco para la sección 1
        self.marco_seccion_1 = tk.Frame(self.marco_principal)
        self.marco_seccion_1.pack(side="left", padx=10, pady=10)

        # COCOMO Básico - Parte 1
        self.cocomo_basico_1 = tk.Label(self.marco_seccion_1, text="Modelo Orgánico")
        self.cocomo_basico_1.grid(row=2, columnspan=4)

        # Etiqueta para "Peso de Complejidad" - Parte 1
        self.etiqueta_complejidad_1 = tk.Label(self.marco_seccion_1, text="Pesos de Complejidad")
        self.etiqueta_complejidad_1.grid(row=7, column=3)

        # Crear etiquetas y campos de entrada - Parte 1
        self.campos_entrada_1 = [
            ("Salidas:", "PesoS", "entry_salidas", "entry_peso"),
            ("Entradas:", "PesoE", "entry_entradas", "entry_peso2"),
            ("Consultas:", "PesoC", "entry_consultas", "entry_peso3"),
            ("Archivos internos:", "PesoAI", "entry_archivo_interno", "entry_peso4"),
            ("Archivos externos:", "PesoAE", "entry_archivo_externo", "entry_peso5")
        ]

        for i, (label_text, peso_text, entry_name, peso_name) in enumerate(self.campos_entrada_1, start=8):
            label = tk.Label(self.marco_seccion_1, text=label_text)
            label.grid(row=i, column=0)
            entry = tk.Entry(self.marco_seccion_1)
            entry.grid(row=i, column=1)
            setattr(self, entry_name, entry)

            peso_label = tk.Label(self.marco_seccion_1, text=peso_text)
            peso_label.grid(row=i, column=2)
            peso_entry = tk.Entry(self.marco_seccion_1)
            peso_entry.grid(row=i, column=3)
            setattr(self, peso_name, peso_entry)

        # Crear el resto de los widgets - Parte 1
        self.etiqueta_lineas_codigo_1 = tk.Label(self.marco_seccion_1, text="Establecer las líneas de Código\n por cada punto de función")
        self.etiqueta_lineas_codigo_1.grid(row=13, columnspan=4)
        self.entry_lineas_codigo = tk.Entry(self.marco_seccion_1)
        self.entry_lineas_codigo.grid(row=14, columnspan=4)

        self.boton_calcular_1 = tk.Button(self.marco_seccion_1, text="Calcular", command=self.calcular_cocomo_1)
        self.boton_calcular_1.grid(row=15, columnspan=4)

        # Crear marco para mostrar los resultados - Parte 1
        self.marco_resultado_1 = tk.Frame(self.marco_seccion_1, borderwidth=1, relief="solid")
        self.marco_resultado_1.grid(row=16, columnspan=4, padx=5, pady=5)

        # Crear etiquetas para los resultados dentro del marco - Parte 1
        self.resultado_cocomo_1 = tk.Label(self.marco_resultado_1, text="", justify="left")
        self.resultado_cocomo_1.pack()

        # Crear un marco de sombra para separar los modelos
        self.marco_sombra_1_2 = tk.Frame(self.marco_principal, bg="gray", width=2, height=300)
        self.marco_sombra_1_2.pack(side="left", padx=10, pady=10)

        # Crear un marco para la sección 2
        self.marco_seccion_2 = tk.Frame(self.marco_principal)
        self.marco_seccion_2.pack(side="left", padx=10, pady=10)

        # COCOMO Básico - Parte 2
        self.cocomo_basico_2 = tk.Label(self.marco_seccion_2, text="Modelo SemiAcoplado")
        self.cocomo_basico_2.grid(row=2, columnspan=4)

        # Etiqueta para "Peso de Complejidad" - Parte 2
        self.etiqueta_complejidad_2 = tk.Label(self.marco_seccion_2, text="Pesos de Complejidad")
        self.etiqueta_complejidad_2.grid(row=7, column=3)

        # Crear etiquetas y campos de entrada - Parte 2
        self.campos_entrada_2 = [
            ("Salidas:", "PesoS", "entry_salidas_2", "entry_peso_2"),
            ("Entradas:", "PesoE", "entry_entradas_2", "entry_peso2_2"),
            ("Consultas:", "PesoC", "entry_consultas_2", "entry_peso3_2"),
            ("Archivos internos:", "PesoAI", "entry_archivo_interno_2", "entry_peso4_2"),
            ("Archivos externos:", "PesoAE", "entry_archivo_externo_2", "entry_peso5_2")
        ]

        for i, (label_text, peso_text, entry_name, peso_name) in enumerate(self.campos_entrada_2, start=8):
            label = tk.Label(self.marco_seccion_2, text=label_text)
            label.grid(row=i, column=0)
            entry = tk.Entry(self.marco_seccion_2)
            entry.grid(row=i, column=1)
            setattr(self, entry_name, entry)

            peso_label = tk.Label(self.marco_seccion_2, text=peso_text)
            peso_label.grid(row=i, column=2)
            peso_entry = tk.Entry(self.marco_seccion_2)
            peso_entry.grid(row=i, column=3)
            setattr(self, peso_name, peso_entry)

        # Crear el resto de los widgets - Parte 2
        self.etiqueta_lineas_codigo_2 = tk.Label(self.marco_seccion_2, text="Establecer las líneas de Código\n por cada punto de función")
        self.etiqueta_lineas_codigo_2.grid(row=13, columnspan=4)
        self.entry_lineas_codigo_2 = tk.Entry(self.marco_seccion_2)
        self.entry_lineas_codigo_2.grid(row=14, columnspan=4)

        self.boton_calcular_2 = tk.Button(self.marco_seccion_2, text="Calcular", command=self.calcular_cocomo_2)
        self.boton_calcular_2.grid(row=15, columnspan=4)

        # Crear marco para mostrar los resultados - Parte 2
        self.marco_resultado_2 = tk.Frame(self.marco_seccion_2, borderwidth=1, relief="solid")
        self.marco_resultado_2.grid(row=16, columnspan=4, padx=5, pady=5)

        # Crear etiquetas para los resultados dentro del marco - Parte 2
        self.resultado_cocomo_2 = tk.Label(self.marco_resultado_2, text="", justify="left")
        self.resultado_cocomo_2.pack()

        # Crear un marco de sombra para separar los modelos
        self.marco_sombra_2_3 = tk.Frame(self.marco_principal, bg="gray", width=2, height=300)
        self.marco_sombra_2_3.pack(side="left", padx=10, pady=10)

        # Crear un marco para la sección 3
        self.marco_seccion_3 = tk.Frame(self.marco_principal)
        self.marco_seccion_3.pack(side="left", padx=10, pady=10)

        # COCOMO Básico - Parte 3
        self.cocomo_basico_3 = tk.Label(self.marco_seccion_3, text="Modelo Empotrado")
        self.cocomo_basico_3.grid(row=2, columnspan=4)

        # Etiqueta para "Peso de Complejidad" - Parte 3
        self.etiqueta_complejidad_3 = tk.Label(self.marco_seccion_3, text="Pesos de Complejidad")
        self.etiqueta_complejidad_3.grid(row=7, column=3)

        # Crear etiquetas y campos de entrada - Parte 3
        self.campos_entrada_3 = [
            ("Salidas:", "PesoS", "entry_salidas_3", "entry_peso_3"),
            ("Entradas:", "PesoE", "entry_entradas_3", "entry_peso2_3"),
            ("Consultas:", "PesoC", "entry_consultas_3", "entry_peso3_3"),
            ("Archivos internos:", "PesoAI", "entry_archivo_interno_3", "entry_peso4_3"),
            ("Archivos externos:", "PesoAE", "entry_archivo_externo_3", "entry_peso5_3")
        ]

        for i, (label_text, peso_text, entry_name, peso_name) in enumerate(self.campos_entrada_3, start=8):
            label = tk.Label(self.marco_seccion_3, text=label_text)
            label.grid(row=i, column=0)
            entry = tk.Entry(self.marco_seccion_3)
            entry.grid(row=i, column=1)
            setattr(self, entry_name, entry)

            peso_label = tk.Label(self.marco_seccion_3, text=peso_text)
            peso_label.grid(row=i, column=2)
            peso_entry = tk.Entry(self.marco_seccion_3)
            peso_entry.grid(row=i, column=3)
            setattr(self, peso_name, peso_entry)

        # Crear el resto de los widgets - Parte 3
        self.etiqueta_lineas_codigo_3 = tk.Label(self.marco_seccion_3, text="Establecer las líneas de Código\n por cada punto de función")
        self.etiqueta_lineas_codigo_3.grid(row=13, columnspan=4)
        self.entry_lineas_codigo_3 = tk.Entry(self.marco_seccion_3)
        self.entry_lineas_codigo_3.grid(row=14, columnspan=4)

        self.boton_calcular_3 = tk.Button(self.marco_seccion_3, text="Calcular", command=self.calcular_cocomo_3)
        self.boton_calcular_3.grid(row=15, columnspan=4)

        # Crear marco para mostrar los resultados - Parte 3
        self.marco_resultado_3 = tk.Frame(self.marco_seccion_3, borderwidth=1, relief="solid")
        self.marco_resultado_3.grid(row=16, columnspan=4, padx=5, pady=5)

        # Crear etiquetas para los resultados dentro del marco - Parte 3
        self.resultado_cocomo_3 = tk.Label(self.marco_resultado_3, text="", justify="left")
        self.resultado_cocomo_3.pack()

    def calcular_cocomo_1(self):
        try:
            salidas = float(self.entry_salidas.get())
            peso_s = float(self.entry_peso.get())
            entradas = float(self.entry_entradas.get())
            peso_e = float(self.entry_peso2.get())
            consultas = float(self.entry_consultas.get())
            peso_c = float(self.entry_peso3.get())
            archivos_internos = float(self.entry_archivo_interno.get())
            peso_ai = float(self.entry_peso4.get())
            archivos_externos = float(self.entry_archivo_externo.get())
            peso_ae = float(self.entry_peso5.get())
            lineas_codigo = float(self.entry_lineas_codigo.get())

            puntos_funcion = (salidas * peso_s) + (entradas * peso_e) + (consultas * peso_c) + (archivos_internos * peso_ai) + (archivos_externos * peso_ae)
            codigo_java = puntos_funcion*lineas_codigo
            kcodigo_java= codigo_java/1000
            esfuerzo = 2.4* (kcodigo_java**1.05)
            tiempo = 2.5 * (esfuerzo **0.38)
            
            self.resultado_cocomo_1.config(text=f"Puntos de Función: {puntos_funcion}\nEsfuerzo: {esfuerzo:.2f} PM\nTiempo de Desarrollo: {tiempo:.2f} Meses\nCódigo Java:\n{codigo_java}")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos.")

    def calcular_cocomo_2(self):
        try:
            salidas = float(self.entry_salidas_2.get())
            peso_s = float(self.entry_peso_2.get())
            entradas = float(self.entry_entradas_2.get())
            peso_e = float(self.entry_peso2_2.get())
            consultas = float(self.entry_consultas_2.get())
            peso_c = float(self.entry_peso3_2.get())
            archivos_internos = float(self.entry_archivo_interno_2.get())
            peso_ai = float(self.entry_peso4_2.get())
            archivos_externos = float(self.entry_archivo_externo_2.get())
            peso_ae = float(self.entry_peso5_2.get())
            lineas_codigo = float(self.entry_lineas_codigo_2.get())

            puntos_funcion = (salidas * peso_s) + (entradas * peso_e) + (consultas * peso_c) + (archivos_internos * peso_ai) + (archivos_externos * peso_ae)
            codigo_java = puntos_funcion*lineas_codigo
            kcodigo_java= codigo_java/1000
            esfuerzo = 3.0 * (kcodigo_java ** 1.12)
            tiempo = 2.5 * (esfuerzo ** 0.35)
            
            self.resultado_cocomo_2.config(text=f"Puntos de Función: {puntos_funcion}\nEsfuerzo: {esfuerzo} PM\nTiempo de Desarrollo: {tiempo} Meses\nCódigo Java:\n{codigo_java}")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos.")

    def calcular_cocomo_3(self):
        try:
            salidas = float(self.entry_salidas_3.get())
            peso_s = float(self.entry_peso_3.get())
            entradas = float(self.entry_entradas_3.get())
            peso_e = float(self.entry_peso2_3.get())
            consultas = float(self.entry_consultas_3.get())
            peso_c = float(self.entry_peso3_3.get())
            archivos_internos = float(self.entry_archivo_interno_3.get())
            peso_ai = float(self.entry_peso4_3.get())
            archivos_externos = float(self.entry_archivo_externo_3.get())
            peso_ae = float(self.entry_peso5_3.get())
            lineas_codigo = float(self.entry_lineas_codigo_3.get())

            puntos_funcion = (salidas * peso_s) + (entradas * peso_e) + (consultas * peso_c) + (archivos_internos * peso_ai) + (archivos_externos * peso_ae)
            codigo_java = puntos_funcion*lineas_codigo
            kcodigo_java= codigo_java/1000
            esfuerzo = 3.6 * (kcodigo_java ** 1.20)
            tiempo = 2.5 * (esfuerzo **0.32)

            self.resultado_cocomo_3.config(text=f"Puntos de Función: {puntos_funcion}\nEsfuerzo: {esfuerzo:.2f} PM\nTiempo de Desarrollo: {tiempo:.2f} Meses\nCódigo Java:\n{codigo_java}")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos.")

if __name__ == "__main__":
    root = tk.Tk()
    app = CocomoBasicoApp(root)
    root.mainloop()
