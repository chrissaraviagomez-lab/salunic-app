import tkinter as tk
from tkinter import messagebox
from screens.styles import (VERDE, CELESTE, FUCSIA, ROSADO, AMARILLO, NARANJA,
                            AZUL_NOCHE, BLANCO, TEXTO_OSCURO, TEXTO_GRIS,
                            GRADIENT_COLORS, WIDTH, HEIGHT, create_rounded_rect)

class InicioScreen(tk.Frame):
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
        self.canvas.create_oval(240, -30, 430, 160, fill=FUCSIA, outline="")
        self.canvas.create_oval(-30, 560, 170, 760, fill=VERDE, outline="")
        self.canvas.create_oval(210, 380, 320, 490, fill=CELESTE, outline="")

    def _draw_content(self):
        # Titulo sobre el gradiente
        self.canvas.create_text(187, 110, text="Bienvenido a", font=("Nunito", 14), fill=BLANCO)
        self.canvas.create_text(187, 148, text="SALUNIC", font=("Nunito", 34, "bold"), fill=BLANCO)

        # Card redondeada con gradiente alrededor
        card_x, card_y, card_w, card_h = 28, 205, 319, 500
        create_rounded_rect(self.canvas, card_x, card_y, card_x + card_w, card_y + card_h,
                            20, fill="#FFFFFF", outline="")

        # Divider de colores
        dot_y = card_y + 78
        for i, color in enumerate([VERDE, CELESTE, AMARILLO, FUCSIA, NARANJA]):
            dw, dgap = 26, 6
            dtotal = 5 * dw + 4 * dgap
            dx = card_x + (card_w - dtotal) / 2 + i * (dw + dgap)
            create_rounded_rect(self.canvas, dx, dot_y, dx + dw, dot_y + 5, 2, fill=color, outline="")

        # Feature boxes redondeados dentro de la card
        feat_y = card_y + 108
        icons = [("💊", "Medicamentos", "#1565C0"),
                 ("📅", "Citas", "#0A4D2E"),
                 ("📋", "Historial", "#7B1FA2")]
        box_w, box_h, gap = 95, 92, 8
        total = 3 * box_w + 2 * gap
        x0 = card_x + (card_w - total) / 2
        for i, (icon, text, color) in enumerate(icons):
            bx = x0 + i * (box_w + gap)
            create_rounded_rect(self.canvas, bx, feat_y, bx + box_w, feat_y + box_h, 14, fill="#F5F5F5", outline="")
            self.canvas.create_text(bx + box_w / 2, feat_y + 26, text=icon, font=("Nunito", 24))
            self.canvas.create_text(bx + box_w / 2, feat_y + box_h - 22, text=text,
                                    font=("Nunito", 9, "bold"), fill=TEXTO_OSCURO)

        # Texto descriptivo
        self.canvas.create_text(187, feat_y + box_h + 34,
                                text="Tu plataforma de salud y bienestar",
                                font=("Nunito", 11), fill=TEXTO_GRIS)

        # Boton COMENZAR
        b1_y = feat_y + box_h + 60
        create_rounded_rect(self.canvas, card_x + 44, b1_y, card_x + card_w - 44, b1_y + 48, 24, fill=VERDE, outline="")
        btn1 = tk.Label(self, text="COMENZAR", font=("Nunito", 14, "bold"), fg=BLANCO, bg=VERDE, cursor="hand2")
        btn1.place(x=card_x + 46, y=b1_y + 2, width=card_w - 92, height=44)
        btn1.bind("<Button-1>", lambda e: self.controller.show_screen("Login"))

        # Boton INICIAR SESION
        b2_y = b1_y + 60
        create_rounded_rect(self.canvas, card_x + 44, b2_y, card_x + card_w - 44, b2_y + 44, 22, fill=CELESTE, outline="")
        btn2 = tk.Label(self, text="INICIAR SESION", font=("Nunito", 12, "bold"), fg=BLANCO, bg=CELESTE, cursor="hand2")
        btn2.place(x=card_x + 46, y=b2_y + 2, width=card_w - 92, height=40)
        btn2.bind("<Button-1>", lambda e: self.controller.show_screen("Login"))

        # Login hint
        hint_y = b2_y + 58
        hint = tk.Label(self, text="Ya tienes cuenta? Ingresa aqui", font=("Nunito", 10),
                        fg=ROSADO, bg="#FFFFFF", cursor="hand2")
        hint.place(x=card_x, y=hint_y, width=card_w, height=24)
        hint.bind("<Button-1>", lambda e: self.controller.show_screen("Login"))

        # Boton salir (sobre gradiente, dentro del alcance de la card inferior)
        exit_y = card_y + card_h + 26
        create_rounded_rect(self.canvas, 88, exit_y, 288, exit_y + 40, 20, fill="#152B46", outline="")
        btn_exit = tk.Label(self, text="Salir de la aplicacion", font=("Nunito", 10),
                            fg="#FF8FA3", bg="#152B46", cursor="hand2")
        btn_exit.place(x=90, y=exit_y + 2, width=196, height=36)
        btn_exit.bind("<Button-1>", lambda e: self._salir())

    def _salir(self):
        if messagebox.askyesno("Salir", "Estas seguro de que deseas salir de SALUNIC?"):
            self.controller.quit()
            self.controller.destroy()
