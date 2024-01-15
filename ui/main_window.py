import customtkinter as ctk
from CTkListbox import CTkListbox
from tkinter import filedialog, messagebox
from pathlib import Path  


class MainWindow(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

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

        self.controls_frame = ctk.CTkFrame(master=self.content_frame)
        self.controls_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        self.options_frame = ctk.CTkFrame(master=self.content_frame)
        self.options_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew",columnspan=1)

        # self.right_frame = ctk.CTkFrame(master=self)
        # self.right_frame.grid(row=0, column=1, padx=10, pady=20, sticky="nsew")

        # self.docs_frame = ctk.CTkFrame(master=self.right_frame)
        # self.docs_frame.pack(pady=10, side="left")

        # Left Frame Content
        for i in range(20):  # Puedes cambiar el número de botones aquí
            button = ctk.CTkButton(self.question_template_frame, text=f"Button {i+1}", command=lambda i=i: self.button_click(i))
            button.pack(pady=10, padx=20, fill='x')

        # Right Frame Content
            
        # Menú para cargar documentos
        self.load_button = ctk.CTkButton(self.controls_frame, text="Cargar Documento", command=self.load_document)
        self.load_button.pack(pady=5)

        self.listbox = CTkListbox(self.panel_frame, command=self.show_value)
        self.listbox.pack(fill="both", expand=True, padx=10, pady=10)

        # Botones para mover los elementos
        up_button = ctk.CTkButton(self.controls_frame, text="Move Up", command=self.move_up)
        up_button.pack(pady=5)

        down_button = ctk.CTkButton(self.controls_frame, text="Move Down", command=self.move_down)
        down_button.pack(pady=5)

        # Botón para eliminar elementos
        delete_button = ctk.CTkButton(self.controls_frame, text="Eliminar", command=self.delete_doc, fg_color="red")
        delete_button.pack(pady=5)

        # Botón para generar Texto
        gen_text_button = ctk.CTkButton(self.options_frame, text="Generar Texto", command=self.generate_text)
        gen_text_button.pack(pady=5)



    def load_document(self):
        # Función para cargar documentos
        file_paths = filedialog.askopenfilenames()
        file_paths = list(file_paths)
        if len(file_paths)>=1:
            for file_path in file_paths:
                self.listbox.insert("end", Path(file_path).name)
            pass

    def button_click(self, i):
        print(f"Button {i+1} pressed")

    def show_value(self, selected_option):
        print(selected_option)


    def move_up(self):
        selected_indices = self.listbox.curselection()
        if selected_indices:
            self.listbox.move_up(selected_indices)

    def move_down(self):
        selected_indices = self.listbox.curselection()
        if selected_indices or selected_indices==0:
            self.listbox.move_down(selected_indices)

    def delete_doc(self):
        selected_indices = self.listbox.curselection()
        if selected_indices or selected_indices==0:
            self.listbox.delete(selected_indices)
    
    def generate_text(self):
        print("Generando...")
