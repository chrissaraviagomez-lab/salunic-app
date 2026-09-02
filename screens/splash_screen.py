import tkinter as tk
import math
from screens.styles import CELESTE, AZUL_NOCHE, BLANCO, GRADIENT_COLORS, WIDTH, HEIGHT

class SplashScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg=AZUL_NOCHE)
        self.controller = controller
        self.angle = 0
        self.canvas = tk.Canvas(self, width=WIDTH, height=HEIGHT, highlightthickness=0, bg=AZUL_NOCHE)
        self.canvas.pack()
        self._draw_bg()
        self._draw_navbar()
        self._draw_rings()
        self.after(50, self._animate)

    def _draw_bg(self):
        colors = GRADIENT_COLORS
        segments = len(colors) - 1
        seg_h = HEIGHT / segments
        for y in range(0, HEIGHT, 3):
            seg = int(y // seg_h)
            if seg >= segments:
                seg = segments - 1
            r = (y - seg * seg_h) / seg_h
            c1, c2 = colors[seg], colors[seg + 1]
            r1, g1, b1 = int(c1[1:3], 16), int(c1[3:5], 16), int(c1[5:7], 16)
            r2, g2, b2 = int(c2[1:3], 16), int(c2[3:5], 16), int(c2[5:7], 16)
            cr = int(r1 + (r2 - r1) * r)
            cg = int(g1 + (g2 - g1) * r)
            cb = int(b1 + (b2 - b1) * r)
            self.canvas.create_line(0, y, WIDTH, y, fill=f"#{cr:02x}{cg:02x}{cb:02x}")
        self.canvas.create_oval(240, -20, 420, 160, fill="#E91E8C", outline="")
        self.canvas.create_oval(-40, 580, 160, 780, fill="#2ECC71", outline="")
        self.canvas.create_oval(200, 380, 320, 500, fill="#4FC3F7", outline="")

    def _draw_navbar(self):
        self.canvas.create_text(20, 18, text="9:41", font=("Nunito", 12, "bold"), fill=BLANCO, anchor="w")

    def _draw_rings(self):
        glow = self.canvas.create_oval(107, 257, 267, 417, fill="", outline=CELESTE, width=0)
        self.canvas.create_oval(147, 297, 227, 377, fill=BLANCO, outline="")
        self.canvas.create_text(187, 337, text="S", font=("Nunito", 48, "bold"), fill=AZUL_NOCHE)
        self.ring1 = self.canvas.create_oval(137, 287, 237, 387, fill="", outline=BLANCO, width=2, dash=(4, 8))
        self.ring2 = self.canvas.create_oval(127, 277, 247, 397, fill="", outline=BLANCO, width=1, dash=(2, 6))
        self.canvas.create_text(187, 440, text="SALUNIC", font=("Nunito", 36, "bold"), fill=BLANCO)
        self.canvas.create_text(187, 480, text="Salud y Bienestar • Nicaragua", font=("Nunito", 11, "bold"), fill=BLANCO)
        pills = [("Salud", "#2ECC71"), ("Bienestar", "#4FC3F7"), ("Esperanza", "#F9A825")]
        px = 187 - ((len(pills) * 70 + (len(pills) - 1) * 8) // 2)
        for ptext, pcolor in pills:
            self.canvas.create_rectangle(px, 508, px + 70, 526, fill=pcolor, outline="")
            self.canvas.create_text(px + 35, 517, text=ptext, font=("Nunito", 9, "bold"), fill=BLANCO)
            px += 78

    def _animate(self):
        self.angle += 4
        if self.angle >= 360:
            self.angle = 0
            self.after(1500, lambda: self.controller.show_screen("Inicio"))
            return
        center_x, center_y = 187, 337
        for ring_id, radius in [(self.ring1, 50), (self.ring2, 60)]:
            rad = math.radians(self.angle)
            dx = radius * math.cos(rad)
            dy = radius * math.sin(rad)
            self.canvas.coords(ring_id, center_x - 50 + dx, center_y - 50 + dy, center_x + 50 + dx, center_y + 50 + dy)
        self.after(50, self._animate)
