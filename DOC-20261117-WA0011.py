# Ejercicio 17. Registro de vehículos por cajón

FILAS = 3
COLUMNAS = 3

estacionamiento = []
for i in range(FILAS):
    fila = []
    for j in range(COLUMNAS):
        fila.append("LIBRE")
    estacionamiento.append(fila)


def leer_entero(mensaje, minimo, maximo):
    while True:
        texto = input(mensaje)
        if texto.isdigit() and minimo <= int(texto) <= maximo:
            return int(texto)
        print(f"  Ingresa un número entre {minimo} y {maximo}.")


def mostrar():
    print()
    for i in range(FILAS):
        for j in range(COLUMNAS):
            print(f"[{estacionamiento[i][j]:^8}]", end=" ")
        print()


def buscar_placa(placa):
    """Devuelve (fila, columna) o None si la placa no está."""
    for i in range(FILAS):
        for j in range(COLUMNAS):
            if estacionamiento[i][j] == placa:
                return (i, j)
    return None


def registrar():
    fila = leer_entero(f"Fila (1-{FILAS}): ", 1, FILAS) - 1
    col = leer_entero(f"Columna (1-{COLUMNAS}): ", 1, COLUMNAS) - 1
    if estacionamiento[fila][col] != "LIBRE":
        print(f"Ese cajón ya está ocupado por {estacionamiento[fila][col]}.")
        return
    placa = input("Placa del vehículo: ").strip().upper()
    if placa == "" or placa == "LIBRE":
        print("Placa no válida.")
    elif buscar_placa(placa) is not None:
        print("Esa placa ya está registrada en otro cajón.")
    else:
        estacionamiento[fila][col] = placa
        print(f"{placa} registrado en fila {fila + 1}, columna {col + 1}.")


def consultar():
    placa = input("Placa a buscar: ").strip().upper()
    posicion = buscar_placa(placa)
    if posicion is None:
        print("Esa placa no se encuentra en el estacionamiento.")
    else:
        print(f"{placa} está en la fila {posicion[0] + 1}, columna {posicion[1] + 1}.")


opcion = ""
while opcion != "4":
    print("\n===== CAJONES DE ESTACIONAMIENTO =====")
    print("1. Registrar vehículo en un cajón")
    print("2. Consultar ubicación de una placa")
    print("3. Mostrar estacionamiento")
    print("4. Salir")
    opcion = input("Elige una opción: ").strip()

    if opcion == "1":
        registrar()
    elif opcion == "2":
        consultar()
    elif opcion == "3":
        mostrar()
    elif opcion == "4":
        print("Programa finalizado.")
    else:
        print("Opción no válida.")
