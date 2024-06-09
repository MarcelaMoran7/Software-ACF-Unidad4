import tkinter as tk
from tkinter import ttk

class COCOMOIntermedioApp:
    def __init__(self, root):
        self.root = root
        self.root.title("COCOMO INTERMEDIO")

        # Dividir la ventana en dos partes con un PanedWindow
        self.paned_window = ttk.PanedWindow(self.root, orient=tk.HORIZONTAL)
        self.paned_window.pack(expand=True, fill=tk.BOTH)

        # Crear la primera sección
        self.seccion_1_frame = ttk.Frame(self.paned_window, relief=tk.RIDGE)
        self.crear_seccion(self.seccion_1_frame, "Modelo Orgánico - Sección 1", 0, 1)
        self.paned_window.add(self.seccion_1_frame)

        # Crear la segunda sección
        self.seccion_2_frame = ttk.Frame(self.paned_window, relief=tk.RIDGE)
        self.crear_seccion(self.seccion_2_frame, "Modelo SemiAcoplado - Sección 2", 0, 2)
        self.paned_window.add(self.seccion_2_frame)

        # Crear la tercera sección
        self.seccion_3_frame = ttk.Frame(self.paned_window, relief=tk.RIDGE)
        self.crear_seccion(self.seccion_3_frame, "Modelo Empotrado - Sección 3", 0, 3)
        self.paned_window.add(self.seccion_3_frame)

    def calcular_pfa(self, entradas_entry, entradas_peso_entry, salidas_entry, salidas_peso_entry,
                     consultas_entry, consultas_peso_entry, archivos_internos_entry,
                     archivos_internos_peso_entry, archivos_externos_entry,
                     archivos_externos_peso_entry, entradas_numericas, lineas_codigo_entry,
                     resultado_label, suma_numeros_label, punto_de_funcion_2_label,
                     ldc_label, persona_por_mes_label, meses_label, section):
        try:
            peso_entradas = int(entradas_peso_entry.get())
            peso_salidas = int(salidas_peso_entry.get())
            peso_consultas = int(consultas_peso_entry.get())
            peso_archivos_internos = int(archivos_internos_peso_entry.get())
            peso_archivos_externos = int(archivos_externos_peso_entry.get())

            entradas = int(entradas_entry.get())
            salidas = int(salidas_entry.get())
            consultas = int(consultas_entry.get())
            archivos_internos = int(archivos_internos_entry.get())
            archivos_externos = int(archivos_externos_entry.get())

            pfa_entradas = entradas * peso_entradas
            pfa_salidas = salidas * peso_salidas
            pfa_consultas = consultas * peso_consultas
            pfa_archivos_internos = archivos_internos * peso_archivos_internos
            pfa_archivos_externos = archivos_externos * peso_archivos_externos

            punto_de_funcion_ajustado = (pfa_entradas +
                                         pfa_salidas +
                                         pfa_consultas +
                                         pfa_archivos_internos +
                                         pfa_archivos_externos)

            suma_numeros = sum(int(entry.get()) for entry in entradas_numericas)

            punto_de_funcion_2 = punto_de_funcion_ajustado * (0.65 + 0.01 * suma_numeros)

            lineas_codigo_necesarias = int(lineas_codigo_entry.get())
            ldc = punto_de_funcion_2 * lineas_codigo_necesarias

            if section == 1:
                persona_por_mes = (ldc / 1000) * 3.2 ** 1.05
            elif section == 2:
                persona_por_mes = (ldc / 1000) * 3.0 ** 1.12
            elif section == 3:
                persona_por_mes = (ldc / 1000) * 2.8 ** 1.20

            meses = 2.5 * (persona_por_mes ** 0.38)

            resultado_label.config(text="El punto de función Ajustado es: " + str(punto_de_funcion_ajustado))
            suma_numeros_label.config(text="La Suma de los Números es: " + str(suma_numeros))
            punto_de_funcion_2_label.config(text="El punto de Función 2 es: " + str(punto_de_funcion_2))
            ldc_label.config(text="El producto de LDC es: " + str(ldc))
            persona_por_mes_label.config(text="Persona por Mes es: " + str(persona_por_mes))
            meses_label.config(text="Tiempo en Meses es: " + str(meses))
        except ValueError:
            resultado_label.config(text="Por favor, ingrese números válidos para los pesos y las entradas.")

    def crear_seccion(self, frame, titulo, row_start, section):
        seccion_frame = ttk.LabelFrame(frame, text=titulo)
        seccion_frame.grid(row=row_start, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")

        tk.Label(seccion_frame, text="Número de Entradas:").grid(row=0, column=0)
        entradas_entry = tk.Entry(seccion_frame)
        entradas_entry.grid(row=0, column=1)
        tk.Label(seccion_frame, text="Peso de Entradas:").grid(row=0, column=2)
        entradas_peso_entry = tk.Entry(seccion_frame)
        entradas_peso_entry.grid(row=0, column=3)

        tk.Label(seccion_frame, text="Número de Salidas:").grid(row=1, column=0)
        salidas_entry = tk.Entry(seccion_frame)
        salidas_entry.grid(row=1, column=1)
        tk.Label(seccion_frame, text="Peso de Salidas:").grid(row=1, column=2)
        salidas_peso_entry = tk.Entry(seccion_frame)
        salidas_peso_entry.grid(row=1, column=3)

        tk.Label(seccion_frame, text="Número de Consultas:").grid(row=2, column=0)
        consultas_entry = tk.Entry(seccion_frame)
        consultas_entry.grid(row=2, column=1)
        tk.Label(seccion_frame, text="Peso de Consultas:").grid(row=2, column=2)
        consultas_peso_entry = tk.Entry(seccion_frame)
        consultas_peso_entry.grid(row=2, column=3)

        tk.Label(seccion_frame, text="Número de Archivos Internos:").grid(row=3, column=0)
        archivos_internos_entry = tk.Entry(seccion_frame)
        archivos_internos_entry.grid(row=3, column=1)
        tk.Label(seccion_frame, text="Peso de Archivos Internos:").grid(row=3, column=2)
        archivos_internos_peso_entry = tk.Entry(seccion_frame)
        archivos_internos_peso_entry.grid(row=3, column=3)

        tk.Label(seccion_frame, text="Número de Archivos Externos:").grid(row=4, column=0)
        archivos_externos_entry = tk.Entry(seccion_frame)
        archivos_externos_entry.grid(row=4, column=1)
        tk.Label(seccion_frame, text="Peso de Archivos Externos:").grid(row=4, column=2)
        archivos_externos_peso_entry = tk.Entry(seccion_frame)
        archivos_externos_peso_entry.grid(row=4, column=3)

        tk.Label(seccion_frame, text="Ingrese las 14 preguntas", font=("Arial", 9, "bold")).grid(row=5, columnspan=4)

        entradas_numericas = []
        for i in range(6, 20):
            tk.Label(seccion_frame, text="Pregunta " + str(i - 5)).grid(row=i, column=0)
            tk.Entry(seccion_frame).grid(row=i, column=1)
            tk.Label(seccion_frame, text="Valor de Importancia " + str(i - 5)).grid(row=i, column=2)
            entry_numerica = tk.Entry(seccion_frame)
            entry_numerica.grid(row=i, column=3)
            entradas_numericas.append(entry_numerica)

        tk.Label(seccion_frame, text="Número de Líneas de Código Necesarias:").grid(row=20, column=0)
        lineas_codigo_entry = tk.Entry(seccion_frame)
        lineas_codigo_entry.grid(row=20, column=1)
        lineas_codigo_label = tk.Label(seccion_frame, text="")
        lineas_codigo_label.grid(row=20, column=2)

        tk.Label(seccion_frame, text="Ingrese los valores de Imp. para cada pregunta:", font=("Arial", 9, "italic")).grid(row=21, column=2, columnspan=2)

        calcular_button = tk.Button(seccion_frame, text="Calcular",
                                    command=lambda: self.calcular_pfa(entradas_entry, entradas_peso_entry,
                                                                      salidas_entry, salidas_peso_entry,
                                                                      consultas_entry, consultas_peso_entry,
                                                                      archivos_internos_entry,
                                                                      archivos_internos_peso_entry,
                                                                      archivos_externos_entry,
                                                                      archivos_externos_peso_entry,
                                                                      entradas_numericas, lineas_codigo_entry,
                                                                      resultado_label, suma_numeros_label,
                                                                      punto_de_funcion_2_label, ldc_label,
                                                                      persona_por_mes_label, meses_label, section))
        calcular_button.grid(row=22, columnspan=4)

        resultado_label = tk.Label(seccion_frame, text="")
        resultado_label.grid(row=23, columnspan=4)

        suma_numeros_label = tk.Label(seccion_frame, text="")
        suma_numeros_label.grid(row=24, columnspan=4)

        punto_de_funcion_2_label = tk.Label(seccion_frame, text="")
        punto_de_funcion_2_label.grid(row=25, columnspan=4)

        ldc_label = tk.Label(seccion_frame, text="")
        ldc_label.grid(row=26, columnspan=4)

        persona_por_mes_label = tk.Label(seccion_frame, text="")
        persona_por_mes_label.grid(row=27, columnspan=4)

        meses_label = tk.Label(seccion_frame, text="")
        meses_label.grid(row=28, columnspan=4)

if __name__ == "__main__":
    root = tk.Tk()
    app = COCOMOIntermedioApp(root)
    root.mainloop()
