import tkinter as tk
from tkinter import font as tkFont

class HomeScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#ffffff")
        self.controller = controller
        self.create_widgets()
    
    def create_widgets(self):
        # Encabezado azul con hora y bienvenida
        header = tk.Frame(self, bg="#1565c0", height=180)
        header.pack(fill="x", padx=0, pady=0)
        header.pack_propagate(False)
        
        # Hora y porcentaje
        top_bar = tk.Frame(header, bg="#1565c0")
        top_bar.pack(fill="x", padx=15, pady=(15, 0))
        
        time_label = tk.Label(
            top_bar,
            text="9:41",
            font=("Nunito", 18, "bold"),
            fg="#ffffff",
            bg="#1565c0"
        )
        time_label.pack(side="left")
        
        battery_label = tk.Label(
            top_bar,
            text="100%",
            font=("Nunito", 14, "bold"),
            fg="#ffffff",
            bg="#1565c0"
        )
        battery_label.pack(side="right")
        
        # Saludos
        greeting_frame = tk.Frame(header, bg="#1565c0")
        greeting_frame.pack(fill="x", padx=15, pady=(15, 5))
        
        hello_label = tk.Label(
            greeting_frame,
            text="Buenos días",
            font=("Nunito", 14),
            fg="#ffffff",
            bg="#1565c0"
        )
        hello_label.pack(anchor="w")
        
        name_label = tk.Label(
            greeting_frame,
            text="María González",
            font=("Nunito", 20, "bold"),
            fg="#ffffff",
            bg="#1565c0"
        )
        name_label.pack(anchor="w")
        
        # Datos vitales
        vitals_frame = tk.Frame(header, bg="#1565c0")
        vitals_frame.pack(fill="x", padx=15, pady=(10, 15))
        
        vitals = [
            ("37C", "TEMP"),
            ("72", "PULSO"),
            ("2", "CITAS"),
            ("22", "MEDIC")
        ]
        
        for value, label in vitals:
            vital = tk.Frame(vitals_frame, bg="#1565c0")
            vital.pack(side="left", padx=8)
            
            val_label = tk.Label(
                vital,
                text=value,
                font=("Nunito", 14, "bold"),
                fg="#ffffff",
                bg="#1565c0"
            )
            val_label.pack()
            
            txt_label = tk.Label(
                vital,
                text=label,
                font=("Nunito", 9),
                fg="#b0bec5",
                bg="#1565c0"
            )
            txt_label.pack()
        
        # Avatar
        avatar = tk.Label(
            header,
            text="MG",
            font=("Nunito", 16, "bold"),
            fg="#ffffff",
            bg="#4caf50",
            width=3,
            height=1,
            relief="solid",
            bd=2
        )
        header.create_window(340, 50, window=avatar)
        
        # Contenido principal scrollable
        self.canvas = tk.Canvas(self, bg="#ffffff", highlightthickness=0)
        scrollbar = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        scrollable_frame = tk.Frame(self.canvas, bg="#ffffff")
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )
        
        self.canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=scrollbar.set)
        
        self.canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Sección de servicios
        services_title = tk.Label(
            scrollable_frame,
            text="SERVICIOS PRINCIPALES",
            font=("Nunito", 11, "bold"),
            fg="#9e9e9e",
            bg="#ffffff"
        )
        services_title.pack(anchor="w", padx=15, pady=(20, 10))
        
        # Tarjetas de servicios
        cards_frame = tk.Frame(scrollable_frame, bg="#ffffff")
        cards_frame.pack(fill="x", padx=10, pady=5)
        
        # Fila 1: Citas Médicas y Medicamentos
        row1 = tk.Frame(cards_frame, bg="#ffffff")
        row1.pack(fill="x", padx=5, pady=5)
        
        self.create_service_card(
            row1,
            "Citas Medicas\n2 proximas citas",
            "#ff7f7f",
            side="left"
        )
        
        self.create_service_card(
            row1,
            "Medicamentos\n2 tomas hoy",
            "#4db8ac",
            side="left"
        )
        
        # Fila 2: Historial Médico y Mi Perfil
        row2 = tk.Frame(cards_frame, bg="#ffffff")
        row2.pack(fill="x", padx=5, pady=5)
        
        self.create_service_card(
            row2,
            "Historial Medico\nVer registros",
            "#80deea",
            side="left"
        )
        
        self.create_service_card(
            row2,
            "Mi Perfil\nEditar info",
            "#ffeb99",
            side="left"
        )
        
        # Sección de próximas citas
        appointments_title = tk.Label(
            scrollable_frame,
            text="PRÓXIMAS CITAS",
            font=("Nunito", 11, "bold"),
            fg="#9e9e9e",
            bg="#ffffff"
        )
        appointments_title.pack(anchor="w", padx=15, pady=(20, 10))
        
        # Tarjeta de cita
        appointment = tk.Frame(scrollable_frame, bg="#f5f5f5", relief="flat", bd=1)
        appointment.pack(fill="x", padx=15, pady=5)
        
        # Número de día
        day_circle = tk.Label(
            appointment,
            text="15\nJUN",
            font=("Nunito", 12, "bold"),
            fg="#ffffff",
            bg="#4caf50",
            width=6,
            height=3,
            relief="solid",
            bd=1
        )
        day_circle.pack(side="left", padx=10, pady=10)
        
        # Detalles de la cita
        details = tk.Frame(appointment, bg="#f5f5f5")
        details.pack(side="left", fill="both", expand=True, padx=10, pady=10)
        
        doctor_label = tk.Label(
            details,
            text="Dr. Carlos Ruiz",
            font=("Nunito", 12, "bold"),
            fg="#333333",
            bg="#f5f5f5"
        )
        doctor_label.pack(anchor="w")
        
        specialty_label = tk.Label(
            details,
            text="Medicina General",
            font=("Nunito", 10),
            fg="#9e9e9e",
            bg="#f5f5f5"
        )
        specialty_label.pack(anchor="w")
        
        time_label = tk.Label(
            details,
            text="10:30 AM - Hospital Militar",
            font=("Nunito", 9),
            fg="#2196f3",
            bg="#f5f5f5"
        )
        time_label.pack(anchor="w")
        
        # Espacio al final
        tk.Frame(scrollable_frame, bg="#ffffff", height=20).pack()
        
        # Menú inferior
        footer = tk.Frame(self, bg="#1565c0", height=70)
        footer.pack(fill="x", side="bottom")
        footer.pack_propagate(False)
        
        # Botones del menú
        menu_items = [
            ("🏠", "Inicio"),
            ("📊", "Estadísticas"),
            ("👤", "Perfil"),
            ("🚪", "Salir")
        ]
        
        for icon, label in menu_items:
            if label == "Salir":
                btn = tk.Button(
                    footer,
                    text=f"{icon}\n{label}",
                    font=("Nunito", 9),
                    bg="#e74c3c",
                    fg="#ffffff",
                    relief="flat",
                    command=lambda: self.controller.show_screen("Inicio")
                )
            else:
                btn = tk.Button(
                    footer,
                    text=f"{icon}\n{label}",
                    font=("Nunito", 9),
                    bg="#1565c0",
                    fg="#ffffff",
                    relief="flat"
                )
            
            btn.pack(side="left", fill="both", expand=True)
    
    def create_service_card(self, parent, text, color, side="left"):
        card = tk.Frame(parent, bg=color, relief="flat", bd=0)
        card.pack(side=side, fill="both", expand=True, padx=5, pady=5)
        
        label = tk.Label(
            card,
            text=text,
            font=("Nunito", 11, "bold"),
            fg="#ffffff",
            bg=color,
            justify="left",
            padx=15,
            pady=20
        )
        label.pack(fill="both", expand=True)
