import tkinter as tk
from screens.styles import (VERDE, CELESTE, FUCSIA, AMARILLO, AZUL_NOCHE, BLANCO,
                            TEXTO_OSCURO, TEXTO_GRIS, GRADIENT_COLORS, WIDTH, HEIGHT,
                            create_rounded_rect)

class CitasScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg=AZUL_NOCHE)
        self.controller = controller
        self._build_ui()

    def _build_ui(self):
        self.canvas = tk.Canvas(self, width=WIDTH, height=HEIGHT, highlightthickness=0, bg=AZUL_NOCHE)
        self.canvas.pack()
        self._draw_bg()
        self._draw_content()

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
        # Blobs decorativos
        self.canvas.create_oval(210, -30, 390, 150, fill=FUCSIA, outline="")
        self.canvas.create_oval(-40, 560, 170, 770, fill=VERDE, outline="")

    def _rounded_card(self, x, y, w, h, fill, r=16):
        create_rounded_rect(self.canvas, x, y, x + w, y + h, r, fill=fill, outline="")

    def _draw_content(self):
        # Nav bar
        nav = tk.Frame(self, bg=BLANCO, bd=0)
        nav.place(relx=0.5, y=28, anchor="center", width=340, height=34)
        back_btn = tk.Label(nav, text="←", font=("Nunito", 18, "bold"), fg="#333333", bg=BLANCO, cursor="hand2")
        back_btn.pack(side="left", padx=8)
        back_btn.bind("<Button-1>", lambda e: self.controller.show_screen("Home"))
        tk.Label(nav, text="Citas", font=("Nunito", 12, "bold"), fg="#333333", bg=BLANCO
                 ).pack(side="left", padx=(16, 0))
        tk.Label(nav, text="100%", font=("Nunito", 11), fg=TEXTO_GRIS, bg=BLANCO
                 ).pack(side="right", padx=8)

        # Titulo sobre el gradiente
        self.canvas.create_text(187, 120, text="Citas Medicas", font=("Nunito", 22, "bold"), fill=BLANCO)
        self.canvas.create_text(187, 148, text="Tus proximas citas agendadas", font=("Nunito", 11), fill=BLANCO)

        citas = [
            ("15", "JUN", "Dr. Carlos Ruiz", "Medicina General", "10:30 AM", "Hospital Militar EADB", VERDE),
            ("22", "JUN", "Dra. Maria Lopez", "Cardiologia", "2:00 PM", "Hospital Fernando Velez Paiz", CELESTE),
            ("05", "JUL", "Dr. Pedro Martinez", "Dermatologia", "9:00 AM", "Hospital Bautista", AMARILLO),
        ]

        cy = 185
        for dia, mes, doctor, espec, hora, lugar, color in citas:
            # Card redondeada
            create_rounded_rect(self.canvas, 18, cy, 18 + 340, cy + 78, 16, fill="#FFFFFF", outline="")
            # Fecha (cuadro de color)
            create_rounded_rect(self.canvas, 28, cy + 14, 28 + 52, cy + 64, 12, fill=color, outline="")
            self.canvas.create_text(54, cy + 39, text=f"{dia}\n{mes}", font=("Nunito", 10, "bold"),
                                    fill=BLANCO, justify="center")
            # Info
            self.canvas.create_text(100, cy + 22, text=doctor, font=("Nunito", 12, "bold"),
                                    fill=TEXTO_OSCURO, anchor="w")
            self.canvas.create_text(100, cy + 42, text=espec, font=("Nunito", 10),
                                    fill=TEXTO_GRIS, anchor="w")
            self.canvas.create_text(100, cy + 60, text=f"{hora} - {lugar}", font=("Nunito", 9),
                                    fill=color, anchor="w")
            cy += 90

        # Boton VOLVER AL INICIO (label clicable sobre rounded rect)
        btn_y = cy + 12
        create_rounded_rect(self.canvas, 18, btn_y, 18 + 340, btn_y + 46, 23, fill=CELESTE, outline="")
        btn = tk.Label(self, text="VOLVER AL INICIO", font=("Nunito", 13, "bold"),
                       fg=BLANCO, bg=CELESTE, cursor="hand2")
        btn.place(x=20, y=btn_y + 2, width=336, height=42)
        btn.bind("<Button-1>", lambda e: self.controller.show_screen("Home"))
