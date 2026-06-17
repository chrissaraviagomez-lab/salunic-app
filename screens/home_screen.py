import tkinter as tk
from tkinter import Canvas

class HomeScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#f4f6fb")
        self.controller = controller
        
        self.canvas = Canvas(
            self,
            width=375,
            height=812,
            bg="#f4f6fb",
            highlightthickness=0
        )
        self.canvas.pack()
        
        self.create_header()
        self.create_health_stats()
        self.create_services()
        self.create_upcoming_appointments()
        self.create_today_medications()
        self.create_bottom_navigation()
    
    def create_header(self):
        self.canvas.create_rectangle(
            0, 0, 375, 181,
            fill="#1565c0",
            outline=""
        )
        
        self.canvas.create_text(
            22, 30,
            text="9:41",
            font=("Nunito", 12, "bold"),
            fill="#dce8f6",
            anchor="w"
        )
        
        self.canvas.create_text(
            345, 32,
            text="100%",
            font=("Nunito", 12, "bold"),
            fill="#dce8f6",
            anchor="e"
        )
        
        self.canvas.create_text(
            22, 63,
            text="Buenos días",
            font=("Nunito", 13, "bold"),
            fill="#a9cae8",
            anchor="nw"
        )
        
        self.canvas.create_text(
            22, 88,
            text="María González",
            font=("Nunito", 20, "bold"),
            fill="#ffffff",
            anchor="nw"
        )
        
        self.canvas.create_oval(
            307, 43, 353, 89,
            fill="#2ecc71",
            outline=""
        )
        
        self.canvas.create_text(
            330, 66,
            text="MG",
            font=("Nunito", 16, "bold"),
            fill="#ffffff"
        )
    
    def create_health_stats(self):
        self.canvas.create_rectangle(
            18, 102, 357, 167,
            fill="#3379c8",
            outline="",
            width=0
        )
        
        self.canvas.create_text(
            46, 122,
            text="37°C",
            font=("Nunito", 14, "bold"),
            fill="#ffffff"
        )
        
        self.canvas.create_text(
            46, 150,
            text="TEMP",
            font=("Nunito", 9, "bold"),
            fill="#a9cae8"
        )
        
        self.canvas.create_line(
            85.26, 130.5, 85.26, 164.5,
            fill="#5a93d1",
            width=1
        )
        
        self.canvas.create_text(
            128, 122,
            text="72",
            font=("Nunito", 14, "bold"),
            fill="#ffffff"
        )
        
        self.canvas.create_text(
            128, 150,
            text="PULSO",
            font=("Nunito", 9, "bold"),
            fill="#a9cae8"
        )
        
        self.canvas.create_line(
            169.13, 130.5, 169.13, 164.5,
            fill="#5a93d1",
            width=1
        )
        
        self.canvas.create_text(
            209, 122,
            text="2",
            font=("Nunito", 14, "bold"),
            fill="#ffffff"
        )
        
        self.canvas.create_text(
            209, 150,
            text="CITAS",
            font=("Nunito", 9, "bold"),
            fill="#a9cae8"
        )
        
        self.canvas.create_line(
            248.66, 130.5, 248.66, 164.5,
            fill="#5a93d1",
            width=1
        )
        
        self.canvas.create_text(
            298, 122,
            text="22",
            font=("Nunito", 14, "bold"),
            fill="#ffffff"
        )
        
        self.canvas.create_text(
            298, 150,
            text="MEDIC",
            font=("Nunito", 9, "bold"),
            fill="#a9cae8"
        )
    
    def create_services(self):
        self.canvas.create_text(
            18, 200,
            text="SERVICIOS PRINCIPALES",
            font=("Nunito", 10.5, "bold"),
            fill="#9aa0b2",
            anchor="nw"
        )
        
        services = [
            (18, 226, "📅", "Citas Médicas", "2 próximas citas", "#FF6B6B", "#ffd0d0"),
            (193.5, 226, "💊", "Medicamentos", "2 tomas hoy", "#4ECDC4", "#c6efec"),
            (18, 379.8, "📋", "Historial Médico", "Ver registros", "#95E1D3", "#ddf5f1"),
            (193.5, 379.8, "👤", "Mi Perfil", "Editar datos", "#F7DC6F", "#fcf4d1"),
        ]
        
        for x, y, icon, title, subtitle, color, subtitle_color in services:
            self.canvas.create_rectangle(
                x, y, x + 163.5, y + 121.8,
                fill=color,
                outline="",
                width=0
            )
            
            self.canvas.create_text(
                x + 14, y + 18,
                text=icon,
                font=("Arial", 28),
                fill="#000000",
                anchor="nw"
            )
            
            self.canvas.create_text(
                x + 14, y + 64,
                text=title,
                font=("Nunito", 14, "bold"),
                fill="#ffffff",
                anchor="nw"
            )
            
            self.canvas.create_text(
                x + 14, y + 88.8,
                text=subtitle,
                font=("Nunito", 11, "bold"),
                fill=subtitle_color,
                anchor="nw"
            )
    
    def create_upcoming_appointments(self):
        self.canvas.create_text(
            18, 535,
            text="PRÓXIMAS CITAS",
            font=("Nunito", 10.5, "bold"),
            fill="#9aa0b2",
            anchor="nw"
        )
        
        appointments = [
            (561, "15", "JUN", "Dr. Carlos Ruiz", "Medicina General", "10:30 AM - Hospital Militar"),
            (650, "22", "JUN", "Dra. Ana López", "Cardiología", "2:00 PM - Hospital Militar"),
        ]
        
        for y, day, month, doctor, specialty, time in appointments:
            self.canvas.create_rectangle(
                18, y, 357, y + 79,
                fill="#ffffff",
                outline="",
                width=0
            )
            
            self.canvas.create_oval(
                33, y + 16.5, 79, y + 62.5,
                fill="#2ecc71",
                outline=""
            )
            
            self.canvas.create_text(
                56, y + 32,
                text=day,
                font=("Nunito", 16, "bold"),
                fill="#ffffff"
            )
            
            self.canvas.create_text(
                56, y + 47,
                text=month,
                font=("Nunito", 9, "bold"),
                fill="#cef1dd"
            )
            
            self.canvas.create_text(
                88, y + 23,
                text=doctor,
                font=("Nunito", 13, "bold"),
                fill="#1a1a2e",
                anchor="nw"
            )
            
            self.canvas.create_text(
                88, y + 43,
                text=specialty,
                font=("Nunito", 11),
                fill="#9aa0b2",
                anchor="nw"
            )
            
            self.canvas.create_text(
                88, y + 61,
                text=time,
                font=("Nunito", 11, "bold"),
                fill="#4fc3f7",
                anchor="nw"
            )
            
            self.canvas.create_text(
                324, y + 41,
                text=">",
                font=("Nunito", 20),
                fill="#dddddd"
            )
    
    def create_today_medications(self):
        self.canvas.create_text(
            18, 739,
            text="MEDICAMENTOS DE HOY",
            font=("Nunito", 10.5, "bold"),
            fill="#9aa0b2",
            anchor="nw"
        )
        
        self.canvas.create_rectangle(
            18, 765, 357, 829,
            fill="#ffffff",
            outline="",
            width=0
        )
        
        self.canvas.create_oval(
            32, 776, 74, 818,
            fill="#eafaf1",
            outline=""
        )
        
        self.canvas.create_text(
            53, 783.5,
            text="💊",
            font=("Arial", 20),
            fill="#000000"
        )
        
        self.canvas.create_text(
            81, 780.5,
            text="Metformina 500mg",
            font=("Nunito", 13, "bold"),
            fill="#1a1a2e",
            anchor="nw"
        )
        
        self.canvas.create_text(
            81, 800.5,
            text="1 tableta con desayuno",
            font=("Nunito", 11),
            fill="#9aa0b2",
            anchor="nw"
        )
        
        self.canvas.create_rectangle(
            281.75, 786.5, 342.98, 807.5,
            fill="#eafaf1",
            outline="",
            width=0
        )
        
        self.canvas.create_text(
            311.87, 797,
            text="8:00 AM",
            font=("Nunito", 11, "bold"),
            fill="#2ecc71",
            anchor="center"
        )
    
    def create_bottom_navigation(self):
        self.canvas.create_rectangle(
            0, 738, 375, 812,
            fill="#ffffff",
            outline="",
            width=0
        )
        
        nav_items = [
            (39, "🏠", "INICIO", "#1565c0", True),
            (108, "📅", "CITAS", "#bbbbbb", False),
            (179, "💊", "MEDIC", "#bbbbbb", False),
            (259, "📋", "HISTORIAL", "#bbbbbb", False),
            (337, "👤", "PERFIL", "#bbbbbb", False),
        ]
        
        for x, icon, label, color, is_active in nav_items:
            self.canvas.create_text(
                x, 750,
                text=icon,
                font=("Arial", 22),
                fill="#000000"
            )
            
            self.canvas.create_text(
                x, 788.5 if is_active else 793,
                text=label,
                font=("Nunito", 9, "bold"),
                fill=color
            )
            
            if is_active:
                self.canvas.create_oval(
                    x - 2.5, 809, x + 2.5, 814,
                    fill=color,
                    outline=""
                )
