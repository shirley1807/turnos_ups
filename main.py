from pila import Pila
from cola import Cola
from lista import ListaEnlazada


def main():
    # Inicialización de estructuras
    historial = Pila()
    cola_turnos = Cola()
    clientes_registrados = ListaEnlazada()

    print("=== Sistema de Gestión de Turnos - Taller CarUPS ===")
    while True:
        print("\n----- MENÚ -----")
        print("1. Registrar nuevo turno")
        print("2. Atender siguiente turno")
        print("3. Deshacer última acción")
        print("4. Ver siguiente en espera")
        print("5. Buscar cliente registrado")
        print("6. Mostrar todos los clientes registrados")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            dni = input("Ingrese DNI: ")
            nombre = input("Ingrese nombre: ")
            cliente = {"dni": dni,"nombre": nombre}
            # Agregar a lista de registrados
            clientes_registrados.agregar(cliente)
            # Encolar para atención
            cola_turnos.enqueue(cliente)
            # Registrar acción en historial
            accion = f"Registro: {nombre} (DNI: {dni})"
            historial.push(accion)
            print(f" {accion}")

        elif opcion == "2":
            if not cola_turnos.esta_vacia():
                atendido = cola_turnos.dequeue()
                accion = f"Atención completada: {atendido['nombre']}"
                historial.push(accion)
                print(f"Atendido a: {atendido['nombre']}")
            else:
                print("No hay turnos en espera")

        elif opcion == "3":
            deshecha = historial.pop()
            if deshecha:
                print(f"Acción deshecha: {deshecha}")
            else:
                print("No hay acciones para deshacer")

        elif opcion == "4":
            if not cola_turnos.esta_vacia():
                sig = cola_turnos.ver_frente()
                print(f"Siguiente: {sig['nombre']} — DNI: {sig['dni']}")
            else:
                print("No hay turnos en espera")

        elif opcion == "5":
            nombre_buscar = input("Nombre a buscar: ")
            resultado = clientes_registrados.buscar(nombre_buscar)
            if resultado:
                print(f"Encontrado — DNI: {resultado['dni']}, Nombre: {resultado['nombre']}")
            else:
                print("Cliente no registrado")

        elif opcion == "6":
            print("Lista de clientes registrados:")
            print(clientes_registrados.mostrar())

        elif opcion == "7":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida, intente nuevamente")


if __name__ == "__main__":
    main()