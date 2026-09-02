import tkinter as tk
from tkinter import messagebox
from screens.styles import (VERDE, CELESTE, FUCSIA,
                            AZUL_NOCHE, BLANCO, TEXTO_OSCURO, TEXTO_GRIS,
                            GRADIENT_COLORS, WIDTH, HEIGHT, create_rounded_rect)

class HomeScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg=AZUL_NOCHE)
        self.controller = controller
        self._build_ui()

    def _build_ui(self):
        self.canvas = tk.Canvas(self, width=WIDTH, height=HEIGHT, highlightthickness=0, bg=AZUL_NOCHE)
        self.canvas.pack()
        self._draw_bg()
        self._draw_header()
        self._draw_content()
        self._draw_footer()

    def _greeting(self):
        h = __import__("datetime").datetime.now().hour
        if h < 12: return "Buenos dias"
        if h < 18: return "Buenas tardes"
        return "Buenas noches"

    def _initials(self, name):
        parts = name.strip().split()
        return "".join(p[0].upper() for p in parts[:2])

    def _draw_bg(self):
        colors = GRADIENT_COLORS
        segs = len(colors) - 1
        sh = HEIGHT / segs
        for y in range(0, HEIGHT, 3):
            s = int(y // sh)
            if s >= segs:
                s = segs - 1
            r = (y - s * sh) / sh
            c1, c2 = colors[s], colors[s + 1]
            r1, g1, b1 = int(c1[1:3], 16), int(c1[3:5], 16), int(c1[5:7], 16)
            r2, g2, b2 = int(c2[1:3], 16), int(c2[3:5], 16), int(c2[5:7], 16)
            cr = int(r1 + (r2 - r1) * r)
            cg = int(g1 + (g2 - g1) * r)
            cb = int(b1 + (b2 - b1) * r)
            self.canvas.create_line(0, y, WIDTH, y, fill=f"#{cr:02x}{cg:02x}{cb:02x}")
        self.canvas.create_oval(220, -20, 380, 140, fill=FUCSIA, outline="")
        self.canvas.create_oval(-30, 580, 140, 750, fill=VERDE, outline="")
        self.canvas.create_oval(190, 390, 300, 500, fill=CELESTE, outline="")

    def _draw_header(self):
        nav = tk.Frame(self, bg=BLANCO, bd=0)
        nav.place(relx=0.5, y=28, anchor="center", width=340, height=34)
        back_btn = tk.Label(nav, text="←", font=("Nunito", 18, "bold"), fg="#333333", bg=BLANCO, cursor="hand2")
        back_btn.pack(side="left", padx=8)
        back_btn.bind("<Button-1>", lambda e: self.controller.show_screen("Inicio"))
        tk.Label(nav, text="9:41", font=("Nunito", 14, "bold"), fg="#333333", bg=BLANCO
                 ).pack(side="left", padx=(16, 0))
        tk.Label(nav, text="100%", font=("Nunito", 11), fg=TEXTO_GRIS, bg=BLANCO
                 ).pack(side="right", padx=8)

        card = tk.Frame(self, bg=BLANCO, bd=0)
        card.place(relx=0.5, y=100, anchor="center", width=340, height=130)

        user = self.controller.current_user
        name = user["name"] if user and isinstance(user, dict) else "Usuario"
        tk.Label(card, text=self._greeting(), font=("Nunito", 12), fg=TEXTO_GRIS, bg=BLANCO
                 ).pack(anchor="w", padx=16, pady=(12, 0))
        tk.Label(card, text=name, font=("Nunito", 18, "bold"), fg=AZUL_NOCHE, bg=BLANCO
                 ).pack(anchor="w", padx=16)

        vitals = tk.Frame(card, bg=BLANCO)
        vitals.pack(fill="x", padx=16, pady=(10, 0))
        for val, lbl in [("37C", "TEMP"), ("72", "PULSO"), ("2", "CITAS"), ("22", "MEDIC")]:
            v = tk.Frame(vitals, bg="#F0F8FF", bd=0, width=65, height=50)
            v.pack(side="left", padx=4)
            v.pack_propagate(False)
            tk.Label(v, text=val, font=("Nunito", 12, "bold"), fg=CELESTE, bg="#F0F8FF").pack(pady=(4, 0))
            tk.Label(v, text=lbl, font=("Nunito", 8, "bold"), fg=TEXTO_GRIS, bg="#F0F8FF").pack()

        initials = self._initials(name)
        tk.Label(self, text=initials, font=("Nunito", 14, "bold"), fg=BLANCO, bg=VERDE,
                 width=3, height=1).place(x=310, y=75)

    def _gradient_lines(self, canvas, height):
        colors = GRADIENT_COLORS
        segs = len(colors) - 1
        sh = height / segs
        for y in range(0, height, 3):
            s = int(y // sh)
            if s >= segs:
                s = segs - 1
            r = (y - s * sh) / sh
            c1, c2 = colors[s], colors[s + 1]
            r1, g1, b1 = int(c1[1:3], 16), int(c1[3:5], 16), int(c1[5:7], 16)
            r2, g2, b2 = int(c2[1:3], 16), int(c2[3:5], 16), int(c2[5:7], 16)
            cr = int(r1 + (r2 - r1) * r)
            cg = int(g1 + (g2 - g1) * r)
            cb = int(b1 + (b2 - b1) * r)
            canvas.create_line(0, y, WIDTH, y, fill=f"#{cr:02x}{cg:02x}{cb:02x}")

    def _draw_content(self):
        # Canvas desplazable con gradiente de fondo
        self.scroll = tk.Canvas(self, width=WIDTH, height=530, highlightthickness=0, bg=AZUL_NOCHE)
        self.scroll.place(y=245)
        self._gradient_lines(self.scroll, 900)
        sb = tk.Scrollbar(self, orient="vertical", command=self.scroll.yview)
        sb.place(x=360, y=245, height=530)
        self.scroll.configure(yscrollcommand=sb.set, scrollregion=(0, 0, WIDTH, 900))

        # SERVICIOS PRINCIPALES
        self.scroll.create_text(16, 30, text="SERVICIOS PRINCIPALES", font=("Nunito", 11, "bold"),
                                fill="#BDE0FE", anchor="w")
        self.scroll.create_rectangle(16, 40, 120, 43, fill="#BDE0FE", outline="")

        # Cards de servicios clicables
        serv = [
            ("#1565C0", "Citas Medicas\n2 proximas", "📅", "Citas"),
            ("#0A4D2E", "Medicamentos\n2 tomas hoy", "💊", "Medicamentos"),
            ("#7B1FA2", "Historial Medico\nVer registros", "📋", "Historial"),
            ("#BF360C", "Mi Perfil\nEditar info", "👤", "FormRegistro"),
        ]
        positions = [(20, 60), (190, 60), (20, 162), (190, 162)]
        for (color, text, icon, dest), (x, y) in zip(serv, positions):
            frame = tk.Frame(self.scroll, bg=color)
            self.scroll.create_window(x, y, window=frame, anchor="nw", width=165, height=92)
            tk.Label(frame, text=icon, font=("Nunito", 22), bg=color).pack(anchor="w", padx=12, pady=(10, 0))
            l = tk.Label(frame, text=text, font=("Nunito", 10, "bold"), fg=BLANCO, bg=color,
                         justify="left", padx=12, pady=6, cursor="hand2")
            l.pack(fill="both", expand=True)
            l.bind("<Button-1>", lambda e, d=dest: self.controller.show_screen(d))
            frame.bind("<Button-1>", lambda e, d=dest: self.controller.show_screen(d))

        # PROXIMAS CITAS
        self.scroll.create_text(16, 278, text="PROXIMAS CITAS", font=("Nunito", 11, "bold"),
                                fill="#BDE0FE", anchor="w")
        self.scroll.create_rectangle(16, 288, 120, 291, fill="#BDE0FE", outline="")

        citas = [
            ("15", "JUN", "Dr. Carlos Ruiz", "Medicina General", "10:30 AM", "Hospital Militar EADB", VERDE),
            ("22", "JUN", "Dra. Maria Lopez", "Cardiologia", "2:00 PM", "Hospital Fernando Velez Paiz", CELESTE),
        ]
        cy = 310
        for day, month, doc, spec, time, place, color in citas:
            create_rounded_rect(self.scroll, 20, cy, 20 + 335, cy + 84, 16, fill="#FFFFFF", outline="")
            create_rounded_rect(self.scroll, 30, cy + 14, 30 + 52, cy + 70, 12, fill=color, outline="")
            self.scroll.create_text(56, cy + 42, text=f"{day}\n{month}", font=("Nunito", 9, "bold"),
                                    fill=BLANCO, justify="center")
            self.scroll.create_text(102, cy + 24, text=doc, font=("Nunito", 12, "bold"),
                                    fill=TEXTO_OSCURO, anchor="w")
            self.scroll.create_text(102, cy + 46, text=spec, font=("Nunito", 10),
                                    fill=TEXTO_GRIS, anchor="w")
            self.scroll.create_text(102, cy + 64, text=f"{time} - {place}", font=("Nunito", 9),
                                    fill=color, anchor="w")
            cy += 94

        self.scroll.create_text(187, cy + 50, text="💊  Recuerda tomar tus medicamentos a tiempo",
                                font=("Nunito", 10, "bold"), fill=BLANCO)

    def _draw_footer(self):
        f = tk.Frame(self, bg=BLANCO, bd=0)
        f.place(relx=0.5, y=789, anchor="center", width=375, height=46)
        items = [("🏠\nInicio", "Inicio", False), ("📊\nEstadisticas", "Estadisticas", False), ("👤\nPerfil", "FormRegistro", False), ("🚪\nSalir", None, True)]
        for label, dest, is_exit in items:
            if is_exit:
                cmd = self._confirmar_salir
            else:
                cmd = lambda d=dest: self.controller.show_screen(d)
            b = tk.Label(f, text=label, font=("Nunito", 8), fg=TEXTO_GRIS if "Inicio" not in label else CELESTE,
                         bg=BLANCO, cursor="hand2")
            b.pack(side="left", fill="both", expand=True)
            b.bind("<Button-1>", lambda e, c=cmd: c())

    def _confirmar_salir(self):
        if messagebox.askyesno("Cerrar sesion", "Estas seguro de cerrar sesion?"):
            self.controller.show_screen("Inicio")
