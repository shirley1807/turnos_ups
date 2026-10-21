class NodoPila:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class Pila:
    def __init__(self):
        self.cima = None  # Referencia al tope de la pila
        self.tamano = 0

    # Apilar: se agrega al inicio (cima)
    def push(self, accion):
        """Registrar una nueva acción en el historial"""
        nuevo_nodo = NodoPila(accion)
        nuevo_nodo.siguiente = self.cima
        self.cima = nuevo_nodo
        self.tamano += 1
        # push: O(1) — solo se modifican referencias fijas

    # Desapilar: se elimina desde la cima
    def pop(self):
        """Deshacer la última acción; devuelve None si está vacía"""
        if self.cima is None:
            return None
        dato_eliminado = self.cima.dato
        self.cima = self.cima.siguiente
        self.tamano -= 1
        return dato_eliminado
        # pop: O(1) — acceso directo a la cima

    def esta_vacia(self):
        return self.cima is None

    def ver_cima(self):
        if self.cima:
            return self.cima.dato
        return None


# Prueba de la pila
if __name__ == "__main__":
    historial = Pila()
    historial.push("Registrar turno: Juan")
    historial.push("Atender turno: Juan")
    print("Última acción:", historial.ver_cima())
    deshecha = historial.pop()
    print("Acción deshecha:", deshecha)
    print("Ahora la cima es:", historial.ver_cima())
