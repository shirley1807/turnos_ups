class NodoLista:
    def __init__(self, cliente):
        self.cliente = cliente  # Diccionario con DNI y nombre
        self.siguiente = None


class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    # Agregar al final de la lista
    def agregar(self, cliente):
        """Registrar un nuevo cliente recorriendo hasta el final"""
        nuevo_nodo = NodoLista(cliente)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
        # agregar: O(n) — recorrido hasta el último nodo

    # Buscar por nombre
    def buscar(self, nombre):
        """Buscar cliente por nombre; devuelve el cliente o None"""
        actual = self.cabeza
        while actual:
            if actual.cliente.get("nombre") == nombre:
                return actual.cliente
            actual = actual.siguiente
        return None
        # buscar: O(n) — recorrido en el peor caso hasta el final

    # Mostrar toda la lista
    def mostrar(self):
        """Devuelve una cadena con todos los clientes registrados"""
        elementos = []
        actual = self.cabeza
        while actual:
            dni = actual.cliente.get("dni", actual.cliente.get("DNI", ""))
            nombre = actual.cliente.get("nombre", actual.cliente.get("Nombre", ""))
            elementos.append(f"DNI: {dni}, Nombre: {nombre}")
            actual = actual.siguiente
        return "\n".join(elementos) if elementos else "Sin clientes registrados"
        # mostrar: O(n) — recorrido completo de la lista


# Prueba de la lista
if __name__ == "__main__":
    lista = ListaEnlazada()
    lista.agregar({"dni": "123", "nombre": "Ana"})
    lista.agregar({"dni": "456", "nombre": "Luis"})
    print(lista.mostrar())
    buscado = lista.buscar("Ana")
    print("Buscado:", buscado)