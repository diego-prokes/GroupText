from tkinter import filedialog
from pathlib import Path

class EventHandler:
    def __init__(self, main_window):
        # Referencia a la ventana principal para acceder a sus elementos
        self.main_window = main_window
        self.doc_list = []

    def load_documents(self):
        # Función para cargar documentos
        file_paths = filedialog.askopenfilenames(filetypes=[("All Files", "*.pdf;*.docx;*.doc;*.png;*.jpg;*.jpeg")])
        file_paths = list(file_paths)
        if len(file_paths)>=1:
            for file_path in file_paths:
                element = (file_path, Path(file_path).name)
                if element not in self.doc_list:
                    self.doc_list.append(element)
                    self.main_window.listbox.insert("end", self.doc_list[-1][1])
            pass

    def button_click(self, i):
        print(f"Button {i+1} pressed")

    def show_value(self, selected_option):
        print(selected_option)


    def move_up(self):
        index = self.main_window.listbox.curselection()
        if index:
            if 1 <= index <= len(self.doc_list) - 1:
                self.doc_list[index], self.doc_list[index - 1] = self.doc_list[index - 1], self.doc_list[index]
                self.main_window.listbox.move_up(index)

    def move_down(self):
        index = self.main_window.listbox.curselection()
        if index or index==0:
            if 0 <= index < len(self.doc_list) - 1:
                self.doc_list[index], self.doc_list[index + 1] = self.doc_list[index + 1], self.doc_list[index]
                self.main_window.listbox.move_down(index)

    def delete_doc(self):
        index = self.main_window.listbox.curselection()
        if index or index==0:
            elemento_eliminado = self.doc_list.pop(index)
            self.main_window.listbox.delete(index)

    def preview(self):
        print("Vista Previa del documento")

    def select_directory(self):
        print("Seleccionando Directorio")
        directorio = filedialog.askdirectory()
        entry = self.output_directory_entry
        if entry.get():
            entry.delete(0,len(entry.get()))
        self.output_directory_entry.insert(0,directorio)
    
    def generate_text(self):
        print("Generando...")
