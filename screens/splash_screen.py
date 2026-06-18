import tkinter as tk
from tkinter import Canvas
import math

class SplashScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#1565c0")
        self.controller = controller
        self.parent = parent
        
        self.canvas = Canvas(
            self,
            width=375,
            height=812,
            bg="#1565c0",
            highlightthickness=0
        )
        self.canvas.pack()
        
        self.angle = 0
        self.create_splash()
        self.animate()
    
    def create_splash(self):
        # Fondo azul
        self.canvas.create_rectangle(
            0, 0, 375, 812,
            fill="#1565c0",
            outline=""
        )
        
        # Logo/Título
        self.canvas.create_text(
            187, 300,
            text="SALUNIC",
            font=("Nunito", 48, "bold"),
            fill="#ffffff"
        )
        
        # Subtítulo
        self.canvas.create_text(
            187, 370,
            text="Salud y Bienestar",
            font=("Nunito", 16),
            fill="#e0e0e0"
        )
        
        # Círculos animados
        self.circle1_id = self.canvas.create_oval(
            150, 450, 210, 510,
            fill="",
            outline="#2ecc71",
            width=3
        )
        
        self.circle2_id = self.canvas.create_oval(
            165, 450, 225, 510,
            fill="",
            outline="#3498db",
            width=3
        )
        
        self.circle3_id = self.canvas.create_oval(
            180, 450, 240, 510,
            fill="",
            outline="#e74c3c",
            width=3
        )
        
        # Texto de carga
        self.canvas.create_text(
            187, 560,
            text="Cargando...",
            font=("Nunito", 12),
            fill="#ffffff"
        )
    
    def animate(self):
        self.angle += 6
        
        if self.angle >= 360:
            self.angle = 0
            # Después de 3 segundos, ir a Inicio
            self.after(2000, lambda: self.controller.show_screen("Inicio"))
            return
        
        # Rotar círculos
        center_x, center_y = 187, 480
        radius = 30
        
        rad = math.radians(self.angle)
        x1 = center_x + radius * math.cos(rad) - 30
        y1 = center_y + radius * math.sin(rad) - 30
        x2 = x1 + 60
        y2 = y1 + 60
        
        self.canvas.coords(self.circle1_id, x1, y1, x2, y2)
        
        rad2 = math.radians(self.angle + 120)
        x1 = center_x + radius * math.cos(rad2) - 30
        y1 = center_y + radius * math.sin(rad2) - 30
        x2 = x1 + 60
        y2 = y1 + 60
        
        self.canvas.coords(self.circle2_id, x1, y1, x2, y2)
        
        rad3 = math.radians(self.angle + 240)
        x1 = center_x + radius * math.cos(rad3) - 30
        y1 = center_y + radius * math.sin(rad3) - 30
        x2 = x1 + 60
        y2 = y1 + 60
        
        self.canvas.coords(self.circle3_id, x1, y1, x2, y2)
        
        self.after(50, self.animate)
