import tkinter as tk
from tkinter import messagebox
from data import users_data
from screens.styles import (VERDE, CELESTE, FUCSIA, AZUL_NOCHE, BLANCO,
                            TEXTO_OSCURO, TEXTO_GRIS, GRADIENT_COLORS, WIDTH, HEIGHT,
                            create_rounded_rect)

class FormRegistro(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg=AZUL_NOCHE)
        self.controller = controller
        self.terminos_var = tk.BooleanVar(value=False)
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
        self.canvas.create_oval(230, -20, 390, 130, fill=FUCSIA, outline="")
        self.canvas.create_oval(-20, 580, 150, 770, fill=VERDE, outline="")

    def _prefill(self):
        user = self.controller.current_user
        nombre = ""
        apellido = ""
        email = ""
        telefono = ""
        if user and isinstance(user, dict):
            name = user.get("name", "")
            nombre = name.split()[0] if name.split() else ""
            apellido = " ".join(name.split()[1:]) if len(name.split()) > 1 else ""
            email = user.get("email", "")
            telefono = user.get("telefono", "")
        return nombre, apellido, email, telefono

    def _draw_content(self):
        nav = tk.Frame(self, bg=BLANCO, bd=0)
        nav.place(relx=0.5, y=28, anchor="center", width=340, height=34)
        back_btn = tk.Label(nav, text="←", font=("Nunito", 18, "bold"), fg="#333333", bg=BLANCO, cursor="hand2")
        back_btn.pack(side="left", padx=8)
        back_btn.bind("<Button-1>", lambda e: self.controller.show_screen("Home"))
        tk.Label(nav, text="Editar Perfil", font=("Nunito", 14, "bold"),
                 fg=AZUL_NOCHE, bg=BLANCO).pack(side="left", padx=12)
        tk.Label(nav, text="100%", font=("Nunito", 11), fg=TEXTO_GRIS, bg=BLANCO
                 ).pack(side="right", padx=8)

        self.canvas.create_text(187, 120, text="Editar Perfil", font=("Nunito", 22, "bold"), fill=BLANCO)
        self.canvas.create_text(187, 148, text="Actualiza tu informacion personal", font=("Nunito", 11), fill=BLANCO)

        nombre, apellido, email, telefono = self._prefill()

        campos = [
            ("Nombre", nombre, "Ej: Juan"),
            ("Apellido", apellido, "Ej: Perez"),
            ("Correo Electronico", email, "Ej: usuario@correo.com"),
            ("Telefono", telefono, "Ej: +505 86459285"),
        ]

        self.entries = {}
        cy = 180
        for i, (label, valor, ph) in enumerate(campos):
            # Card individual que contiene el campo
            create_rounded_rect(self.canvas, 18, cy, 18 + 340, cy + 86, 16, fill="#FFFFFF", outline="")
            self.canvas.create_text(30, cy + 20, text=label, font=("Nunito", 9, "bold"),
                                    fill=TEXTO_OSCURO, anchor="w")
            e = self._entry(self, valor, ph)
            e.place(x=30, y=cy + 34, width=316, height=38)
            self.entries[f"campo{i}"] = {"entry": e, "label": label, "key": ("nombre", "apellido", "email", "telefono")[i], "ph": ph}
            cy += 96

        # Checkbox terminos (dentro de card blanca)
        chk_y = cy + 2
        create_rounded_rect(self.canvas, 18, chk_y, 18 + 340, chk_y + 44, 12, fill="#FFFFFF", outline="")
        chk = tk.Checkbutton(self, text="Acepto los terminos y condiciones",
                             variable=self.terminos_var, font=("Nunito", 9),
                             fg=TEXTO_OSCURO, bg="#FFFFFF", activebackground="#FFFFFF",
                             selectcolor="#FFFFFF", anchor="w", cursor="hand2")
        chk.place(x=26, y=chk_y + 4, width=324, height=36)

        # Boton GUARDAR CAMBIOS
        btn_y = chk_y + 52
        create_rounded_rect(self.canvas, 18, btn_y, 18 + 340, btn_y + 46, 23, fill=VERDE, outline="")
        btn = tk.Label(self, text="GUARDAR CAMBIOS", font=("Nunito", 12, "bold"),
                       fg=BLANCO, bg=VERDE, cursor="hand2")
        btn.place(x=20, y=btn_y + 2, width=336, height=42)
        btn.bind("<Button-1>", lambda e: self._guardar())

        # Volver (dentro de card blanca)
        v_y = btn_y + 54
        create_rounded_rect(self.canvas, 18, v_y, 18 + 340, v_y + 40, 20, fill="#FFFFFF", outline="")
        volver = tk.Label(self, text="Volver", font=("Nunito", 11, "bold"),
                          fg=CELESTE, bg="#FFFFFF", cursor="hand2")
        volver.place(x=20, y=v_y + 1, width=336, height=38)
        volver.bind("<Button-1>", lambda e: self.controller.show_screen("Home"))

    def _entry(self, parent, valor, ph):
        e = tk.Entry(parent, font=("Nunito", 12), bg="#F5F5F5", relief="flat", bd=0, fg=TEXTO_OSCURO,
                      highlightthickness=1, highlightbackground="#E0E0E0", highlightcolor=VERDE)
        if valor:
            e.insert(0, valor)
        else:
            e.insert(0, ph)
            e.config(fg=TEXTO_GRIS)
            e.bind("<FocusIn>", lambda ev: self._fi(ev, ph))
            e.bind("<FocusOut>", lambda ev: self._fo(ev, ph))
        return e

    def _fi(self, ev, ph):
        if ev.widget.get() == ph:
            ev.widget.delete(0, "end")
            ev.widget.config(fg=TEXTO_OSCURO)

    def _fo(self, ev, ph):
        if ev.widget.get().strip() == "":
            ev.widget.insert(0, ph)
            ev.widget.config(fg=TEXTO_GRIS)

    def _val(self, campo):
        e = campo["entry"].get().strip()
        ph = campo["ph"]
        if e == ph or e == "":
            return ""
        return e

    def _guardar(self):
        nombre = self._val(self.entries["campo0"])
        apellido = self._val(self.entries["campo1"])
        email = self._val(self.entries["campo2"])
        telefono = self._val(self.entries["campo3"])

        if not nombre:
            messagebox.showerror("Error", "Por favor ingresa tu nombre")
            return
        if not email:
            messagebox.showerror("Error", "Por favor ingresa tu correo")
            return
        if "@" not in email or "." not in email:
            messagebox.showerror("Error", "Correo electronico invalido")
            return
        if not self.terminos_var.get():
            messagebox.showerror("Error", "Debes aceptar los terminos y condiciones")
            return

        nombre_completo = " ".join([nombre, apellido]).strip()
        email_anterior = None
        if self.controller.current_user and isinstance(self.controller.current_user, dict):
            email_anterior = self.controller.current_user.get("email")
            self.controller.current_user["name"] = nombre_completo
            self.controller.current_user["email"] = email
            self.controller.current_user["telefono"] = telefono
        else:
            self.controller.current_user = {"name": nombre_completo, "email": email, "telefono": telefono}

        if email_anterior:
            users_data.update_user(email_anterior, name=nombre_completo, email_nuevo=email)

        messagebox.showinfo("Perfil actualizado", "Perfil guardado exitosamente")
        self.controller.show_screen("Home")
