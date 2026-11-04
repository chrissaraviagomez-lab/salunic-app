import tkinter as tk
from tkinter import messagebox, simpledialog
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from core import cola_atencion
from core import datos as core_datos
from core import entidades
from core import archivo_datos
from core import busqueda_lineal
from screens.styles import (VERDE, CELESTE, FUCSIA, AMARILLO, AZUL_NOCHE, BLANCO,
                            TEXTO_OSCURO, TEXTO_GRIS, GRADIENT_COLORS, WIDTH, HEIGHT,
                            create_rounded_rect)


class CitasScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg=AZUL_NOCHE)
        self.controller = controller
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

    def _get_current_patient_name(self):
        current = getattr(self.controller, 'current_user', None)
        paciente = 'Paciente'
        if isinstance(current, dict):
            paciente = current.get('name') or current.get('nombre') or current.get('full_name') or current.get('email') or paciente
        elif current is not None:
            paciente = getattr(current, 'nombre', None) or getattr(current, 'name', None) or getattr(current, 'full_name', None) or getattr(current, 'email', None) or paciente
        if paciente in (None, '', 'Paciente'):
            try:
                archivo_datos.cargar_datos()
                email = None
                if isinstance(current, dict):
                    email = current.get('email')
                elif current is not None:
                    email = getattr(current, 'email', None)
                if email:
                    u = busqueda_lineal.busqueda_lineal_por_email(core_datos.usuarios, email)
                    if u:
                        paciente = getattr(u, 'nombre', paciente)
            except Exception:
                pass
        return paciente

    def _draw_content(self):
        nav = tk.Frame(self, bg=BLANCO, bd=0)
        nav.place(relx=0.5, y=28, anchor="center", width=340, height=34)
        back_btn = tk.Label(nav, text="←", font=("Nunito", 18, "bold"), fg="#333333", bg=BLANCO, cursor="hand2")
        back_btn.pack(side="left", padx=8)
        back_btn.bind("<Button-1>", lambda e: self.controller.show_screen("Home"))
        tk.Label(nav, text="Citas", font=("Nunito", 12, "bold"), fg="#333333", bg=BLANCO).pack(side="left", padx=(16, 0))
        tk.Label(nav, text="100%", font=("Nunito", 11), fg=TEXTO_GRIS, bg=BLANCO).pack(side="right", padx=8)

        self.canvas.create_text(187, 110, text="Citas Médicas", font=("Nunito", 22, "bold"), fill=BLANCO)
        self.canvas.create_text(187, 138, text="Gestiona tus citas desde aquí", font=("Nunito", 10), fill=BLANCO)

        try:
            archivo_datos.cargar_datos()
        except Exception:
            pass

        cy = 165
        citas_core = list(getattr(core_datos, 'citas', []))
        if not citas_core:
            self.canvas.create_text(187, cy + 35, text="Sin citas registradas", font=("Nunito", 11), fill=BLANCO)
            cy += 80
        else:
            colors_c = [VERDE, CELESTE, FUCSIA, AMARILLO]
            for idx, c in enumerate(citas_core[:4]):
                dia_mes = str(getattr(c, 'fecha', '01/01')).split('/')
                dia = dia_mes[0] if len(dia_mes) > 0 else '--'
                mes = 'MES'
                try:
                    meses = {'01': 'ENE', '02': 'FEB', '03': 'MAR', '04': 'ABR', '05': 'MAY', '06': 'JUN', '07': 'JUL', '08': 'AGO', '09': 'SEP', '10': 'OCT', '11': 'NOV', '12': 'DIC'}
                    mes = meses.get(dia_mes[1], 'MES')
                except Exception:
                    pass
                medico = f"Medico ID: {getattr(c, 'medico_id', '-')}"
                espec = getattr(c, 'especialidad', 'Consulta')
                hora = getattr(c, 'hora', '--:--')
                lugar = getattr(c, 'lugar', 'Hospital')
                color = colors_c[idx % len(colors_c)]
                create_rounded_rect(self.canvas, 18, cy, 18 + 340, cy + 78, 16, fill="#FFFFFF", outline="")
                create_rounded_rect(self.canvas, 28, cy + 14, 28 + 52, cy + 64, 12, fill=color, outline="")
                self.canvas.create_text(54, cy + 39, text=f"{dia}\n{mes}", font=("Nunito", 10, "bold"), fill=BLANCO, justify="center")
                self.canvas.create_text(100, cy + 22, text=medico, font=("Nunito", 12, "bold"), fill=TEXTO_OSCURO, anchor="w")
                self.canvas.create_text(100, cy + 42, text=espec, font=("Nunito", 10), fill=TEXTO_GRIS, anchor="w")
                self.canvas.create_text(100, cy + 60, text=f"{hora} - {lugar}", font=("Nunito", 9), fill=color, anchor="w")
                cy += 90

        btn_ac_y = cy + 6
        create_rounded_rect(self.canvas, 18, btn_ac_y, 18 + 340, btn_ac_y + 44, 22, fill=VERDE, outline="")
        btn_ac = tk.Label(self, text="AGREGAR NUEVA CITA", font=("Nunito", 11, "bold"), fg=BLANCO, bg=VERDE, cursor="hand2")
        btn_ac.place(x=20, y=btn_ac_y + 2, width=336, height=40)
        btn_ac.bind("<Button-1>", lambda e: self._add_cita())

        btn_qy = btn_ac_y + 52
        create_rounded_rect(self.canvas, 18, btn_qy, 18 + 340, btn_qy + 44, 22, fill=FUCSIA, outline="")
        btn_q = tk.Label(self, text="AGREGAR A COLA DE ATENCION (PRIORIDAD)", font=("Nunito", 10, "bold"), fg=BLANCO, bg=FUCSIA, cursor="hand2")
        btn_q.place(x=20, y=btn_qy + 2, width=336, height=40)
        btn_q.bind("<Button-1>", lambda e: self._add_to_queue())

        btn_y = btn_qy + 52
        create_rounded_rect(self.canvas, 18, btn_y, 18 + 340, btn_y + 44, 22, fill=CELESTE, outline="")
        btn = tk.Label(self, text="VOLVER AL INICIO", font=("Nunito", 12, "bold"), fg=BLANCO, bg=CELESTE, cursor="hand2")
        btn.place(x=20, y=btn_y + 2, width=336, height=40)
        btn.bind("<Button-1>", lambda e: self.controller.show_screen("Home"))

    def _add_cita(self):
        try:
            archivo_datos.cargar_datos()
            paciente = self._get_current_patient_name()
            especialidad = simpledialog.askstring("Nueva Cita", "Especialidad:") or "Medicina General"
            fecha = simpledialog.askstring("Nueva Cita", "Fecha (DD/MM/AAAA):") or "01/12/2026"
            hora = simpledialog.askstring("Nueva Cita", "Hora (HH:MM):") or "09:00"
            medico_id = simpledialog.askinteger("Nueva Cita", "ID del Médico:") or 201
            new_id = len(core_datos.citas) + 500
            paciente_id = 1
            try:
                current = getattr(self.controller, 'current_user', None)
                email = None
                if isinstance(current, dict):
                    email = current.get('email')
                elif current is not None:
                    email = getattr(current, 'email', None)
                if email:
                    u = busqueda_lineal.busqueda_lineal_por_email(core_datos.usuarios, email)
                    if u:
                        paciente_id = getattr(u, 'id', 1)
            except Exception:
                pass
            cita = entidades.CitaMedica(id=new_id, paciente_id=paciente_id, medico_id=medico_id, especialidad=especialidad, fecha=fecha, hora=hora, lugar="Hospital")
            core_datos.citas.append(cita)
            archivo_datos.guardar_datos()
            messagebox.showinfo("Cita Agendada", f"Cita registrada correctamente.\nPaciente: {paciente}\n{especialidad} | {fecha} {hora}")
            self._build_ui()
        except Exception as ex:
            messagebox.showerror("Error", str(ex))

    def _add_to_queue(self):
        try:
            paciente = self._get_current_patient_name()
            item = {"paciente": paciente, "cita_id": len(cola_atencion.cola_atencion.cola) + 200, "hora": "09:00"}
            es_adulto_mayor = messagebox.askyesno("Cola con Prioridad", "¿Es Adulto Mayor?\n(Se le dará PRIORIDAD al atender con heapq)")
            cola_atencion.cola_atencion.encolar(item, es_adulto_mayor=es_adulto_mayor)
            messagebox.showinfo("Cola de Atención", f"Paciente: {paciente}\nAgregado a la cola con prioridad.")
            try:
                cola_atencion.cola_atencion.mostrar_cola()
            except Exception:
                pass
        except Exception as ex:
            messagebox.showerror("Error", str(ex))
