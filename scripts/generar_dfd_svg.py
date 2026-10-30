import os
from PIL import Image, ImageDraw, ImageFont

# =====================================================
# SALUNIC - Generacion de DFD en PNG (Pillow)
# Actualizados al PROTOTIPO DE CONSOLA del 1er corte
# Entidades: Usuario, CitaMedica, Medicamento, AlmacenMedicamento
# =====================================================

OUT = "C:\\salunic-app\\diagramas_img"
os.makedirs(OUT, exist_ok=True)

# Colores
AZUL = (21, 101, 192); AZUL_L = (227, 242, 253); AZUL_O = (13, 71, 161)
VERDE = (46, 204, 113); VERDE_L = (232, 245, 233)
NARANJA = (255, 112, 67); NARANJA_L = (255, 243, 224)
ROJO = (229, 57, 53); ROJO_L = (255, 235, 238)
PURPURA = (156, 39, 176); PURPURA_L = (243, 229, 245)
FONDO = (250, 250, 250); NEGRO = (33, 33, 33); GRIS = (97, 97, 97); GRIS2 = (158, 158, 158)
BLANCO = (255, 255, 255)
COLORS = {"AZUL": (AZUL, AZUL_L), "VERDE": (VERDE, VERDE_L), "NARANJA": (NARANJA, NARANJA_L),
          "ROJO": (ROJO, ROJO_L), "PURPURA": (PURPURA, PURPURA_L)}

FONT_REG = r"C:\Windows\Fonts\segoeui.ttf"
FONT_BOLD = r"C:\Windows\Fonts\segoeuib.ttf"


def font(size, bold=False):
    return ImageFont.truetype(FONT_BOLD if bold else FONT_REG, size)


