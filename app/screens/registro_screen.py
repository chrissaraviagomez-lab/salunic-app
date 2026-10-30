import tkinter as tk
from tkinter import messagebox
from data import users_data
from screens.styles import (VERDE, CELESTE, AZUL_NOCHE, BLANCO,
                            TEXTO_OSCURO, TEXTO_GRIS, GRADIENT_COLORS, WIDTH, HEIGHT,
                            create_rounded_rect)

class RegistroScreen(tk.Frame):
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
        self.canvas.create_oval(230, -30, 400, 140, fill="#E91E8C", outline="")
        self.canvas.create_oval(-20, 600, 150, 770, fill=VERDE, outline="")
        self.canvas.create_oval(200, 400, 310, 510, fill=CELESTE, outline="")

    def _draw_content(self):
        nav = tk.Frame(self, bg=BLANCO, bd=0)
        nav.place(relx=0.5, y=28, anchor="center", width=340, height=34)
        back_btn = tk.Label(nav, text="←", font=("Nunito", 18, "bold"), fg="#333333", bg=BLANCO, cursor="hand2")
        back_btn.pack(side="left", padx=8)
        back_btn.bind("<Button-1>", lambda e: self.controller.show_screen("Login"))
        tk.Label(nav, text="Registro", font=("Nunito", 12, "bold"), fg="#333333", bg=BLANCO
                 ).pack(side="left", padx=(16, 0))
        tk.Label(nav, text="100%", font=("Nunito", 11), fg=TEXTO_GRIS, bg=BLANCO
                 ).pack(side="right", padx=8)

        # Titulo sobre el gradiente
        self.canvas.create_text(187, 118, text="Crear Cuenta", font=("Nunito", 26, "bold"), fill=BLANCO)

        # Card redondeada con gradiente alrededor
        card_x, card_y, card_w, card_h = 28, 165, 319, 500
        create_rounded_rect(self.canvas, card_x, card_y, card_x + card_w, card_y + card_h,
                            20, fill="#FFFFFF", outline="")

        in_x = card_x + 24
        fields = [("Nombre Completo:", "name", False), ("Email:", "email", False),
                  ("Contrasena:", "password", True), ("Confirmar Contrasena:", "confirm", True)]
        self.entries = {}
        fpy = card_y + 24
        for label, key, hide in fields:
            tk.Label(self, text=label, font=("Nunito", 10), fg=TEXTO_OSCURO, bg="#FFFFFF"
                     ).place(x=in_x, y=fpy)
            e = tk.Entry(self, font=("Nunito", 11), bg="#F5F5F5", relief="flat", bd=0,
                         show="*" if hide else "",
                         highlightthickness=1, highlightbackground="#E0E0E0", highlightcolor=VERDE)
            e.place(x=in_x, y=fpy + 24, width=card_w - 48, height=36)
            self.entries[key] = e
            fpy += 76

        # Boton CREAR CUENTA
        b_y = fpy + 6
        create_rounded_rect(self.canvas, card_x + 44, b_y, card_x + card_w - 44, b_y + 48, 24, fill=VERDE, outline="")
        btn = tk.Label(self, text="CREAR CUENTA", font=("Nunito", 12, "bold"), fg=BLANCO, bg=VERDE, cursor="hand2")
        btn.place(x=card_x + 46, y=b_y + 2, width=card_w - 92, height=44)
        btn.bind("<Button-1>", lambda e: self._register())

        back_lbl = tk.Label(self, text="Volver", font=("Nunito", 10), fg=CELESTE, bg="#FFFFFF", cursor="hand2")
        back_lbl.place(x=card_x, y=b_y + 60, width=card_w, height=22)
        back_lbl.bind("<Button-1>", lambda e: self.controller.show_screen("Login"))

    def _register(self):
        name = self.entries["name"].get()
        email = self.entries["email"].get()
        pw = self.entries["password"].get()
        cpw = self.entries["confirm"].get()
        if not all([name, email, pw, cpw]):
            messagebox.showerror("Error", "Completa todos los campos")
            return
        if pw != cpw:
            messagebox.showerror("Error", "Las contrasenas no coinciden")
            return
        if len(pw) < 6:
            messagebox.showerror("Error", "La contrasena debe tener al menos 6 caracteres")
            return
        if users_data.email_exists(email):
            messagebox.showerror("Error", "El correo ya esta registrado")
            return
        users_data.add_user(name, email, pw)
        self.controller.current_user = users_data.find_user(email, pw)
        messagebox.showinfo("Exito", "Cuenta creada correctamente")
        self.controller.show_screen("Home")
