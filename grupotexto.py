import customtkinter as ctk
from tkinter import filedialog, messagebox

class GrupoTextoApp(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title('Grupo Texto')
        self.geometry('800x600')

        # Menú para cargar documentos
        self.load_button = ctk.CTkButton(self, text="Cargar Documento", command=self.load_document)
        self.load_button.pack(pady=20)

        # Área de texto para mostrar texto extraído
        self.text_area = ctk.CTkTextbox(self, height=10)
        self.text_area.pack(pady=20)

        # Botón para copiar al portapapeles
        self.copy_button = ctk.CTkButton(self, text="Copiar al Portapapeles", command=self.copy_to_clipboard)
        self.copy_button.pack(pady=10)

        # Botón para guardar como archivo de texto
        self.save_button = ctk.CTkButton(self, text="Guardar como Archivo", command=self.save_file)
        self.save_button.pack(pady=10)

    def load_document(self):
        # Función para cargar documentos
        file_path = filedialog.askopenfilename()
        if file_path:
            # Aquí se debe implementar la lógica para extraer texto del documento
            pass

    def copy_to_clipboard(self):
        # Función para copiar texto al portapapeles
        self.clipboard_clear()
        self.clipboard_append(self.text_area.get("1.0", "end-1c"))

    def save_file(self):
        # Función para guardar texto en un archivo
        file_path = filedialog.asksaveasfilename(defaultextension=".txt")
        if file_path:
            with open(file_path, "w") as file:
                file.write(self.text_area.get("1.0", "end-1c"))
            messagebox.showinfo("Información", "Archivo guardado con éxito")

if __name__ == "__main__":
    app = GrupoTextoApp()
    app.mainloop()
