# Ejercicio 12. Control de ingresos y egresos

CAPACIDAD = 15
placas = []   # vehículos que están actualmente dentro


def buscar(placa):
    """Devuelve el índice de la placa en la lista, o -1 si no está."""
    for i in range(len(placas)):
        if placas[i] == placa:
            return i
    return -1


def registrar_ingreso():
    if len(placas) >= CAPACIDAD:
        print("El estacionamiento está lleno. No se puede registrar el ingreso.")
        return
    placa = input("Placa del vehículo que ingresa: ").strip().upper()
    if placa == "":
        print("La placa no puede estar vacía.")
    elif buscar(placa) != -1:
        print("Esa placa ya está registrada dentro del estacionamiento.")
    else:
        placas.append(placa)
        print(f"Ingreso registrado: {placa}")


def registrar_salida():
    placa = input("Placa del vehículo que sale: ").strip().upper()
    posicion = buscar(placa)
    if posicion == -1:
        print("Ese vehículo no se encuentra registrado en el estacionamiento.")
    else:
        placas.pop(posicion)
        print(f"Salida registrada: {placa}")


def consultar_placas():
    if len(placas) == 0:
        print("No hay vehículos dentro del estacionamiento.")
    else:
        print("Vehículos dentro del estacionamiento:")
        for i in range(len(placas)):
            print(f"  {i + 1}. {placas[i]}")


opcion = ""
while opcion != "7":
    print("\n===== CONTROL DE ESTACIONAMIENTO =====")
    print("1. Registrar ingreso")
    print("2. Registrar salida")
    print("3. Consultar placas dentro")
    print("4. Mostrar vehículos estacionados")
    print("5. Mostrar espacios disponibles")
    print("6. Mostrar estado completo")
    print("7. Salir")
    opcion = input("Elige una opción: ").strip()

    if opcion == "1":
        registrar_ingreso()
    elif opcion == "2":
        registrar_salida()
    elif opcion == "3":
        consultar_placas()
    elif opcion == "4":
        print(f"Vehículos estacionados: {len(placas)}")
    elif opcion == "5":
        print(f"Espacios disponibles: {CAPACIDAD - len(placas)}")
    elif opcion == "6":
        consultar_placas()
        print(f"Estacionados: {len(placas)} | Disponibles: {CAPACIDAD - len(placas)}")
    elif opcion == "7":
        print("Programa finalizado.")
    else:
        print("Opción no válida.")
