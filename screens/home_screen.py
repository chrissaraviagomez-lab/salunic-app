import tkinter as tk

class HomeScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#f5f5f5")
        self.controller = controller
        self.create_widgets()
    
    def create_widgets(self):
        # Encabezado
        header = tk.Frame(self, bg="#1565c0", height=100)
        header.pack(fill="x")
        
        user_label = tk.Label(
            header,
            text=f"Hola, {self.controller.logged_in_user}",
            font=("Nunito", 16, "bold"),
            fg="#ffffff",
            bg="#1565c0"
        )
        user_label.pack(pady=20)
        
        welcome = tk.Label(
            header,
            text="Panel de Control",
            font=("Nunito", 12),
            fg="#e0e0e0",
            bg="#1565c0"
        )
        welcome.pack()
        
        # Contenido principal
        content = tk.Frame(self, bg="#f5f5f5")
        content.pack(fill="both", expand=True, padx=15, pady=20)
        
        # Tarjetas de información
        self.create_card(
            content,
            "❤️ Salud General",
            "Estado: Excelente",
            0, 0
        )
        
        self.create_card(
            content,
            "🏃 Actividad",
            "Hoy: 8,234 pasos",
            0, 1
        )
        
        self.create_card(
            content,
            "😴 Descanso",
            "Anoche: 7.5 horas",
            1, 0
        )
        
        self.create_card(
            content,
            "🍎 Nutrición",
            "Bien balanceado",
            1, 1
        )
        
        # Menú inferior
        footer = tk.Frame(self, bg="#1565c0", height=60)
        footer.pack(fill="x", side="bottom")
        
        btn_home = tk.Button(
            footer,
            text="🏠 Inicio",
            font=("Nunito", 10),
            bg="#1565c0",
            fg="#ffffff",
            relief="flat"
        )
        btn_home.pack(side="left", fill="both", expand=True, padx=5, pady=10)
        
        btn_stats = tk.Button(
            footer,
            text="📊 Estadísticas",
            font=("Nunito", 10),
            bg="#1565c0",
            fg="#ffffff",
            relief="flat"
        )
        btn_stats.pack(side="left", fill="both", expand=True, padx=5, pady=10)
        
        btn_profile = tk.Button(
            footer,
            text="👤 Perfil",
            font=("Nunito", 10),
            bg="#1565c0",
            fg="#ffffff",
            relief="flat"
        )
        btn_profile.pack(side="left", fill="both", expand=True, padx=5, pady=10)
        
        btn_logout = tk.Button(
            footer,
            text="🚪 Salir",
            font=("Nunito", 10),
            bg="#e74c3c",
            fg="#ffffff",
            relief="flat",
            command=lambda: self.controller.show_screen("Inicio")
        )
        btn_logout.pack(side="left", fill="both", expand=True, padx=5, pady=10)
    
    def create_card(self, parent, title, subtitle, row, col):
        card = tk.Frame(parent, bg="#ffffff", relief="flat", bd=1)
        card.grid(row=row, column=col, padx=7, pady=7, sticky="nsew")
        
        parent.grid_rowconfigure(row, weight=1)
        parent.grid_columnconfigure(col, weight=1)
        
        title_label = tk.Label(
            card,
            text=title,
            font=("Nunito", 12, "bold"),
            fg="#1565c0",
            bg="#ffffff"
        )
        title_label.pack(pady=(10, 5))
        
        subtitle_label = tk.Label(
            card,
            text=subtitle,
            font=("Nunito", 10),
            fg="#666666",
            bg="#ffffff"
        )
        subtitle_label.pack(pady=(0, 10))
