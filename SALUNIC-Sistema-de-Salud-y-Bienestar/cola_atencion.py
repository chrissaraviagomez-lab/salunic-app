import heapq


class ColaAtencion:
    """Implementacion de una Cola CON PRIORIDAD para gestionar la atencion de citas
    Prioridad: 1 = Adulto Mayor (ATENCION PRIORITARIA) | 2 = Normal
    """
    def __init__(self):
        self.cola = []
        self.contador = 0
        self.turno_global = 0

    def encolar(self, item, es_adulto_mayor=False):
        """Agregar elemento a la cola con prioridad"""
        self.contador += 1
        self.turno_global += 1
        # Prioridad: 0 = Mayor prioridad (Adulto Mayor), 1 = Normal
        if es_adulto_mayor:
            prioridad = 0
            tipo = "ADULTO MAYOR (PRIORITARIO)"
        else:
            prioridad = 1
            tipo = "NORMAL"
        item['turno'] = self.turno_global
        item['prioridad'] = tipo
        # (prioridad, turno_global, item) - heapq usa el primer elemento para ordenar
        heapq.heappush(self.cola, (prioridad, self.turno_global, item))
        print(f"  [COLA] Paciente {item.get('paciente', '')} agregado. Turno #{self.turno_global} | {tipo}")

    def desencolar(self):
        """Atender (eliminar) elemento con MAYOR PRIORIDAD"""
        if self.esta_vacia():
            print("  [COLA] No hay pacientes en espera para atender.")
            return None
        prioridad, turno, atendido = heapq.heappop(self.cola)
        print(f"  [COLA] ATENDIENDO -> {atendido.get('prioridad')} | Paciente: {atendido.get('paciente', '')} | Cita ID: {atendido.get('cita_id', '')} | Turno: {atendido.get('turno')}")
        return atendido

    def mostrar_cola(self):
        """Mostrar todos los pacientes en espera con su prioridad"""
        if self.esta_vacia():
            print("  [COLA] La cola de atencion esta vacia.")
            return
        print("\n--- COLA DE ATENCION CON PRIORIDAD ---")
        print("  (Adulto Mayor = Prioritario | Se atiende primero sin importar orden de llegada)")
        # Copiar y ordenar para mostrar sin alterar la cola
        temp = sorted(self.cola, key=lambda x: (x[0], x[1]))
        for i, (prio, turno, item) in enumerate(temp, 1):
            print(f"  {i}. [{item.get('prioridad')}] Turno: {item.get('turno')} | Paciente: {item.get('paciente')} | Cita ID: {item.get('cita_id')} | Hora: {item.get('hora')}")
        print(f"\n  Total en espera: {self.tamanio()}")

    def tamanio(self):
        return len(self.cola)

    def esta_vacia(self):
        return len(self.cola) == 0


# Instancia global para usar en todo el programa
cola_atencion = ColaAtencion()
