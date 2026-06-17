import tkinter as tk
from screens.home_screen import HomeScreen

class SalunicApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Salunic - Salud y Bienestar Nicaragua")
        self.root.geometry("375x812")
        self.root.resizable(False, False)
        self.root.config(bg="#f4f6fb")
        
        # Contenedor principal
        self.container = tk.Frame(root, bg="#f4f6fb")
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)
        
        # Mostrar HomeScreen directamente con diseño de Figma
        self.home_screen = HomeScreen(self.container, self)
        self.home_screen.grid(row=0, column=0, sticky="nsew")

def main():
    root = tk.Tk()
    app = SalunicApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
