import customtkinter as ctk
from CTkListbox import CTkListbox
from tkinter import filedialog, messagebox
from pathlib import Path  
from PIL import Image


class MainWindow(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        # MainWindows
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=5)
        self.grid_rowconfigure(0, weight=1)

        self.doc_list = []

        # Frames
        self.question_template_frame = ctk.CTkScrollableFrame(master=self)
        self.question_template_frame.grid(row=0, column=0, padx=10, pady=20, sticky="nsew")

        self.content_frame = ctk.CTkFrame(master=self)
        self.content_frame.grid(row=0, column=1, padx=10, pady=20, sticky="nsew")

        self.content_frame.grid_columnconfigure(0, weight=4)
        self.content_frame.grid_columnconfigure(1, weight=1)
        self.content_frame.grid_rowconfigure(0, weight=1)

        self.panel_frame = ctk.CTkFrame(master=self.content_frame)
        self.panel_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.utils_frame = ctk.CTkFrame(master=self.content_frame)
        self.utils_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        
        self.utils_frame.grid_columnconfigure(0, weight=1)
        self.utils_frame.grid_rowconfigure(0, weight=1)

        self.controls_frame = ctk.CTkFrame(master=self.utils_frame)
        self.controls_frame.pack(padx=5, pady=5, fill="x")

        self.preview_frame = ctk.CTkFrame(master=self.utils_frame)
        self.preview_frame.pack(padx=5, pady=5, fill="both")

        self.options_frame = ctk.CTkFrame(master=self.content_frame)
        self.options_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        self.generate_frame = ctk.CTkFrame(master=self.content_frame)
        self.generate_frame.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")


        # Question Template Frame Content
        for i in range(10):  # Puedes cambiar el número de botones aquí
            button = ctk.CTkButton(self.question_template_frame, text=f"Plantilla {i+1}\nDescripción", command=lambda i=i: self.button_click(i))
            button.pack(pady=10, padx=20, fill='x')

        # Content Frame Content
            
        # Panel Frame Content
        self.listbox = CTkListbox(self.panel_frame, command=self.show_value)
        self.listbox.pack(fill="both", expand=True, padx=10, pady=10)

        # Utils Frame Content

        # Controls Frame Content

        # Label de controls frame
        controls_label = ctk.CTkLabel(self.controls_frame, text="Controles: ", fg_color="transparent")
        controls_label.pack(pady=5, padx=5, side="left")
        
        # Menú para cargar documentos
        self.load_button = ctk.CTkButton(self.controls_frame, text="Cargar Documentos", command=self.load_documents, fg_color="green", hover_color="dark green")
        self.load_button.pack(pady=5)

        # Botones para mover los elementos
        up_button = ctk.CTkButton(self.controls_frame, text="Subir", command=self.move_up)
        up_button.pack(pady=5)

        down_button = ctk.CTkButton(self.controls_frame, text="Bajar", command=self.move_down)
        down_button.pack(pady=5)

        # Botón para mostrar vista previa
        preview_button = ctk.CTkButton(self.controls_frame, text="Vista Previa", command=self.preview)
        preview_button.pack(pady=5)

        # Botón para eliminar elementos
        delete_button = ctk.CTkButton(self.controls_frame, text="Eliminar", command=self.delete_doc, fg_color="red", hover_color="dark red")
        delete_button.pack(pady=5)

        # Preview Frame Content
        controls_label = ctk.CTkLabel(self.preview_frame, text="Panel de Vista Previa: ", fg_color="transparent")
        controls_label.pack(pady=5, padx=5, fill="y")

        # Label para directorio de salida
        output_directory_label = ctk.CTkLabel(self.options_frame, text="Ruta de salida: ", fg_color="transparent")
        output_directory_label.pack(pady=5, padx=5, side="left")

        # Entrada para seleccionar direcotorio de salida
        self.output_directory_entry = ctk.CTkEntry(self.options_frame, placeholder_text="ruta de salida", width=400)
        self.output_directory_entry.pack(pady=5, padx=5, side="left", fill="x")

        # Botón para seleccionar directorio de salida
        output_directory_button = ctk.CTkButton(self.options_frame, text="Seleccionar", command=self.select_directory)
        output_directory_button.pack(pady=5, padx=5, side="right")

        # Botón para generar Texto
        gen_text_button = ctk.CTkButton(self.generate_frame, text="Generar Texto", command=self.generate_text, fg_color="yellow", hover_color="orange", text_color="black")
        gen_text_button.pack(padx=30, pady=5)



    def load_documents(self):
        # Función para cargar documentos
        file_paths = filedialog.askopenfilenames(filetypes=[("All Files", "*.pdf;*.docx;*.doc;*.png;*.jpg;*.jpeg")])
        file_paths = list(file_paths)
        if len(file_paths)>=1:
            for file_path in file_paths:
                element = (file_path, Path(file_path).name)
                if element not in self.doc_list:
                    self.doc_list.append(element)
                    self.listbox.insert("end", self.doc_list[-1][1])
            pass

    def button_click(self, i):
        print(f"Button {i+1} pressed")

    def show_value(self, selected_option):
        print(selected_option)


    def move_up(self):
        index = self.listbox.curselection()
        if index:
            if 1 <= index <= len(self.doc_list) - 1:
                self.doc_list[index], self.doc_list[index - 1] = self.doc_list[index - 1], self.doc_list[index]
                self.listbox.move_up(index)

    def move_down(self):
        index = self.listbox.curselection()
        if index or index==0:
            if 0 <= index < len(self.doc_list) - 1:
                self.doc_list[index], self.doc_list[index + 1] = self.doc_list[index + 1], self.doc_list[index]
                self.listbox.move_down(index)

    def delete_doc(self):
        index = self.listbox.curselection()
        if index or index==0:
            elemento_eliminado = self.doc_list.pop(index)
            self.listbox.delete(index)

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
