import tkinter as tk
from tkinter import filedialog, ttk, messagebox
import pandas as pd 

class ProcesadorPersonas:

    def __init__(self, root):
        self.root = root
        self.root.title("Algoritmo")
        self.root.geometry("800x500")

        self.df = None

        # Boton cargar archivo
        self.btn_cargar = tk.Button(root, text="Seleccionar archivo .txt", command=self.cargar_archivo)
        self.btn_cargar.pack(pady=10)

        # Selector de columna
        self.combo_columnas = ttk.Combobox(root, state="readonly")
        self.combo_columnas.pack(pady=5)

        # Orden 
        self.orden_var = tk.StringVar(value="Ascendente")
        tk.Radiobutton(root, text="Ascendente", variable=self.orden_var, value="Ascendente").pack()
        tk.Radiobutton(root, text="Descendente", variable=self.orden_var, value="Descendente").pack()

        # Boton ordenar
        self.btn_ordenar = tk.Button(root, text="Ordenar", command=self.ordenar_datos)
        self.btn_ordenar.pack(pady=10)

        # Tabla
        self.tree = ttk.Treeview(root)
        self.tree.pack(expand=True, fill="both")

        # Boton descargar
        self.btn_descargar = tk.Button(root, text="Descargar CSV", command=self.descargar_csv)
        self.btn_descargar.pack(pady=10)

    def cargar_archivo(self):
        ruta = filedialog.askopenfilename(filetypes=[("Archivos de texto", "*.txt")])
        if not ruta:
            return

        with open(ruta, "r", encoding="utf-8") as f:
            content = f.read()

        data = []
        lines = content.strip().split('\n')

        for line in lines:
            parts = [p.strip() for p in line.split(',')]
            if len(parts) >= 2:
                data.append(parts)

        if not data:
            messagebox.showerror("Error", "Archivo vacío o mal formateado")
            return

        columns = ["Nombre", "Edad", "Ciudad"] if len(data[0]) == 3 else [f"Dato {i+1}" for i in range(len(data[0]))]
        self.df = pd.DataFrame(data, columns=columns)

        self.combo_columnas["values"] = list(self.df.columns)
        self.combo_columnas.current(0)

        self.mostrar_tabla(self.df)

    def mostrar_tabla(self, dataframe):
        self.tree.delete(*self.tree.get_children())
        self.tree["columns"] = list(dataframe.columns)
        self.tree["show"] = "headings"

        for col in dataframe.columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=150)

        for _, row in dataframe.iterrows():
            self.tree.insert("", "end", values=list(row))

    def ordenar_datos(self):
        if self.df is None:
            messagebox.showwarning("Advertencia", "Primero carga un archivo")
            return

        columna = self.combo_columnas.get()
        asc = self.orden_var.get() == "Ascendente"

        df_sorted = self.df.sort_values(by=columna, ascending=asc)
        self.mostrar_tabla(df_sorted)
        self.df = df_sorted

    def descargar_csv(self):
        if self.df is None:
            return

        ruta = filedialog.asksaveasfilename(defaultextension=".csv",
                                            filetypes=[("CSV", "*.csv")])
        if ruta:
            self.df.to_csv(ruta, index=False)
            messagebox.showinfo("Éxito", "Archivo guardado correctamente")


if __name__ == "__main__":
    root = tk.Tk()
    app = ProcesadorPersonas(root)
    root.mainloop()