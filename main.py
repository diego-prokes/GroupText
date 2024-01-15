import customtkinter as ctk
from ui.main_window import MainWindow

if __name__ == "__main__":

    app = ctk.CTk()
    app.title('Grupo Texto')
    app.geometry("1200x600-0-0")
    app._set_appearance_mode("system")
    app.resizable(width=True, height=True)

    main_window = MainWindow(app)
    main_window.pack(fill="both", expand=True)

    app.mainloop()
