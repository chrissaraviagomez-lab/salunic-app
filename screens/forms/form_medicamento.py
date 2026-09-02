import tkinter as tk
from tkinter import messagebox
from screens.styles import (VERDE, CELESTE, FUCSIA, AZUL_NOCHE, BLANCO,
                            TEXTO_OSCURO, TEXTO_GRIS, GRADIENT_COLORS, WIDTH, HEIGHT,
                            create_rounded_rect)

class FormMedicamento(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg=AZUL_NOCHE)
        self.controller = controller
        self.frecuencia_var = tk.StringVar(value="2x")
        self.recordatorio_var = tk.BooleanVar(value=True)
        self.frecuencia_botones = []
        self._build_ui()

    def _build_ui(self):
        self.canvas = tk.Canvas(self, width=WIDTH, height=HEIGHT, highlightthickness=0, bg=AZUL_NOCHE)
        self.canvas.pack()
        self._draw_bg()
        self._draw_content()

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

    def _draw_bg(self):
        self._gradient_lines(self.canvas, HEIGHT)
        self.canvas.create_oval(230, -20, 390, 130, fill=FUCSIA, outline="")
        self.canvas.create_oval(-20, 600, 150, 770, fill="#2ECC71", outline="")

    def _card(self, canvas, x, y, w, h, parent_title=None):
        create_rounded_rect(canvas, x, y, x + w, y + h, 16, fill="#FFFFFF", outline="")

    def _draw_content(self):
        nav = tk.Frame(self, bg=BLANCO, bd=0)
        nav.place(relx=0.5, y=28, anchor="center", width=340, height=34)
        back_btn = tk.Label(nav, text="←", font=("Nunito", 18, "bold"), fg="#333333", bg=BLANCO, cursor="hand2")
        back_btn.pack(side="left", padx=8)
        back_btn.bind("<Button-1>", lambda e: self.controller.show_screen("Medicamentos"))
        tk.Label(nav, text="Nuevo Medicamento", font=("Nunito", 14, "bold"),
                 fg=AZUL_NOCHE, bg=BLANCO).pack(side="left", padx=12)
        tk.Label(nav, text="100%", font=("Nunito", 11), fg=TEXTO_GRIS, bg=BLANCO
                 ).pack(side="right", padx=8)

        # Titulo sobre el gradiente
        self.canvas.create_text(187, 96, text="Agregar Medicamento", font=("Nunito", 22, "bold"), fill=BLANCO)

        # Canvas desplazable con gradiente de contenido
        self.scroll = tk.Canvas(self, width=WIDTH, height=HEIGHT - 140, highlightthickness=0, bg=AZUL_NOCHE)
        self.scroll.place(y=140)
        self._gradient_lines(self.scroll, 900)
        sb = tk.Scrollbar(self, orient="vertical", command=self.scroll.yview)
        sb.place(x=360, y=140, height=HEIGHT - 140)
        self.scroll.configure(yscrollcommand=sb.set, scrollregion=(0, 0, WIDTH, 900))

        # ---- Card 1: NOMBRE + DOSIS/PRESENTACION ----
        cy = 16
        self.scroll.create_text(34, cy + 16, text="NOMBRE DEL MEDICAMENTO *", font=("Nunito", 9, "bold"),
                                fill="#BDE0FE", anchor="w")
        self.nombre_entry = self._entry(self.scroll, "Ej: Metformina 500mg")
        self.scroll.create_window(34, cy + 28, window=self.nombre_entry, anchor="nw", width=307, height=40)

        # DOSIS
        self.scroll.create_text(34, cy + 84, text="DOSIS *", font=("Nunito", 9, "bold"), fill="#BDE0FE", anchor="w")
        self.dosis_entry = self._entry(self.scroll, "500mg")
        self.scroll.create_window(34, cy + 96, window=self.dosis_entry, anchor="nw", width=150, height=40)

        # PRESENTACION
        self.scroll.create_text(194, cy + 84, text="PRESENTACION", font=("Nunito", 9, "bold"), fill="#BDE0FE", anchor="w")
        self.presentacion_entry = self._entry(self.scroll, "Tableta")
        self.scroll.create_window(194, cy + 96, window=self.presentacion_entry, anchor="nw", width=147, height=40)

        # ---- Card 2: FRECUENCIA ----
        cy = 160
        self.scroll.create_text(34, cy + 16, text="FRECUENCIA *", font=("Nunito", 9, "bold"), fill="#BDE0FE", anchor="w")
        ff_x = 34
        for i, (valor, texto) in enumerate([("1x", "1X DIA"), ("2x", "2X DIA"), ("3x", "3X DIA"), ("8h", "C/8H")]):
            active = valor == "2x"
            btn = tk.Button(self.scroll, text=texto, font=("Nunito", 8, "bold"),
                            bg=VERDE if active else "#FFFFFF",
                            fg=BLANCO if active else "#666666",
                            relief="flat", bd=0, cursor="hand2",
                            command=lambda v=valor: self._toggle_frec(v))
            self.scroll.create_window(ff_x + i * 78, cy + 30, window=btn, anchor="nw", width=72, height=38)
            self.frecuencia_botones.append((btn, valor))

        # ---- Card 3: HORARIOS ----
        cy = 230
        self.scroll.create_text(34, cy + 16, text="HORARIOS *", font=("Nunito", 9, "bold"), fill="#BDE0FE", anchor="w")
        self.h1 = self._entry(self.scroll, "8:00 AM")
        self.scroll.create_window(34, cy + 28, window=self.h1, anchor="nw", width=150, height=40)
        self.h2 = self._entry(self.scroll, "8:00 PM")
        self.scroll.create_window(194, cy + 28, window=self.h2, anchor="nw", width=147, height=40)

        # ---- Card 4: INSTRUCCIONES ----
        cy = 310
        self.scroll.create_text(34, cy + 16, text="INSTRUCCIONES", font=("Nunito", 9, "bold"), fill="#BDE0FE", anchor="w")
        self.inst = self._entry(self.scroll, "Ej: Tomar con alimentos")
        self.scroll.create_window(34, cy + 28, window=self.inst, anchor="nw", width=307, height=40)

        # ---- Checkbox recordatorio (dentro de card) ----
        cy = 384
        create_rounded_rect(self.scroll, 20, cy, 20 + 335, cy + 44, 12, fill="#FFFFFF", outline="")
        chk = tk.Checkbutton(self.scroll, text="Notificacion push", variable=self.recordatorio_var,
                             font=("Nunito", 10), fg=TEXTO_OSCURO, bg="#FFFFFF", activebackground="#FFFFFF",
                             selectcolor="#FFFFFF", anchor="w", cursor="hand2")
        self.scroll.create_window(28, cy + 4, window=chk, anchor="nw", width=320, height=36)

        # ---- Boton GUARDAR (card verde) ----
        cy = 452
        create_rounded_rect(self.scroll, 20, cy, 20 + 335, cy + 50, 23, fill=VERDE, outline="")
        btn = tk.Label(self.scroll, text="GUARDAR MEDICAMENTO", font=("Nunito", 12, "bold"),
                       fg=BLANCO, bg=VERDE, cursor="hand2")
        self.scroll.create_window(20, cy + 2, window=btn, anchor="nw", width=335, height=46)
        btn.bind("<Button-1>", lambda e: self._guardar())

        # ---- Volver (card blanca) ----
        cy = 520
        create_rounded_rect(self.scroll, 20, cy, 20 + 335, cy + 40, 20, fill="#FFFFFF", outline="")
        volver = tk.Label(self.scroll, text="Volver", font=("Nunito", 11, "bold"),
                          fg=CELESTE, bg="#FFFFFF", cursor="hand2")
        self.scroll.create_window(20, cy + 1, window=volver, anchor="nw", width=335, height=38)
        volver.bind("<Button-1>", lambda e: self.controller.show_screen("Medicamentos"))

        self.scroll.create_text(187, cy + 70, text="Recuerda: toma tus medicamentos a la hora indicada",
                                font=("Nunito", 9), fill="#DCE6F5")

    def _entry(self, parent, placeholder):
        e = tk.Entry(parent, font=("Nunito", 11), bg="#F5F5F5", relief="flat", bd=0, fg=TEXTO_GRIS,
                      highlightthickness=1, highlightbackground="#E0E0E0", highlightcolor=VERDE)
        e.insert(0, placeholder)
        e.bind("<FocusIn>", lambda ev: self._fi(ev, placeholder))
        e.bind("<FocusOut>", lambda ev: self._fo(ev, placeholder))
        return e

    def _fi(self, ev, ph):
        if ev.widget.get() == ph:
            ev.widget.delete(0, "end")
            ev.widget.config(fg=TEXTO_OSCURO)

    def _fo(self, ev, ph):
        if ev.widget.get().strip() == "":
            ev.widget.insert(0, ph)
            ev.widget.config(fg=TEXTO_GRIS)

    def _toggle_frec(self, valor):
        self.frecuencia_var.set(valor)
        for btn, v in self.frecuencia_botones:
            btn.config(bg=VERDE if v == valor else "#FFFFFF",
                       fg=BLANCO if v == valor else "#666666")

    def _guardar(self):
        nombre = self.nombre_entry.get().strip()
        dosis = self.dosis_entry.get().strip()
        h1 = self.h1.get().strip()
        if not nombre or nombre == "Ej: Metformina 500mg":
            messagebox.showerror("Error", "Ingresa el nombre del medicamento")
            return
        if not dosis or dosis == "500mg":
            messagebox.showerror("Error", "Ingresa la dosis")
            return
        if not h1 or h1 == "8:00 AM":
            messagebox.showerror("Error", "Ingresa al menos un horario")
            return
        freq = {"1x": "1 vez al dia", "2x": "2 veces al dia",
                "3x": "3 veces al dia", "8h": "Cada 8 horas"}
        f = freq.get(self.frecuencia_var.get(), "")
        messagebox.showinfo("Medicamento guardado",
                            f"Medicamento: {nombre}\nDosis: {dosis}\nFrecuencia: {f}\n"
                            f"Recordatorio: {'Si' if self.recordatorio_var.get() else 'No'}")
        self.controller.show_screen("Medicamentos")