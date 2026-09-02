import os

OUT = "C:\\salunic-app\\diagramas_nuevos"
os.makedirs(OUT, exist_ok=True)

AZUL = "#1565C0"; AZUL_L = "#E3F2FD"; AZUL_O = "#0D47A1"
VERDE = "#2ECC71"; VERDE_L = "#E8F5E9"
NARANJA = "#FF7043"; NARANJA_L = "#FFF3E0"
ROJO = "#E53935"; ROJO_L = "#FFEBEE"
PURPURA = "#9C27B0"; PURPURA_L = "#F3E5F5"
FONDO = "#FAFAFA"; NEGRO = "#212121"; GRIS = "#616161"; GRIS2 = "#9E9E9E"
BLANCO = "#FFFFFF"
FAM = "Segoe UI, Arial, sans-serif"
BCOLORS = {"AZUL":(AZUL,AZUL_L),"VERDE":(VERDE,VERDE_L),"NARANJA":(NARANJA,NARANJA_L),"ROJO":(ROJO,ROJO_L),"PURPURA":(PURPURA,PURPURA_L)}

def esc(s):
    return str(s).replace("&","&amp;").replace("<","&lt;").replace(">","&gt;").replace('"',"&quot;")

class SVG:
    def __init__(self, w, h):
        self.w, self.h = w, h
        self.c = []

    def _h(self, c): return BCOLORS.get(c, (c,"#eee"))[0]
    def _l(self, c): return BCOLORS.get(c, ("#333","#eee"))[1]

    def save(self, path):
        defs = []
        for col in ["AZUL","VERDE","NARANJA","ROJO","PURPURA"]:
            hx = self._h(col)
            defs.append(f'<marker id="a-{col}" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0L10 5L0 10z" fill="{hx}"/></marker>')
        defs.append('<filter id="sh"><feDropShadow dx="2" dy="3" stdDeviation="3" flood-color="#000" flood-opacity=".10"/></filter>')
        defs.append('<filter id="sh2"><feDropShadow dx="1" dy="2" stdDeviation="2" flood-color="#000" flood-opacity=".08"/></filter>')
        with open(path,"w",encoding="utf-8") as f:
            f.write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {self.w} {self.h}"><defs>{"".join(defs)}</defs><rect width="{self.w}" height="{self.h}" fill="{FONDO}"/>{"".join(self.c)}</svg>')

    def _r(self, x, y, w, h, rx, fill, stroke="none", sw=0):
        self.c.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>')

    def _t(self, s, x, y, sz, c=NEGRO, w="normal", a="middle"):
        self.c.append(f'<text x="{x}" y="{y}" text-anchor="{a}" font-family="{FAM}" font-size="{sz}" font-weight="{w}" fill="{c}">{esc(s)}</text>')

    def _p(self, pts, fill="none", stroke="#333", sw=1):
        self.c.append(f'<polyline points="{pts}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>')

    # ========== HEADERS ==========
    def title(self, txt):
        self._r(0, 0, self.w, 52, 0, AZUL)
        self.c.append(f'<rect x="0" y="48" width="{self.w}" height="4" fill="{AZUL_O}" rx="0"/>')
        self._t(txt, self.w//2, 33, 22, BLANCO, "bold")

    def subtitle(self, txt, y):
        self._r(0, y, self.w, 32, 0, AZUL_O)
        self._t(txt, self.w//2, y+21, 16, BLANCO, "bold")

    def section(self, txt, y):
        self._t(txt, 25, y, 14, GRIS2, "bold", "start")

    # ========== DFD SYMBOLS ==========
    def entity(self, x, y, w, h, label, color="AZUL"):
        """External entity: rectangle with 3D right/bottom shadow"""
        c = self._h(color)
        self._r(x+3, y+3, w, h, 6, "rgba(0,0,0,.08)")
        self._r(x, y, w, h, 6, BLANCO, c, 2.5)
        self._t(label, x+w//2, y+h//2+5, 16, c, "bold")

    def process(self, x, y, w, h, pid, title, items, color="AZUL"):
        """Process: rounded rect with color header"""
        c, cl = self._h(color), self._l(color)
        self._r(x+2, y+2, w, h, 12, "rgba(0,0,0,.06)")
        self._r(x, y, w, h, 12, cl, c, 2.5)
        self._r(x+6, y+6, w-12, 26, 7, c, c)
        self._t(pid, x+w//2, y+24, 13, BLANCO, "bold")
        self._t(title, x+w//2, y+52, 16, c, "bold")
        yy = y + 72
        for it in items:
            self._t(it, x+20, yy, 13, NEGRO, "normal", "start")
            yy += 22

    def datastore(self, x, y, w, h, label, items, color="PURPURA"):
        """Data store: YOURDON notation - rectangle open on right side"""
        c, cl = self._h(color), self._l(color)
        # Left and top/bottom borders (open right side)
        self._r(x+2, y+2, w, h, 0, "rgba(0,0,0,.05)")
        self.c.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="0" fill="{cl}" stroke="none"/>')
        self.c.append(f'<line x1="{x}" y1="{y}" x2="{x}" y2="{y+h}" stroke="{c}" stroke-width="2.5"/>')
        self.c.append(f'<line x1="{x}" y1="{y}" x2="{x+w-8}" y2="{y}" stroke="{c}" stroke-width="2.5"/>')
        self.c.append(f'<line x1="{x}" y1="{y+h}" x2="{x+w-8}" y2="{y+h}" stroke="{c}" stroke-width="2.5"/>')
        # Right side small cap
        self.c.append(f'<line x1="{x+w-8}" y1="{y}" x2="{x+w-8}" y2="{y+6}" stroke="{c}" stroke-width="2.5"/>')
        self.c.append(f'<line x1="{x+w-8}" y1="{y+h}" x2="{x+w-8}" y2="{y+h-6}" stroke="{c}" stroke-width="2.5"/>')
        # Label
        self._t(label, x+w//2-4, y+18, 12, c, "bold")
        yy = y + 36
        for it in items:
            self._t(it, x+w//2-4, yy, 12, c, "bold")
            yy += 20

    def step(self, x, y, w, h, label, items, color):
        """Step box for Nivel 2 flows"""
        c, cl = self._h(color), self._l(color)
        self._r(x+2, y+2, w, h, 9, "rgba(0,0,0,.05)")
        self._r(x, y, w, h, 9, cl, c, 2)
        if label:
            self._r(x+5, y+5, w-10, 22, 6, c, c)
            self._t(label, x+w//2, y+20, 12, BLANCO, "bold")
            yy = y + 36
        else:
            yy = y + h//2 + 5
        for it in items:
            self._t(it, x+w//2, yy, 14, NEGRO, "normal")
            yy += 20

    def info(self, x, y, w, h, items, color):
        c, cl = self._h(color), self._l(color)
        self._r(x, y, w, h, 9, cl, c, 2)
        yy = y + h//2 + 5
        for it in items:
            self._t(it, x+w//2, yy, 15, c, "bold")
            yy += 26

    # ========== ARROWS ==========
    def flow(self, x1, y1, x2, y2, color="AZUL", label="", lw=1.8):
        c = self._h(color)
        self.c.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{c}" stroke-width="{lw}" marker-end="url(#a-{color})"/>')
        if label:
            self._t(label, (x1+x2)//2, (y1+y2)//2-8, 11, GRIS, "bold")

    def flow_bi(self, x1, y1, x2, y2, color, t1="", t2=""):
        c = self._h(color)
        self.c.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{c}" stroke-width="1.8" marker-end="url(#a-{color})"/>')
        self.c.append(f'<line x1="{x2}" y1="{y2}" x2="{x1}" y2="{y1}" stroke="{c}" stroke-width="1.8" marker-end="url(#a-{color})"/>')
        mx, my = (x1+x2)//2, (y1+y2)//2
        if t1: self._t(t1, mx, my-9, 11, GRIS, "bold")
        if t2: self._t(t2, mx, my+19, 11, GRIS, "bold")

    def elbow(self, x1, y1, x2, y2, color="AZUL", label=""):
        c = self._h(color)
        self.c.append(f'<polyline points="{x1},{y1} {x2},{y1} {x2},{y2}" fill="none" stroke="{c}" stroke-width="1.8" marker-end="url(#a-{color})"/>')
        if label:
            self._t(label, (x1+x2)//2, y1-8, 11, GRIS, "bold")

    def vflow(self, x, y1, y2, color="AZUL"):
        self.c.append(f'<line x1="{x}" y1="{y1}" x2="{x}" y2="{y2}" stroke="{self._h(color)}" stroke-width="2" marker-end="url(#a-{color})"/>')

    def line(self, x1, y1, x2, y2):
        self.c.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#E0E0E0" stroke-width="1"/>')

    # ========== LEGEND ==========
    def legend(self):
        lx, ly = self.w-230, self.h-105
        self._r(lx, ly, 220, 95, 7, BLANCO, "#BDBDBD", 1)
        self._t("NOTACION DFD (Yourdon/DeMarco)", lx+110, ly+18, 11, GRIS, "bold")
        # Entity
        self._r(lx+12, ly+28, 34, 20, 4, BLANCO, GRIS, 1.5)
        self._t("Entidad externa", lx+52, ly+42, 10, GRIS, "normal", "start")
        # Process
        self._r(lx+12, ly+54, 34, 20, 7, AZUL_L, AZUL, 1.5)
        self._t("Proceso", lx+52, ly+68, 10, GRIS, "normal", "start")
        # Data store
        self.c.append(f'<line x1="{lx+148}" y1="{ly+28}" x2="{lx+148}" y2="{ly+48}" stroke="{PURPURA}" stroke-width="2"/>')
        self.c.append(f'<line x1="{lx+148}" y1="{ly+28}" x2="{lx+182}" y2="{ly+28}" stroke="{PURPURA}" stroke-width="2"/>')
        self.c.append(f'<line x1="{lx+148}" y1="{ly+48}" x2="{lx+182}" y2="{ly+48}" stroke="{PURPURA}" stroke-width="2"/>')
        self._t("Almacen datos", lx+187, ly+42, 10, GRIS, "normal", "start")
        # Flow
        self.c.append(f'<line x1="{lx+148}" y1="{ly+65}" x2="{lx+180}" y2="{ly+65}" stroke="{GRIS}" stroke-width="1.5" marker-end="url(#a-GRIS)"/>')
        self._t("Flujo de datos", lx+187, ly+69, 10, GRIS, "normal", "start")
        if "a-GRIS" not in "".join(self.c):
            pass  # marker already in defs if we add it

def marker_gris():
    return f'<marker id="a-GRIS" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0L10 5L0 10z" fill="{GRIS}"/></marker>'

# ====================================================================
# DOC1: NIVEL 0 (CONTEXTO) + NIVEL 1 (PROCESOS)
# ====================================================================
def doc1():
    W, H = 900, 900
    s = SVG(W, H)
    s.title("DIAGRAMA DE FLUJO DE DATOS - NIVEL 0 (CONTEXTO)")

    s.entity(35, 75, 155, 62, "PACIENTE", "AZUL")
    s.entity(W-190, 75, 155, 62, "MEDICO", "VERDE")
    s.process(300, 64, 300, 70, "SALU NIC", "Aplicacion de Salud", ["y Bienestar"], "AZUL")

    s.flow_bi(190, 102, 300, 94, "AZUL", "credenciales, datos del perfil", "confirmacion, ficha medica")
    s.flow_bi(600, 94, W-190, 102, "AZUL", "disponibilidad, diagnosticos", "confirmacion, datos paciente")

    s.line(30, 168, W-30, 168)
    s.subtitle("DIAGRAMA DE FLUJO DE DATOS - NIVEL 1", 175)

    # Top row: P1-P3
    pw, ph, gp = 195, 148, 25
    tops = [
        ("P1", "REGISTRO E INICIO", "DE SESION",
         ["  - usuario + password", "  - validar credenciales", "  - acceso al menu"], "AZUL"),
        ("P2", "GESTION DE", "MEDICAMENTOS",
         ["  - nombre del medicamento", "  - dosis, frecuencia", "  - horario de toma"], "VERDE"),
        ("P3", "GESTION DE CITAS", "MEDICAS",
         ["  - paciente, doctor", "  - especialidad, fecha", "  - disponibilidad"], "NARANJA"),
    ]
    for i, (pid, t1, t2, items, c) in enumerate(tops):
        x = 30+i*(pw+gp)
        s.process(x, 222, pw, ph, pid, f"{t1} {t2}", items, c)

    # Bottom: P4-P5
    pw2 = (W-185-gp)//2
    bots = [
        ("P4", "GENERACION DE", "RECORDATORIOS",
         ["  - alerta de cita medica", "  - alarma de medicamento", "  - notificacion push"], "ROJO"),
        ("P5", "ADMINISTRACION", "DE PERFIL MEDICO",
         ["  - datos personales", "  - grupo sanguineo", "  - ficha medica"], "PURPURA"),
    ]
    for i, (pid, t1, t2, items, c) in enumerate(bots):
        x = 30+i*(pw2+gp)
        s.process(x, 400, pw2, ph, pid, f"{t1} {t2}", items, c)

    # BD Yourdon open-style
    bdx, bdw = W-170, 150
    s.datastore(bdx, 222, bdw, 326, "ALMACEN DE DATOS",
                ["Usuarios", "Medicamentos", "Citas", "Perfiles Medicos"], "PURPURA")

    # Flows: process right edge -> BD left edge (elbow)
    s.elbow(225, 296, bdx, 248, "AZUL")
    s.elbow(445, 296, bdx, 315, "VERDE")
    s.elbow(665, 296, bdx, 382, "NARANJA")
    s.elbow(30+pw2, 474, bdx, 445, "ROJO")
    s.elbow(30+pw2+gp+pw2, 474, bdx, 510, "PURPURA")

    # Entity flows to Nivel1
    s.flow(112, 137, 112, 218, "AZUL", "datos del paciente")
    s.flow(W-112, 137, W-112, 296, "AZUL", "informacion medica")

    s.legend()
    s.save(os.path.join(OUT, "DFD_Documento_1.svg"))
    print("  Doc1 OK")

# ====================================================================
# DOC2: NIVEL 2 - P1 + P2
# ====================================================================
def doc2():
    W, H = 900, 720
    s = SVG(W, H)
    s.title("DIAGRAMA DE FLUJO DE DATOS - NIVEL 2 (P1-P2)")

    # ---- P1 ----
    c1, bw = 210, 250
    s.subtitle("P1. REGISTRO E INICIO DE SESION", 52)

    p1 = [
        ("1.1 Registrarse", ["nombre, email, password"], 95, 56),
        ("1.2 Validar Password", [">= 8 caracteres; confirmar"], 175, 54),
        ("1.3 Guardar Medicamento", ["nombre del medicamento", "dosificacion"], 253, 58),
        ("1.4 Iniciar Sesion", ["usuario + password"], 335, 54),
    ]
    for label, items, y, h in p1:
        s.step(c1-bw//2, y, bw, h, label, items, "AZUL")
    for i in range(len(p1)-1):
        _, _, y, h = p1[i]; _, _, yn, _ = p1[i+1]
        s.vflow(c1, y+h+4, yn-4, "AZUL")

    s.vflow(c1, 389, 416, "AZUL")
    s.step(c1-bw//2, 416, bw, 54, "1.5 Validar Credenciales", ["credenciales correctas?"], "AZUL")
    s.vflow(c1, 470, 494, "AZUL")

    s.step(c1-bw//2, 494, 120, 56, "SI -> Acceso", ["Menu Principal"], "VERDE")
    s.step(c1-bw//2+130, 494, 120, 68, "NO -> Bloquear", ["intentos < 3?", "bloquear cuenta"], "ROJO")

    s.datastore(c1+bw//2+15, 95, 100, 80, "BD USUARIOS", ["credenciales", "perfiles"], "PURPURA")
    s.flow(c1+bw//2, 125, c1+bw//2+15, 125, "PURPURA")

    # ---- P2 ----
    c2, bw2 = 665, 255
    s.subtitle("P2. GESTION DE MEDICAMENTOS", 52)

    p2 = [
        ("2.1 Ingresar Datos", ["nombreMedicamento, dosis, frecuencia", "horaInicio, duracion (dias)"], 95, 60),
        ("2.2 Validar Datos", ["todos los campos completos?", "duracion > 0?"], 180, 56),
        ("2.3 Mostrar Resumen", ["Medicamento, dosis, frecuencia", "Horario programado"], 260, 56),
        ("2.4 Confirmar Horario", ["desea confirmar? SI / NO"], 340, 54),
    ]
    for label, items, y, h in p2:
        s.step(c2-bw2//2, y, bw2, h, label, items, "VERDE")
    for i in range(len(p2)-1):
        _, _, y, h = p2[i]; _, _, yn, _ = p2[i+1]
        s.vflow(c2, y+h+4, yn-4, "VERDE")

    s.vflow(c2, 394, 420, "VERDE")
    s.step(c2-bw2//2, 420, bw2, 56, "2.5 Confirmar", ["SI -> Guardar en BD Medicamentos", "NO -> Cancelar operacion"], "NARANJA")

    s.datastore(c2+bw2//2+15, 95, 100, 80, "BD MEDICAMENTOS", ["nombre, dosis", "horarios"], "PURPURA")
    s.flow(c2+bw2//2, 125, c2+bw2//2+15, 125, "PURPURA")

    s.legend()
    s.save(os.path.join(OUT, "DFD_Documento_2.svg"))
    print("  Doc2 OK")

# ====================================================================
# DOC3: NIVEL 2 - P3 + P4 + P5
# ====================================================================
def doc3():
    W, H = 950, 780
    s = SVG(W, H)
    s.title("DIAGRAMA DE FLUJO DE DATOS - NIVEL 2 (P3-P5)")

    # ---- P3 ----
    c1, bw = 175, 230
    s.subtitle("P3. GESTION DE CITAS MEDICAS", 52)

    p3 = [
        ("3.1 Solicitar Renovacion", ["nombrePaciente, doctorActual", "especialidadActual"], 88, 52),
        ("3.2 Validar Datos", ["campos obligatorios completos?"], 158, 46),
        ("3.3 Consultar Disponibilidad", ["buscar en BD Citas", "verificar horarios libres"], 222, 52),
        ("3.4 Ingresar Nueva Cita", ["fechaNuevaCita", "horaNuevaCita"], 292, 48),
        ("3.5 Validar Fecha/Hora", ["fecha valida?  hora valida?"], 358, 46),
        ("3.6 Confirmar Cita", ["mostrar resumen", "confirmar? SI / NO"], 422, 52),
    ]
    for label, items, y, h in p3:
        s.step(c1-bw//2, y, bw, h, label, items, "NARANJA")
    for i in range(len(p3)-1):
        _, _, y, h = p3[i]; _, _, yn, _ = p3[i+1]
        s.vflow(c1, y+h+4, yn-4, "NARANJA")

    s.vflow(c1, 474, 498, "NARANJA")
    s.datastore(c1-bw//2, 498, bw, 56, "BD CITAS", ["citas registradas"], "PURPURA")

    s.elbow(c1+bw//2, 88+52//2, c1+bw//2+35, 88+52//2, "ROJO", "Error: datos incompletos")
    s.elbow(c1+bw//2, 358+46//2, c1+bw//2+35, 358+46//2, "ROJO", "Error: fecha/hora invalida")

    # ---- P4 ----
    c2, bw2 = 470, 200
    s.subtitle("P4. GENERACION DE RECORDATORIOS", 52)

    p4 = [
        ("4.1 Ingresar Datos Cita", ["fechaCita, horaCita", "nombrePaciente, doctor"], 88, 52),
        ("4.2 Validar Horario", ["hora entre 08:00 - 17:00?"], 162, 46),
        ("4.3 Generar Recordatorio", ["mostrar datos de la cita", "programar alarma"], 230, 52),
    ]
    for label, items, y, h in p4:
        s.step(c2-bw2//2, y, bw2, h, label, items, "ROJO")
    for i in range(len(p4)-1):
        _, _, y, h = p4[i]; _, _, yn, _ = p4[i+1]
        s.vflow(c2, y+h+4, yn-4, "ROJO")

    s.vflow(c2, 282, 306, "ROJO")
    s.step(c2-75, 306, 150, 50, "RECORDATORIO ACTIVO", ["notificacion push", "alarma de audio"], "VERDE")

    # ---- P5 ----
    c3, bw3 = 750, 240
    s.subtitle("P5. ADMINISTRACION DE PERFIL MEDICO", 52)

    p5 = [
        ("5.1 Datos Personales", ["nombre, apellido", "fecha de nacimiento"], 88, 48),
        ("5.2 Grupo Sanguineo", ["A+, O-, AB+, B+, etc."], 154, 44),
        ("5.3 Alergias", ["registrar alergias conocidas"], 216, 44),
        ("5.4 Antecedentes Medicos", ["hipertension, diabetes", "cirugias previas, otros"], 278, 48),
        ("5.5 Contacto Emergencia", ["nombre del contacto", "telefono"], 344, 46),
        ("5.6 Mostrar Ficha Medica", ["datos completos del perfil", "confirmar? SI / NO"], 408, 52),
    ]
    for label, items, y, h in p5:
        s.step(c3-bw3//2, y, bw3, h, label, items, "PURPURA")
    for i in range(len(p5)-1):
        _, _, y, h = p5[i]; _, _, yn, _ = p5[i+1]
        s.vflow(c3, y+h+4, yn-4, "PURPURA")

    s.vflow(c3, 460, 484, "PURPURA")
    s.step(c3-85, 484, 170, 50, "FICHA MEDICA", ["emergencias", "monitoreo de salud"], "VERDE")

    s.legend()
    s.save(os.path.join(OUT, "DFD_Documento_3.svg"))
    print("  Doc3 OK")

# ====================================================================
# DOC4: ENTRADAS / SALIDAS
# ====================================================================
def doc4():
    W, H = 850, 560
    s = SVG(W, H)
    s.title("ENTRADAS Y SALIDAS DEL SISTEMA")

    s.subtitle("ENTRADAS (INPUTS)", 55)

    inputs = [
        ("Registro de usuario y contrasena", "AZUL"),
        ("Datos de medicamento (nombre, dosis, frecuencia)", "VERDE"),
        ("Solicitud de cita medica", "NARANJA"),
        ("Perfil medico (grupo sanguineo, alergias, antecedentes)", "PURPURA"),
    ]
    for i, (txt, c) in enumerate(inputs):
        s.info(35 + (i % 2)*400, 98 + (i//2)*62, 370, 50, [txt], c)

    s.process(325, 240, 200, 50, "SALU NIC", "Sistema", ["procesa datos"], "AZUL")

    s.flow(220, 148, 220, 185, "AZUL")
    s.flow(220, 185, 325, 240, "AZUL")
    s.flow(620, 148, 620, 185, "AZUL")
    s.flow(620, 185, 525, 240, "AZUL")

    s.subtitle("SALIDAS (OUTPUTS)", 310)

    outputs = [
        ("Confirmacion de registro", "AZUL"),
        ("Horario de medicamentos", "VERDE"),
        ("Recordatorio de cita medica", "NARANJA"),
        ("Renovacion de citas medicas", "ROJO"),
        ("Ficha medica de emergencia", "PURPURA"),
    ]
    for i, (txt, c) in enumerate(outputs):
        s.info(35 + (i % 2)*400, 360 + (i//2)*62, 370, 50, [txt], c)

    s.flow(325, 290, 220, 315, "AZUL")
    s.flow(220, 315, 220, 360, "AZUL")
    s.flow(525, 290, 620, 315, "AZUL")
    s.flow(620, 315, 620, 360, "AZUL")

    s.legend()
    s.save(os.path.join(OUT, "DFD_Documento_4.svg"))
    print("  Doc4 OK")

# ====================================================================
# ADD GRIS marker to saves
# ====================================================================
# Monkey-patch save to include GRIS marker in defs
_orig_save = SVG.save
def _patched_save(self, path):
    gris_marker = f'<marker id="a-GRIS" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0L10 5L0 10z" fill="{GRIS}"/></marker>'
    with open(path,"w",encoding="utf-8") as f:
        defs = []
        for col in ["AZUL","VERDE","NARANJA","ROJO","PURPURA"]:
            hx = self._h(col)
            defs.append(f'<marker id="a-{col}" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0L10 5L0 10z" fill="{hx}"/></marker>')
        defs.append(gris_marker)
        defs.append('<filter id="sh"><feDropShadow dx="2" dy="3" stdDeviation="3" flood-color="#000" flood-opacity=".10"/></filter>')
        defs.append('<filter id="sh2"><feDropShadow dx="1" dy="2" stdDeviation="2" flood-color="#000" flood-opacity=".08"/></filter>')
        f.write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {self.w} {self.h}"><defs>{"".join(defs)}</defs><rect width="{self.w}" height="{self.h}" fill="{FONDO}"/>{"".join(self.c)}</svg>')
SVG.save = _patched_save

print("Generando 4 diagramas DFD profesionales (notacion Yourdon)...")
doc1(); doc2(); doc3(); doc4()
print(f"\nCompletado! Archivos en: {OUT}")
