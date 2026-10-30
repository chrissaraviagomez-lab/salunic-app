VERDE = "#2ECC71"
FUCSIA = "#E91E8C"
ROSADO = "#F48FB1"
AZUL = "#1565C0"
CELESTE = "#4FC3F7"
AMARILLO = "#F9A825"
NARANJA = "#FF7043"
BLANCO = "#FFFFFF"
AZUL_NOCHE = "#0A2342"
VERDE_OSCURO = "#062A1A"
TEXTO_CLARO = "#999999"
TEXTO_OSCURO = "#333333"
TEXTO_GRIS = "#777777"

GRADIENT_COLORS = ["#0A2342", "#0D3B7A", "#0A4D2E", "#062A1A"]

WIDTH = 375
HEIGHT = 812

def rounded_card(canvas, x, y, w, h, r=16, **kwargs):
    """Alias de create_rounded_rect para tarjetas."""
    return create_rounded_rect(canvas, x, y, x + w, y + h, r, **kwargs)

def create_rounded_rect(canvas, x1, y1, x2, y2, r, **kwargs):
    """Dibuja un rectangulo redondeado en un Canvas y devuelve su id."""
    pts = [x1+r, y1, x2-r, y1, x2, y1, x2, y1+r,
           x2, y2-r, x2, y2, x2-r, y2, x1+r, y2,
           x1, y2, x1, y2-r, x1, y1+r, x1, y1]
    return canvas.create_polygon(pts, smooth=True, **kwargs)
