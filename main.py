import tkinter as tk

from screens.home_screen import HomeScreen
from screens.inicio_screen import InicioScreen
from screens.login_screen import LoginScreen
from screens.forms.form_registro import FormRegistro
from screens.splash_screen import SplashScreen


class SalunicApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Salunic - Salud y Bienestar Nicaragua")
        self.root.geometry("375x812")
        self.root.resizable(False, False)
        self.root.config(bg="#f4f6fb")

        self.container = tk.Frame(root, bg="#f4f6fb")
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for screen_class in (SplashScreen, InicioScreen, LoginScreen, FormRegistro, HomeScreen):
            frame = screen_class(self.container, self)
            self.frames[screen_class.__name__] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_screen("SplashScreen")

    def show_screen(self, screen_name):
        frame = self.frames[screen_name]
        frame.tkraise()
        if hasattr(frame, "on_show"):
            frame.on_show()


def main():
    root = tk.Tk()
    SalunicApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
