class NodoCola:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class Cola:
    def __init__(self):
        self.cabeza = None  # Primer elemento en espera
        self.cola = None    # Último elemento en espera

    # Encolar: agregar al final por referencia directa a cola
    def enqueue(self, turno):
        """Agregar un cliente al final de la cola de espera"""
        nuevo_nodo = NodoCola(turno)
        if self.cola is None:  # Cola vacía
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo
        # enqueue: O(1) — acceso directo por referencia 'cola'

    # Desencolar: extraer desde la cabeza
    def dequeue(self):
        """Atender y remover el primer cliente; None si está vacía"""
        if self.cabeza is None:
            return None
        dato_atendido = self.cabeza.dato
        self.cabeza = self.cabeza.siguiente
        if self.cabeza is None:  # Quedó vacía
            self.cola = None
        return dato_atendido
        # dequeue: O(1) — acceso directo por referencia 'cabeza'

    def esta_vacia(self):
        return self.cabeza is None

    def ver_frente(self):
        if self.cabeza:
            return self.cabeza.dato
        return None


# Prueba de la cola
if __name__ == "__main__":
    c = Cola()
    c.enqueue({"dni": "001", "nombre": "María"})
    c.enqueue({"dni": "002", "nombre": "Pedro"})
    print("Frente:", c.ver_frente()["nombre"])
    atendido = c.dequeue()
    print("Atendido:", atendido["nombre"])
    print("Siguiente:", c.ver_frente()["nombre"])