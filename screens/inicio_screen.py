import tkinter as tk
from tkinter import Canvas

class InicioScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#ffffff")
        self.controller = controller
        self.parent = parent
        
        self.canvas = Canvas(
            self,
            width=375,
            height=812,
            bg="#ffffff",
            highlightthickness=0
        )
        self.canvas.pack()
        
        self.create_background()
        self.create_header()
        self.create_features()
        self.create_buttons()
    
    def create_background(self):
        self.canvas.create_rectangle(
            0, 0, 375, 812,
            fill="#f4f6fb",
            outline=""
        )
        
        self.canvas.create_rectangle(
            0, 0, 375, 120,
            fill="#1565c0",
            outline=""
        )
    
    def create_header(self):
        self.canvas.create_text(
            187, 50,
            text="SALUNIC",
            font=("Nunito", 36, "bold"),
            fill="#ffffff"
        )
        
        self.canvas.create_text(
            187, 85,
            text="Salud y Bienestar",
            font=("Nunito", 12),
            fill="#e0e0e0"
        )
    
    def create_features(self):
        features = [
            {
                "title": "Citas Medicas",
                "description": "Reserva tus citas medicas de forma facil",
                "y": 180
            },
            {
                "title": "Medicamentos",
                "description": "Gestiona tus medicamentos y recordatorios",
                "y": 290
            },
            {
                "title": "Historial Medico",
                "description": "Accede a tu historial medico completo",
                "y": 400
            }
        ]
        
        for feature in features:
            self.canvas.create_rectangle(
                20, feature["y"], 355, feature["y"] + 90,
                fill="#ffffff",
                outline="#e0e0e0",
                width=1
            )
            
            self.canvas.create_text(
                40, feature["y"] + 20,
                text=feature["title"],
                font=("Nunito", 14, "bold"),
                fill="#1565c0",
                anchor="nw"
            )
            
            self.canvas.create_text(
                40, feature["y"] + 50,
                text=feature["description"],
                font=("Nunito", 11),
                fill="#666666",
                anchor="nw",
                width=290
            )
    
    def create_buttons(self):
        self.comenzar_button = self.canvas.create_rectangle(
            20, 680, 355, 730,
            fill="#2ecc71",
            outline=""
        )
        
        self.canvas.create_text(
            187, 705,
            text="Comenzar",
            font=("Nunito", 16, "bold"),
            fill="#ffffff"
        )
        
        self.canvas.bind("<Button-1>", self.on_click_comenzar)
        self.canvas.tag_bind(self.comenzar_button, "<Button-1>", self.on_click_comenzar)
        
        self.iniciar_button = self.canvas.create_rectangle(
            20, 750, 355, 800,
            fill="#ffffff",
            outline="#1565c0",
            width=2
        )
        
        self.canvas.create_text(
            187, 775,
            text="Iniciar Sesion",
            font=("Nunito", 16, "bold"),
            fill="#1565c0"
        )
        
        self.canvas.tag_bind(self.iniciar_button, "<Button-1>", self.on_click_iniciar)
    
    def on_click_comenzar(self, event):
        if 20 <= event.x <= 355 and 680 <= event.y <= 730:
            self.controller.show_screen("Registro")
    
    def on_click_iniciar(self, event):
        if 20 <= event.x <= 355 and 750 <= event.y <= 800:
            self.controller.show_screen("Login")
