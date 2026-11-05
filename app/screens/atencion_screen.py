import tkinter as tk
from tkinter import messagebox
import sys
import os
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if ROOT_DIR not in sys.path:
    sys.path.append(ROOT_DIR)

from Funciones import sistema
from screens.styles import (VERDE, CELESTE, FUCSIA, AMARILLO, NARANJA, AZUL_NOCHE, BLANCO,
                            TEXTO_OSCURO, TEXTO_GRIS, GRADIENT_COLORS, WIDTH, HEIGHT,
                            create_rounded_rect)


class AtencionScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg=AZUL_NOCHE)
        self.controller = controller
        self.en_atencion = None
        self._build_ui()

    def _build_ui(self):
        for widget in self.winfo_children():
            widget.destroy()
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
        self.canvas.create_oval(210, -30, 390, 150, fill=FUCSIA, outline="")
        self.canvas.create_oval(-40, 560, 170, 770, fill=VERDE, outline="")
        self.canvas.create_oval(190, 400, 300, 510, fill=CELESTE, outline="")

    def _draw_content(self):
        nav = tk.Frame(self, bg=BLANCO, bd=0)
        nav.place(relx=0.5, y=28, anchor="center", width=340, height=34)
        back_btn = tk.Label(nav, text="←", font=("Nunito", 18, "bold"), fg="#333333", bg=BLANCO, cursor="hand2")
        back_btn.pack(side="left", padx=8)
        back_btn.bind("<Button-1>", lambda e: self.controller.show_screen("Home"))
        tk.Label(nav, text="Panel de Atención", font=("Nunito", 11, "bold"), fg="#333333", bg=BLANCO).pack(side="left", padx=(10, 0))
        tk.Label(nav, text="100%", font=("Nunito", 11), fg=TEXTO_GRIS, bg=BLANCO).pack(side="right", padx=8)

        self.canvas.create_text(187, 110, text="SALUNIC | Atención", font=("Nunito", 22, "bold"), fill=BLANCO)
        self.canvas.create_text(187, 138, text="Cola con Prioridad (Adulto Mayor primero)", font=("Nunito", 9), fill=BLANCO)

        card_x, card_y, card_w, card_h = 18, 165, 340, 120
        create_rounded_rect(self.canvas, card_x, card_y, card_x + card_w, card_y + card_h, 18, fill="#FFFFFF", outline="")
        self.canvas.create_text(card_x + 20, card_y + 18, text="EN ATENCIÓN", font=("Nunito", 10, "bold"), fill=TEXTO_GRIS, anchor="w")
        if self.en_atencion:
            prio = self.en_atencion.get('prioridad', '')
            pac = self.en_atencion.get('paciente', 'Paciente')
            turno = self.en_atencion.get('turno', '-')
            cid = self.en_atencion.get('cita_id', '-')
            color = FUCSIA if 'ADULTO' in str(prio).upper() else VERDE
            self.canvas.create_text(card_x + 20, card_y + 48, text=f"{pac}", font=("Nunito", 16, "bold"), fill=AZUL_NOCHE, anchor="w")
            self.canvas.create_text(card_x + 20, card_y + 72, text=f"{prio} | Turno #{turno} | Cita ID: {cid}", font=("Nunito", 9), fill=color, anchor="w")
        else:
            self.canvas.create_text(card_x + 20, card_y + 55, text="Sin paciente en atención", font=("Nunito", 12), fill=TEXTO_GRIS, anchor="w")
            self.canvas.create_text(card_x + 20, card_y + 78, text="Presiona 'ATENDER SIGUIENTE'", font=("Nunito", 9), fill=TEXTO_GRIS, anchor="w")

        self.canvas.create_text(18, 305, text="COLA DE ESPERA", font=("Nunito", 10, "bold"), fill=BLANCO, anchor="w")

        cola = sistema.obtener_cola()
        if not cola:
            create_rounded_rect(self.canvas, 18, 325, 358, 385, 16, fill="#FFFFFF", outline="")
            self.canvas.create_text(187, 355, text="No hay pacientes en espera", font=("Nunito", 11), fill=TEXTO_GRIS, justify="center")
            cy_list = 400
        else:
            cy_list = 325
            for i, item in enumerate(cola[:5], 1):
                try:
                    prio, turno, data = item[0], item[1], item[2]
                except Exception:
                    continue
                prio_txt = data.get('prioridad', '')
                pac = data.get('paciente', 'Paciente')
                cid = data.get('cita_id', '-')
                hora = data.get('hora', '--:--')
                color = FUCSIA if 'ADULTO' in str(prio_txt).upper() else CELESTE
                create_rounded_rect(self.canvas, 18, cy_list, 358, cy_list + 58, 16, fill="#FFFFFF", outline="")
                self.canvas.create_text(32, cy_list + 18, text=f"{i}. {pac}", font=("Nunito", 11, "bold"), fill=AZUL_NOCHE, anchor="w")
                self.canvas.create_text(32, cy_list + 38, text=f"{prio_txt} | Turno #{turno} | Cita: {cid} | {hora}", font=("Nunito", 8), fill=color, anchor="w")
                cy_list += 66
            if len(cola) > 5:
                self.canvas.create_text(187, cy_list + 10, text=f"+ {len(cola)-5} pacientes más en espera", font=("Nunito", 9), fill=BLANCO, justify="center")
                cy_list += 30

        btn1_y = cy_list + 20
        create_rounded_rect(self.canvas, 18, btn1_y, 358, btn1_y + 48, 24, fill=VERDE, outline="")
        btn1 = tk.Label(self, text="ATENDER SIGUIENTE", font=("Nunito", 12, "bold"), fg=BLANCO, bg=VERDE, cursor="hand2")
        btn1.place(x=20, y=btn1_y + 2, width=336, height=44)
        btn1.bind("<Button-1>", lambda e: self._atender())

        btn2_y = btn1_y + 62
        create_rounded_rect(self.canvas, 18, btn2_y, 358, btn2_y + 48, 24, fill=CELESTE, outline="")
        btn2 = tk.Label(self, text="ACTUALIZAR PANEL", font=("Nunito", 11, "bold"), fg=BLANCO, bg=CELESTE, cursor="hand2")
        btn2.place(x=20, y=btn2_y + 2, width=336, height=44)
        btn2.bind("<Button-1>", lambda e: self._build_ui())

        btn3_y = btn2_y + 62
        create_rounded_rect(self.canvas, 18, btn3_y, 358, btn3_y + 48, 24, fill=AZUL_NOCHE, outline="")
        btn3 = tk.Label(self, text="VOLVER AL INICIO", font=("Nunito", 11, "bold"), fg=BLANCO, bg=AZUL_NOCHE, cursor="hand2")
        btn3.place(x=20, y=btn3_y + 2, width=336, height=44)
        btn3.bind("<Button-1>", lambda e: self.controller.show_screen("Home"))

    def _atender(self):
        try:
            if sistema.cola_vacia():
                messagebox.showinfo("Atención", "No hay pacientes en espera para atender.")
                self.en_atencion = None
                self._build_ui()
                return
            atendido = sistema.atender_siguiente()
            self.en_atencion = atendido
            if atendido:
                messagebox.showinfo("Atendiendo", f"Atendiendo a:\n{atendido.get('paciente')}\n{atendido.get('prioridad')} | Turno #{atendido.get('turno')}")
            self._build_ui()
        except Exception as ex:
            messagebox.showerror("Error", str(ex))
            self._build_ui()
