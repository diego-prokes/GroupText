import customtkinter as ctk
from CTkListbox import CTkListbox
from tkinter import filedialog, messagebox
from pathlib import Path  
from PIL import Image
from logic.event_handlers import EventHandler


class MainWindow(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.event_handler = EventHandler(self)

        # MainWindows
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=5)
        self.grid_rowconfigure(0, weight=1)

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
        self.listbox = CTkListbox(self.panel_frame, command=self.event_handler.show_value)
        self.listbox.pack(fill="both", expand=True, padx=10, pady=10)

        # Utils Frame Content

        # Controls Frame Content

        # Label de controls frame
        controls_label = ctk.CTkLabel(self.controls_frame, text="Controles: ", fg_color="transparent")
        controls_label.pack(pady=5, padx=5, side="left")
        
        # Menú para cargar documentos
        self.load_button = ctk.CTkButton(self.controls_frame, text="Cargar Documentos", command=self.event_handler.load_documents, fg_color="green", hover_color="dark green")
        self.load_button.pack(pady=5)

        # Botones para mover los elementos
        up_button = ctk.CTkButton(self.controls_frame, text="Subir", command=self.event_handler.move_up)
        up_button.pack(pady=5)

        down_button = ctk.CTkButton(self.controls_frame, text="Bajar", command=self.event_handler.move_down)
        down_button.pack(pady=5)

        # Botón para mostrar vista previa
        preview_button = ctk.CTkButton(self.controls_frame, text="Vista Previa", command=self.event_handler.preview)
        preview_button.pack(pady=5)

        # Botón para eliminar elementos
        delete_button = ctk.CTkButton(self.controls_frame, text="Eliminar", command=self.event_handler.delete_doc, fg_color="red", hover_color="dark red")
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
        output_directory_button = ctk.CTkButton(self.options_frame, text="Seleccionar", command=self.event_handler.select_directory)
        output_directory_button.pack(pady=5, padx=5, side="right")

        # Botón para generar Texto
        gen_text_button = ctk.CTkButton(self.generate_frame, text="Generar Texto", command=self.event_handler.generate_text, fg_color="yellow", hover_color="orange", text_color="black")
        gen_text_button.pack(padx=30, pady=5)
