from docx import Document
doc = Document(r'D:\Defensa\Plantilla Informe Final Integrador II.docx')
for i in range(232, 290):
    p = doc.paragraphs[i]
    t = p.text.strip().replace('\n',' ')
    st = p.style.name if p.style else ''
    if t or st.lower().startswith('heading'):
        print(f'{i}||{st}||{t[:260]}')
