import os, subprocess, sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPTS = os.path.dirname(os.path.abspath(__file__))
MD = os.path.join(RAIZ, "Documento Explicativo del Código.md")
DOCX = os.path.join(RAIZ, "Documento Explicativo del Código.docx")
CARPETA = os.path.join(RAIZ, "Documento Explicativo del Código")
PDF = os.path.join(CARPETA, "Documento Explicativo del Código.pdf")


def convertir_md_a_docx():
    script = os.path.join(SCRIPTS, "md2docx.py")
    if not os.path.exists(MD):
        print(f"[Error] No se encontro: {MD}")
        return False
    print("1. Regenerando el .docx desde el .md ...")
    subprocess.run([sys.executable, script], check=True)
    return True


def convertir_docx_a_pdf():
    print("2. Generando el PDF con Word ...")
    ps = (
        "$word = New-Object -ComObject Word.Application; "
        "$word.Visible = $false; "
        "try { "
        "  $doc = $word.Documents.Open('%s'); "
        "  $doc.SaveAs([ref]'%s', [ref]17); "
        "  $doc.Close(); "
        "} finally { "
        "  $word.Quit(); "
        "}" % (DOCX, PDF)
    )
    subprocess.run(["powershell", "-NoProfile", "-Command", ps], check=True)
    print(f"Listo: {PDF}")


if __name__ == "__main__":
    os.makedirs(CARPETA, exist_ok=True)
    if not os.path.exists(DOCX):
        if not convertir_md_a_docx():
            sys.exit(1)
    convertir_docx_a_pdf()