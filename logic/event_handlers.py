from tkinter import filedialog
from pathlib import Path
import docx
from PIL import Image
import pytesseract
import fitz  # PyMuPDF
import threading
import sys
import os

if getattr(sys, 'frozen', False):
    _path = os.path.join(sys._MEIPASS, './tesseract/tesseract.exe')
    pytesseract.pytesseract.tesseract_cmd = _path
else:
    pytesseract.pytesseract.tesseract_cmd = r'C:\Users\DProkes\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

class EventHandler:
    def __init__(self, main_window):
        # Referencia a la ventana principal para acceder a sus elementos
        self.main_window = main_window
        self.doc_list = []
        self.text = ''

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

    def copy_to_clipboard(self, event):
        print(event)
        # copy text to clipboard

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

    def open_file_location(self):
        return 0


    def select_directory(self):
        print("Seleccionando Directorio")
        directorio = filedialog.askdirectory()
        entry = self.main_window.output_directory_entry
        if entry.get():
            entry.delete(0,len(entry.get()))
        self.main_window.output_directory_entry.insert(0,directorio)

    def generate_text(self):
        # Preparar la interfaz de usuario para la operación
        self.main_window.textbox.configure(state='normal')
        self.main_window.textbox.delete("0.0", "end")

        # Crear y empezar hilos para procesar cada documento
        threads = []
        for document in self.doc_list:
            thread = threading.Thread(target=self.process_document, args=(document,))
            threads.append(thread)
            thread.start()

        # Esperar a que todos los hilos terminen
        for thread in threads:
            thread.join()

        # Actualizar la interfaz de usuario después de completar la operación
        self.main_window.textbox.insert("0.0", "Texto Generado")
        self.main_window.textbox.configure(state='disabled')

    def process_document(self, document):
        file_path = document[0]
        text = f"=== Título: {Path(file_path).name} ===\n\n"
        if file_path.endswith('.docx'):
            text += self.extract_text_from_docx(file_path)
        elif file_path.endswith('.doc'):
            text += self.extract_text_from_doc(file_path)
        elif file_path.endswith('.pdf'):
            text += self.extract_text_from_pdf(file_path)
        else:
            raise ValueError("Unsupported file format")

        # Asegúrate de que el acceso a la variable compartida 'self.text' sea seguro para hilos
        with threading.Lock():
            self.text += text

    
    def delete_text(self):
        self.main_window.textbox.configure(state='normal')
        self.text=''
        self.main_window.textbox.delete("0.0", "end")
        self.main_window.textbox.insert("0.0", "Texto Eliminado")
        self.main_window.textbox.configure(state='disabled')

    def extract_text_from_docx(self, file_path):
        doc = docx.Document(file_path)
        text = "\n".join([para.text for para in doc.paragraphs])
        return text
        
    def extract_text_from_doc(self, file_path):
        # Esta función requiere que estés en un entorno Windows
        try:
            import win32com.client
            word = win32com.client.Dispatch("Word.Application")
            word.visible = False
            wb = word.Documents.Open(file_path)
            doc = word.ActiveDocument
            text = doc.Range().Text
            doc.Close()
            word.Quit()
            return text
        except Exception as e:
            print(f"Error al procesar el archivo DOC: {e}")
            return ""
        
    def extract_text_from_pdf(self, file_path):
        texto = ''
        documento_pdf = fitz.open(file_path)
        for pagina in range(len(documento_pdf)):
            texto_pagina = self.convertir_pagina_a_texto(documento_pdf, pagina)
            texto += texto_pagina + "\n"
        return texto

    def convertir_pagina_a_texto(self, pdf_documento, pagina):
        pagina_pdf = pdf_documento.load_page(pagina)
        imagen = pagina_pdf.get_pixmap()
        imagen_pil = Image.frombytes("RGB", [imagen.width, imagen.height], imagen.samples)
        texto = pytesseract.image_to_string(imagen_pil, lang='spa')  # Usamos pytesseract para OCR
        return texto

    def save_text_to_file(self, text, file_path):
        try:
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(text)
            print(f"Texto guardado con éxito en {file_path}")
        except Exception as e:
            print(f"Error al guardar el texto: {e}")
        return file_path
    
    def ask_save_file_and_write_text(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if file_path:
            output_filepath = self.save_text_to_file(self.text, file_path)
            self.main_window.textbox.delete("0.0", 'end')
            self.main_window.textbox.insert("0.0", f'Texto guardado en:\n{file_path}')      
