def busqueda_lineal(lista, criterio, atributo):
    """
    Implementacion de BUSQUEDA LINEAL
    Recorre elemento por elemento hasta encontrar coincidencia
    """
    resultados = []
    if not lista:
        return resultados

    for elemento in lista:
        valor = getattr(elemento, atributo, None)
        if valor is None:
            continue

        # Comparacion por igualdad (case insensitive para strings)
        if isinstance(valor, str) and isinstance(criterio, str):
            if valor.lower() == criterio.lower():
                resultados.append(elemento)
        elif valor == criterio:
            resultados.append(elemento)

    return resultados


def busqueda_lineal_por_email(usuarios, email):
    """Busqueda lineal especifica para usuarios por email"""
    for u in usuarios:
        if u.email.lower() == email.lower():
            return u
    return None


def busqueda_lineal_citas_por_medico(citas, medico_id):
    """Busqueda lineal para filtrar citas por medico_id"""
    encontrados = []
    for c in citas:
        if c.medico_id == medico_id:
            encontrados.append(c)
    return encontrados


def busqueda_lineal_medicamento_por_nombre(medicamentos, nombre):
    """Busqueda lineal para filtrar medicamentos por nombre"""
    encontrados = []
    for m in medicamentos:
        if m.nombre.lower() == nombre.lower():
            encontrados.append(m)
    return encontrados