class Diagram:
    def __init__(self, w, h, title):
        self.w, self.h = w, h
        self.img = Image.new("RGB", (w, h), FONDO)
        self.d = ImageDraw.Draw(self.img)
        # Header
        self.d.rectangle([0, 0, w, 52], fill=AZUL)
        self.d.rectangle([0, 48, w, 52], fill=AZUL_O)
        tw = self.d.textlength(title, font=font(20, True))
        self.d.text(((w - tw) // 2, 14), title, font=font(20, True), fill=BLANCO)

    def subtitle(self, txt, y):
        self.d.rectangle([0, y, self.w, y + 32], fill=AZUL_O)
        tw = self.d.textlength(txt, font=font(15, True))
        self.d.text(((self.w - tw) // 2, y + 8), txt, font=font(15, True), fill=BLANCO)

    def entity(self, x, y, w, h, label, color="AZUL"):
        c, _ = COLORS[color]
        self.d.rectangle([x + 3, y + 3, x + 3 + w, y + 3 + h], fill=(0, 0, 0, 20))
        self.d.rounded_rectangle([x, y, x + w, y + h], 6, fill=BLANCO, outline=c, width=3)
        tw = self.d.textlength(label, font=font(15, True))
        self.d.text((x + w / 2 - tw / 2, y + h / 2 - 10), label, font=font(15, True), fill=c)

    def process(self, x, y, w, h, pid, title, items, color="AZUL"):
        c, cl = COLORS[color]
        self.d.rounded_rectangle([x, y, x + w, y + h], 12, fill=cl, outline=c, width=3)
        self.d.rounded_rectangle([x + 6, y + 6, x + w - 6, y + 32], 7, fill=c, outline=c)
        tw = self.d.textlength(pid, font=font(13, True))
        self.d.text((x + w / 2 - tw / 2, y + 10), pid, font=font(13, True), fill=BLANCO)
        tw = self.d.textlength(title, font=font(14, True))
        self.d.text((x + w / 2 - tw / 2, y + 40), title, font=font(14, True), fill=c)
        yy = y + 66
        for it in items:
            self.d.text((x + 18, yy), it, font=font(11), fill=NEGRO)
            yy += 20

    def datastore(self, x, y, w, h, label, items, color="PURPURA"):
        c, cl = COLORS[color]
        self.d.rectangle([x, y, x + w, y + h], fill=cl)
        # Yourdon: open right side (left + top + bottom lines)
        self.d.line([x, y, x, y + h], fill=c, width=3)
        self.d.line([x, y, x + w - 8, y], fill=c, width=3)
        self.d.line([x, y + h, x + w - 8, y + h], fill=c, width=3)
        tw = self.d.textlength(label, font=font(12, True))
        self.d.text((x + w / 2 - 4 - tw / 2, y + 6), label, font=font(12, True), fill=c)
        yy = y + 28
        for it in items:
            tw = self.d.textlength(it, font=font(12, True))
            self.d.text((x + w / 2 - 4 - tw / 2, yy), it, font=font(12, True), fill=c)
            yy += 18

    def step(self, x, y, w, h, label, items, color):
        c, cl = COLORS[color]
        self.d.rounded_rectangle([x, y, x + w, y + h], 9, fill=cl, outline=c, width=3)
        if label:
            self.d.rounded_rectangle([x + 5, y + 5, x + w - 5, y + 27], 6, fill=c, outline=c)
            tw = self.d.textlength(label, font=font(12, True))
            self.d.text((x + w / 2 - tw / 2, y + 9), label, font=font(12, True), fill=BLANCO)
            yy = y + 36
        else:
            yy = y + h / 2 + 2
        for it in items:
            tw = self.d.textlength(it, font=font(12))
            self.d.text((x + w / 2 - tw / 2, yy), it, font=font(12), fill=NEGRO)
            yy += 18

    def info(self, x, y, w, h, items, color):
        c, cl = COLORS[color]
        self.d.rounded_rectangle([x, y, x + w, y + h], 9, fill=cl, outline=c, width=3)
        yy = y + h / 2 - 8
        for it in items:
            tw = self.d.textlength(it, font=font(13, True))
            self.d.text((x + w / 2 - tw / 2, yy), it, font=font(13, True), fill=c)
            yy += 24

    def flow(self, x1, y1, x2, y2, color="AZUL", label=""):
        c, _ = COLORS.get(color, (GRIS, GRIS))
        self.d.line([x1, y1, x2, y2], fill=c, width=3)
        # arrowhead
        import math
        ang = math.atan2(y2 - y1, x2 - x1)
        l1 = (x2 - 10 * math.cos(ang - 0.45), y2 - 10 * math.sin(ang - 0.45))
        l2 = (x2 - 10 * math.cos(ang + 0.45), y2 - 10 * math.sin(ang + 0.45))
        self.d.line([x2, y2, l1], fill=c, width=3)
        self.d.line([x2, y2, l2], fill=c, width=3)
        if label:
            tw = self.d.textlength(label, font=font(11, True))
            self.d.text(((x1 + x2) / 2 - tw / 2, (y1 + y2) / 2 - 18), label, font=font(11, True), fill=GRIS)

    def flow_bi(self, x1, y1, x2, y2, color, t1="", t2=""):
        self.flow(x1, y1, x2, y2, color, t1)
        self.flow(x2, y2, x1, y1, color, t2)

    def elbow(self, x1, y1, x2, y2, color="AZUL", label=""):
        c, _ = COLORS[color]
        self.d.line([x1, y1, x2, y1], fill=c, width=3)
        self.d.line([x2, y1, x2, y2], fill=c, width=3)
        if label:
            tw = self.d.textlength(label, font=font(11, True))
            self.d.text(((x1 + x2) / 2 - tw / 2, y1 - 18), label, font=font(11, True), fill=GRIS)

    def vflow(self, x, y1, y2, color="AZUL"):
        self.flow(x, y1, x, y2, color)

    def hline(self, x1, x2, y):
        self.d.line([x1, y, x2, y], fill=(224, 224, 224), width=2)

    def legend(self):
        lx, ly = self.w - 235, self.h - 108
        self.d.rounded_rectangle([lx, ly, lx + 225, ly + 98], 7, fill=BLANCO, outline=(189, 189, 189), width=2)
        tw = self.d.textlength("NOTACION DFD (Yourdon/DeMarco)", font=font(10, True))
        self.d.text((lx + 112 - tw / 2, ly + 6), "NOTACION DFD (Yourdon/DeMarco)", font=font(10, True), fill=GRIS)
        self.d.rounded_rectangle([lx + 12, ly + 26, lx + 46, ly + 46], 4, fill=BLANCO, outline=GRIS, width=2)
        self.d.text((lx + 52, ly + 29), "Entidad externa", font=font(10), fill=GRIS)
        self.d.rounded_rectangle([lx + 12, ly + 52, lx + 46, ly + 72], 7, fill=AZUL_L, outline=AZUL, width=2)
        self.d.text((lx + 52, ly + 55), "Proceso", font=font(10), fill=GRIS)

    def save(self, name):
        self.img.save(os.path.join(OUT, name))
        print("  Guardado:", name)


# ====================================================================
# DOC 1: NIVEL 0 (CONTEXTO) + NIVEL 1
# ====================================================================
def doc1():
    W, H = 900, 860
    d = Diagram(W, H, "SALUNIC - DFD NIVEL 0 (CONTEXTO)")
    d.entity(30, 80, 160, 60, "USUARIO", "AZUL")
    d.entity(W - 195, 80, 160, 60, "ADMIN", "VERDE")
    d.process(300, 72, 300, 80, "SALUNIC", "Sistema de Salud", ["y Bienestar (Consola)"], "AZUL")
    d.flow_bi(190, 108, 300, 100, "AZUL", "datos, opciones", "resultados, mensajes")
    d.flow_bi(600, 100, W - 195, 108, "VERDE", "gestion de datos", "respuesta")
    d.hline(30, W - 30, 168)
    d.subtitle("DFD NIVEL 1 - PROCESOS PRINCIPALES", 175)
    pw, ph, gp = 195, 150, 20
    tops = [
        ("P1", "GESTION DE USUARIOS", ["  - registrar", "  - buscar (email)", "  - actualizar / eliminar"], "AZUL"),
        ("P2", "GESTION DE CITAS", ["  - registrar", "  - buscar (medico)", "  - actualizar / eliminar"], "NARANJA"),
        ("P3", "GESTION DE MEDICAMENTOS", ["  - registrar", "  - buscar (nombre)", "  - actualizar / eliminar"], "VERDE"),
    ]
    for i, (pid, t, items, c) in enumerate(tops):
        x = 25 + i * (pw + gp)
        d.process(x, 250, pw, ph, pid, t, items, c)
    d.process(25, 430, pw * 2 + gp, ph, "P4", "GESTION DE ALMACEN / INVENTARIO",
              ["  - registrar stock (medicamento_id, cantidad, vencimiento)",
               "  - buscar por medicamento", "  - actualizar cantidad / eliminar"], "ROJO")
    bdx, bdw = 700, 175
    d.datastore(bdx, 250, bdw, 335, "ALMACEN DE DATOS",
                ["Usuarios", "Citas", "Medicamentos", "Almacen (stock)"], "PURPURA")
    d.elbow(220, 320, bdx, 285, "AZUL")
    d.elbow(435, 320, bdx, 345, "NARANJA")
    d.elbow(650, 320, bdx, 405, "VERDE")
    d.elbow(445, 480, bdx, 440, "ROJO")
    d.flow(110, 140, 110, 250, "AZUL", "datos del usuario")
    d.flow(W - 110, 140, W - 110, 405, "VERDE", "datos del sistema")
    d.legend()
    d.save("DFD_Documento_1.png")


# ====================================================================
# DOC 2: NIVEL 2 - P1 (USUARIOS) + P2 (CITAS)
# ====================================================================
def doc2():
    W, H = 900, 760
    d = Diagram(W, H, "SALUNIC - DFD NIVEL 2 (P1 USUARIOS  y  P2 CITAS)")
    c1, bw = 210, 250
    d.subtitle("P1. GESTION DE USUARIOS", 52)
    p1 = [
        ("1.1 Ingresar Datos", ["nombre, email, password, telefono"], 95, 54),
        ("1.2 Validar Datos", ["nombre: letras; email valido", "password >= 4; telefono digitos"], 175, 58),
        ("1.3 Agregar a la Lista", ["id unico = max + 1", "usuarios.append(Usuario(...))"], 259, 58),
        ("1.4 Buscar / Actualizar / Eliminar", ["buscar por email", "borrar: usuarios.remove"], 343, 56),
    ]
    for label, items, y, h in p1:
        d.step(c1 - bw / 2, y, bw, h, label, items, "AZUL")
    for i in range(len(p1) - 1):
        _, _, y, h = p1[i]; _, _, yn, _ = p1[i + 1]
        d.vflow(c1, y + h + 4, yn - 4, "AZUL")
    d.datastore(c1 + bw / 2 + 20, 95, 110, 90, "BD USUARIOS", ["lista:", "usuarios = []"], "PURPURA")
    d.flow(c1 + bw / 2, 150, c1 + bw / 2 + 20, 150, "PURPURA")
    c2, bw2 = 665, 260
    d.subtitle("P2. GESTION DE CITAS MEDICAS", 52)
    p2 = [
        ("2.1 Ingresar Datos", ["paciente_id, medico_id", "especialidad, fecha, hora, lugar"], 95, 58),
        ("2.2 Validar Datos", ["fecha real DD/MM/AAAA", "hora HH:MM"], 179, 52),
        ("2.3 Agregar a la Lista", ["id unico = max + 1", "citas.append(CitaMedica(...))"], 255, 58),
        ("2.4 Buscar / Actualizar / Eliminar", ["buscar por medico_id", "actualizar fecha/hora/lugar"], 337, 56),
    ]
    for label, items, y, h in p2:
        d.step(c2 - bw2 / 2, y, bw2, h, label, items, "NARANJA")
    for i in range(len(p2) - 1):
        _, _, y, h = p2[i]; _, _, yn, _ = p2[i + 1]
        d.vflow(c2, y + h + 4, yn - 4, "NARANJA")
    d.datastore(c2 + bw2 / 2 + 20, 95, 110, 90, "BD CITAS", ["lista:", "citas = []"], "PURPURA")
    d.flow(c2 + bw2 / 2, 150, c2 + bw2 / 2 + 20, 150, "PURPURA")
    d.legend()
    d.save("DFD_Documento_2.png")


# ====================================================================
# DOC 3: NIVEL 2 - P3 (MEDICAMENTOS) + P4 (ALMACEN)
# ====================================================================
def doc3():
    W, H = 900, 760
    d = Diagram(W, H, "SALUNIC - DFD NIVEL 2 (P3 MEDICAMENTOS  y  P4 ALMACEN)")
    c1, bw = 210, 250
    d.subtitle("P3. GESTION DE MEDICAMENTOS", 52)
    p3 = [
        ("3.1 Ingresar Datos", ["nombre, dosis, frecuencia", "presentacion"], 95, 56),
        ("3.2 Validar Datos", ["nombre: letras", "frecuencia: texto", "dosis no vacia"], 177, 62),
        ("3.3 Agregar a la Lista", ["id unico = max + 1", "medicamentos.append(...)"], 265, 56),
        ("3.4 Buscar / Actualizar / Eliminar", ["buscar por nombre", "actualizar dosis/frecuencia"], 345, 56),
    ]
    for label, items, y, h in p3:
        d.step(c1 - bw / 2, y, bw, h, label, items, "VERDE")
    for i in range(len(p3) - 1):
        _, _, y, h = p3[i]; _, _, yn, _ = p3[i + 1]
        d.vflow(c1, y + h + 4, yn - 4, "VERDE")
    d.datastore(c1 + bw / 2 + 20, 95, 110, 90, "BD MEDICAMENTOS", ["lista:", "medicamentos = []"], "PURPURA")
    d.flow(c1 + bw / 2, 150, c1 + bw / 2 + 20, 150, "PURPURA")
    c2, bw2 = 665, 260
    d.subtitle("P4. GESTION DE ALMACEN / INVENTARIO", 52)
    p4 = [
        ("4.1 Ingresar Datos", ["medicamento_id, cantidad", "fecha_vencimiento"], 95, 56),
        ("4.2 Validar Datos", ["medicamento_id entero", "cantidad >= 0", "fecha real"], 177, 62),
        ("4.3 Agregar a la Lista", ["id unico = max + 1", "almacen.append(...)"], 265, 56),
        ("4.4 Buscar / Actualizar / Eliminar", ["buscar por medicamento_id", "actualizar cantidad/fecha"], 345, 56),
    ]
    for label, items, y, h in p4:
        d.step(c2 - bw2 / 2, y, bw2, h, label, items, "ROJO")
    for i in range(len(p4) - 1):
        _, _, y, h = p4[i]; _, _, yn, _ = p4[i + 1]
        d.vflow(c2, y + h + 4, yn - 4, "ROJO")
    d.datastore(c2 + bw2 / 2 + 20, 95, 110, 90, "BD ALMACEN", ["lista:", "almacen = []"], "PURPURA")
    d.flow(c2 + bw2 / 2, 150, c2 + bw2 / 2 + 20, 150, "PURPURA")
    d.legend()
    d.save("DFD_Documento_3.png")


# ====================================================================
# DOC 4: MODELO DE ENTIDADES + OPERACIONES
# ====================================================================
def doc4():
    W, H = 850, 640
    d = Diagram(W, H, "SALUNIC - MODELO DE ENTIDADES Y OPERACIONES")
    d.subtitle("ENTIDADES (@dataclass) y sus RELACIONES", 55)
    d.datastore(30, 90, 190, 120, "MEDICAMENTO", ["id", "nombre", "dosis", "frecuencia"], "VERDE")
    d.datastore(330, 90, 190, 120, "ALMACEN", ["id", "medicamento_id", "cantidad", "vencimiento"], "ROJO")
    d.datastore(620, 90, 190, 120, "USUARIO", ["id", "nombre", "email", "password"], "AZUL")
    d.datastore(330, 300, 190, 120, "CITA MEDICA", ["id", "paciente_id", "medico_id", "fecha", "hora"], "NARANJA")
    d.flow(220, 150, 330, 110, "ROJO", "medicamento_id -> id")
    d.elbow(230, 170, 330, 280, "AZUL", "paciente_id")
    d.hline(30, 820, 300)
    d.subtitle("OPERACIONES CRUD por entidad", 330)
    d.info(60, 370, 330, 60, ["Registrar  |  Buscar"], "AZUL")
    d.info(460, 370, 330, 60, ["Actualizar  |  Eliminar"], "VERDE")
    d.info(60, 460, 330, 60, ["Contar  |  Listar"], "NARANJA")
    d.legend()
    d.save("DFD_Documento_4.png")


print("Generando 4 DFD actualizados al prototipo de consola (PNG)...")
doc1(); doc2(); doc3(); doc4()
print(f"\nCompletado! PNG en: {OUT}")
