import tkinter as tk
from tkinter import messagebox
from screens.styles import (VERDE, AZUL_NOCHE, BLANCO,
                            TEXTO_OSCURO, TEXTO_GRIS, GRADIENT_COLORS, WIDTH, HEIGHT,
                            create_rounded_rect)

class Screen2OTP(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg=AZUL_NOCHE)
        self.controller = controller
        self.otp_values = [tk.StringVar() for _ in range(6)]
        self.otp_entries = []
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
        self.canvas.create_oval(-20, 600, 150, 770, fill=VERDE, outline="")
        self.canvas.create_oval(230, 60, 360, 190, fill="#E91E8C", outline="")

    def _draw_content(self):
        nav = tk.Frame(self, bg=BLANCO, bd=0)
        nav.place(relx=0.5, y=28, anchor="center", width=340, height=34)
        back_btn = tk.Label(nav, text="←", font=("Nunito", 18, "bold"), fg="#333333", bg=BLANCO, cursor="hand2")
        back_btn.pack(side="left", padx=8)
        back_btn.bind("<Button-1>", lambda e: self.controller.show_screen("Login"))
        tk.Label(nav, text="OTP", font=("Nunito", 12, "bold"), fg="#333333", bg=BLANCO
                 ).pack(side="left", padx=(16, 0))
        tk.Label(nav, text="100%", font=("Nunito", 11), fg=TEXTO_GRIS, bg=BLANCO
                 ).pack(side="right", padx=8)

        # Titulo sobre el gradiente
        self.canvas.create_text(187, 128, text="Restablecer Contrasena", font=("Nunito", 20, "bold"), fill=BLANCO)

        # Card redondeada con gradiente alrededor
        card_x, card_y, card_w, card_h = 28, 185, 319, 400
        create_rounded_rect(self.canvas, card_x, card_y, card_x + card_w, card_y + card_h,
                            20, fill="#FFFFFF", outline="")

        tk.Label(self, text="Revisa tu correo", font=("Nunito", 16, "bold"),
                 fg=TEXTO_OSCURO, bg="#FFFFFF").place(x=card_x, y=card_y + 24, width=card_w)
        tk.Label(self, text="Ingresa el codigo de 6 digitos\nenviado a usuario@salunic.com",
                 font=("Nunito", 10), fg=TEXTO_GRIS, bg="#FFFFFF", justify="center"
                 ).place(x=card_x, y=card_y + 60, width=card_w)

        otp_frame = tk.Frame(self, bg="#FFFFFF")
        otp_frame.place(x=card_x + 16, y=card_y + 118, width=card_w - 32)
        for i in range(6):
            entry = tk.Entry(otp_frame, textvariable=self.otp_values[i],
                             font=("Nunito", 20, "bold"), width=2, justify="center",
                             bg="#F5F5F5", relief="flat", bd=0, fg=TEXTO_OSCURO,
                             highlightthickness=1, highlightbackground="#E0E0E0", highlightcolor=VERDE)
            entry.pack(side="left", padx=4, ipady=6)
            self.otp_entries.append(entry)
            entry.bind("<KeyRelease>", lambda e, idx=i: self._on_key(e, idx))

        tk.Label(self, text="No recibiste el codigo? Reenviar 02:45",
                 font=("Nunito", 9), fg=TEXTO_GRIS, bg="#FFFFFF"
                 ).place(x=card_x, y=card_y + 200, width=card_w)

        # Boton VERIFICAR CODIGO
        b_y = card_y + 250
        create_rounded_rect(self.canvas, card_x + 44, b_y, card_x + card_w - 44, b_y + 48, 24, fill=VERDE, outline="")
        btn = tk.Label(self, text="VERIFICAR CODIGO", font=("Nunito", 12, "bold"),
                       fg=BLANCO, bg=VERDE, cursor="hand2")
        btn.place(x=card_x + 46, y=b_y + 2, width=card_w - 92, height=44)
        btn.bind("<Button-1>", lambda e: self._verificar())

    def _on_key(self, event, idx):
        if event.keysym == "BackSpace" and idx > 0:
            self.otp_entries[idx - 1].focus()
            self.otp_entries[idx - 1].delete(0, "end")
        elif event.char.isdigit() and idx < 5:
            self.otp_entries[idx + 1].focus()
        elif event.char.isdigit() and idx == 5:
            self.otp_entries[idx].focus_set()

    def _verificar(self):
        codigo = "".join(v.get() for v in self.otp_values)
        if len(codigo) != 6 or not codigo.isdigit():
            messagebox.showerror("Error", "Ingresa el codigo completo de 6 digitos")
            return
        if codigo == "123456":
            messagebox.showinfo("Exito", "Codigo verificado correctamente")
            self.controller.show_screen("Login")
        else:
            messagebox.showerror("Error", "Codigo incorrecto. Intenta de nuevo.")
