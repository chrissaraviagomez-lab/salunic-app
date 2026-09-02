import tkinter as tk
from screens.styles import (VERDE, CELESTE, FUCSIA, AMARILLO, AZUL_NOCHE, BLANCO,
                            TEXTO_OSCURO, TEXTO_GRIS, GRADIENT_COLORS, WIDTH, HEIGHT,
                            create_rounded_rect)

class EstadisticasScreen(tk.Frame):
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
        self.canvas.create_oval(230, -30, 390, 150, fill=FUCSIA, outline="")
        self.canvas.create_oval(-40, 580, 160, 770, fill=VERDE, outline="")

    def _draw_content(self):
        nav = tk.Frame(self, bg=BLANCO, bd=0)
        nav.place(relx=0.5, y=28, anchor="center", width=340, height=34)
        back_btn = tk.Label(nav, text="←", font=("Nunito", 18, "bold"), fg="#333333", bg=BLANCO, cursor="hand2")
        back_btn.pack(side="left", padx=8)
        back_btn.bind("<Button-1>", lambda e: self.controller.show_screen("Home"))
        tk.Label(nav, text="Estadisticas", font=("Nunito", 12, "bold"), fg="#333333", bg=BLANCO
                 ).pack(side="left", padx=(16, 0))
        tk.Label(nav, text="100%", font=("Nunito", 11), fg=TEXTO_GRIS, bg=BLANCO
                 ).pack(side="right", padx=8)

        self.canvas.create_text(187, 120, text="Estadisticas de Salud", font=("Nunito", 22, "bold"), fill=BLANCO)
        self.canvas.create_text(187, 148, text="Resumen de tu estado de salud", font=("Nunito", 11), fill=BLANCO)

        stats = [
            ("37C", "TEMPERATURA", "Temperatura corporal actual", VERDE),
            ("72", "PULSO", "Latidos por minuto", CELESTE),
            ("120/80", "PRESION", "Presion arterial (mmHg)", FUCSIA),
            ("2", "CITAS", "Citas pendientes este mes", AMARILLO),
        ]
        cy = 185
        for valor, titulo, desc, color in stats:
            create_rounded_rect(self.canvas, 18, cy, 18 + 340, cy + 90, 16, fill="#FFFFFF", outline="")
            create_rounded_rect(self.canvas, 28, cy + 14, 28 + 70, cy + 76, 16, fill=color, outline="")
            self.canvas.create_text(63, cy + 45, text=valor, font=("Nunito", 14, "bold"),
                                    fill=BLANCO, justify="center")
            self.canvas.create_text(120, cy + 28, text=titulo, font=("Nunito", 12, "bold"),
                                    fill=TEXTO_OSCURO, anchor="w")
            self.canvas.create_text(120, cy + 56, text=desc, font=("Nunito", 10),
                                    fill=TEXTO_GRIS, anchor="w")
            cy += 104

        create_rounded_rect(self.canvas, 18, cy, 18 + 340, cy + 46, 23, fill=CELESTE, outline="")
        btn = tk.Label(self, text="VOLVER AL INICIO", font=("Nunito", 13, "bold"),
                       fg=BLANCO, bg=CELESTE, cursor="hand2")
        btn.place(x=20, y=cy + 2, width=336, height=42)
        btn.bind("<Button-1>", lambda e: self.controller.show_screen("Home"))