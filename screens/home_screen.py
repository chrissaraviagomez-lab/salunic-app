import tkinter as tk
from tkinter import Canvas, messagebox
from datetime import datetime

class HomeScreen(tk.Frame):
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
        self.create_user_info()
        self.create_dashboard()
        self.create_bottom_menu()
    
    def create_background(self):
        self.canvas.create_rectangle(
            0, 0, 375, 812,
            fill="#f4f6fb",
            outline=""
        )
    
    def create_header(self):
        self.canvas.create_rectangle(
            0, 0, 375, 80,
            fill="#1565c0",
            outline=""
        )
        
        self.canvas.create_text(
            20, 30,
            text="SALUNIC",
            font=("Nunito", 24, "bold"),
            fill="#ffffff",
            anchor="nw"
        )
        
        user_email = self.controller.logged_in_user if hasattr(self.controller, 'logged_in_user') else "usuario@salunic.com"
        self.canvas.create_text(
            20, 55,
            text=f"Bienvenido: {user_email}",
            font=("Nunito", 10),
            fill="#e0e0e0",
            anchor="nw"
        )
    
    def create_user_info(self):
        today = datetime.now().strftime("%d de %B de %Y")
        self.canvas.create_text(
            20, 110,
            text=f"Hoy: {today}",
            font=("Nunito", 11),
            fill="#666666",
            anchor="nw"
        )
        
        self.canvas.create_rectangle(
            20, 150, 355, 220,
            fill="#ffffff",
            outline="#e0e0e0",
            width=1
        )
        
        self.canvas.create_text(
            40, 165,
            text="Estado de Salud",
            font=("Nunito", 14, "bold"),
            fill="#1565c0",
            anchor="nw"
        )
        
        self.canvas.create_text(
            40, 190,
            text="Presión: 120/80 mmHg • Pulso: 72 bpm",
            font=("Nunito", 10),
            fill="#333333",
            anchor="nw"
        )
    
    def create_dashboard(self):
        menu_items = [
            {
                "title": "Citas Medicas",
                "icon": "📅",
                "y": 250,
                "action": "citas"
            },
            {
                "title": "Medicamentos",
                "icon": "💊",
                "y": 330,
                "action": "medicamentos"
            },
            {
                "title": "Historial Medico",
                "icon": "📋",
                "y": 410,
                "action": "historial"
            },
            {
                "title": "Contactos de Emergencia",
                "icon": "🆘",
                "y": 490,
                "action": "emergencia"
            }
        ]
        
        for item in menu_items:
            button_id = self.canvas.create_rectangle(
                20, item["y"], 355, item["y"] + 60,
                fill="#ffffff",
                outline="#e0e0e0",
                width=1
            )
            
            self.canvas.create_text(
                50, item["y"] + 15,
                text=item["icon"],
                font=("Nunito", 24),
                fill="#1565c0",
                anchor="w"
            )
            
            self.canvas.create_text(
                90, item["y"] + 15,
                text=item["title"],
                font=("Nunito", 14, "bold"),
                fill="#333333",
                anchor="nw"
            )
            
            self.canvas.create_text(
                90, item["y"] + 38,
                text="Tap para ver detalles →",
                font=("Nunito", 9),
                fill="#999999",
                anchor="nw"
            )
            
            self.canvas.tag_bind(button_id, "<Button-1>", lambda e, action=item["action"]: self.on_menu_click(action))
    
    def create_bottom_menu(self):
        self.canvas.create_rectangle(
            0, 740, 375, 812,
            fill="#ffffff",
            outline="#e0e0e0",
            width=1
        )
        
        buttons = [
            {"text": "Inicio", "x": 30, "action": "inicio"},
            {"text": "Perfil", "x": 130, "action": "perfil"},
            {"text": "Configuracion", "x": 250, "action": "config"},
            {"text": "Salir", "x": 320, "action": "logout"}
        ]
        
        for btn in buttons:
            button_id = self.canvas.create_text(
                btn["x"], 770,
                text=btn["text"],
                font=("Nunito", 10, "bold"),
                fill="#1565c0"
            )
            
            self.canvas.tag_bind(button_id, "<Button-1>", lambda e, action=btn["action"]: self.on_bottom_click(action))
    
    def on_menu_click(self, action):
        if action == "citas":
            messagebox.showinfo("Citas Medicas", "Tus proximas citas:\n\n• Dr. Juan Rodriguez\n  Consulta General\n  15/07/2026 - 10:00 AM")
        elif action == "medicamentos":
            messagebox.showinfo("Medicamentos", "Tus medicamentos actuales:\n\n• Aspirina 500mg - 1 vez al dia\n• Vitamina C - 2 veces al dia")
        elif action == "historial":
            messagebox.showinfo("Historial Medico", "Historial reciente:\n\n• Consulta General - 10/06/2026\n• Analisis de sangre - 05/06/2026")
        elif action == "emergencia":
            messagebox.showinfo("Emergencia", "Contactos de emergencia:\n\n• Mama: +505 1234-5678\n• Papa: +505 8765-4321\n• Hospital IMSS: 2222-0000")
    
    def on_bottom_click(self, action):
        if action == "logout":
            if messagebox.askyesno("Confirmar", "¿Deseas cerrar sesion?"):
                self.controller.logged_in_user = None
                self.controller.show_screen("Inicio")
        elif action == "perfil":
            messagebox.showinfo("Perfil", f"Email: {self.controller.logged_in_user}\n\nEditar perfil disponible pronto")
        elif action == "config":
            messagebox.showinfo("Configuracion", "Opciones de configuracion:\n\n• Notificaciones\n• Privacidad\n• Tema")
        elif action == "inicio":
            self.controller.show_screen("Inicio")
