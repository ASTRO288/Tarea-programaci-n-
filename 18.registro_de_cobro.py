# Ejercicio 18. Registro de cobros por vehículo

FILAS = 3
COLUMNAS = 3
TIPOS = ["Motocicleta", "Automóvil", "Camioneta", "Camión"]
TARIFAS = [10, 15, 20, 30]

# Matriz de cajones: "LIBRE" o la placa del vehículo
estacionamiento = []
for i in range(FILAS):
    fila = []
    for j in range(COLUMNAS):
        fila.append("LIBRE")
    estacionamiento.append(fila)

# Registros: [espacio, placa, tipo, hora_entrada, hora_salida, permanencia, importe]
registros = []


def leer_entero(mensaje, minimo, maximo):
    while True:
        texto = input(mensaje)
        if texto.isdigit() and minimo <= int(texto) <= maximo:
            return int(texto)
        print(f"  Ingresa un número entre {minimo} y {maximo}.")


def buscar_placa(placa):
    """Localiza la placa dentro de la matriz. Devuelve (fila, columna) o None."""
    for i in range(FILAS):
        for j in range(COLUMNAS):
            if estacionamiento[i][j] == placa:
                return (i, j)
    return None


def registrar_ingreso():
    fila = leer_entero(f"Fila (1-{FILAS}): ", 1, FILAS) - 1
    col = leer_entero(f"Columna (1-{COLUMNAS}): ", 1, COLUMNAS) - 1
    if estacionamiento[fila][col] != "LIBRE":
        print(f"Ese cajón ya está ocupado por {estacionamiento[fila][col]}.")
        return

    placa = input("Placa: ").strip().upper()
    if placa == "" or placa == "LIBRE":
        print("Placa no válida.")
        return
    if buscar_placa(placa) is not None:
        print("Esa placa ya está dentro del estacionamiento.")
        return

    print("1. Motocicleta  2. Automóvil  3. Camioneta  4. Camión")
    tipo = TIPOS[leer_entero("Tipo de vehículo (1-4): ", 1, 4) - 1]
    entrada = leer_entero("Hora de entrada (0-23): ", 0, 23)

    espacio = fila * COLUMNAS + col + 1
    estacionamiento[fila][col] = placa
    registros.append([espacio, placa, tipo, entrada, "—", "—", "—"])
    print(f"Ingreso registrado en el espacio {espacio}.")


def registrar_salida():
    placa = input("Placa del vehículo que sale: ").strip().upper()
    posicion = buscar_placa(placa)
    if posicion is None:
        print("Esa placa no se encuentra en el estacionamiento.")
        return

    # Buscar el registro abierto (sin hora de salida) de esa placa
    indice = -1
    for r in range(len(registros)):
        if registros[r][1] == placa and registros[r][4] == "—":
            indice = r

    entrada = registros[indice][3]
    salida = leer_entero("Hora de salida (0-23): ", 0, 23)

    permanencia = salida - entrada
    if permanencia < 0:
        permanencia += 24          # salió al día siguiente

    horas_cobradas = permanencia if permanencia >= 1 else 1
    tarifa = TARIFAS[TIPOS.index(registros[indice][2])]
    importe = horas_cobradas * tarifa

    registros[indice][4] = salida
    registros[indice][5] = permanencia
    registros[indice][6] = importe

    estacionamiento[posicion[0]][posicion[1]] = "LIBRE"   # se libera el espacio

    print(f"Permanencia: {permanencia} h (se cobran {horas_cobradas} h a ${tarifa})")
    print(f"Importe a pagar: ${importe}")
    print("Espacio liberado.")


def mostrar_tabla():
    print()
    print(f"{'Espacio':<8}{'Placa':<10}{'Tipo':<13}{'Entrada':<9}{'Salida':<8}{'Permanencia':<13}{'Importe':<8}")
    if len(registros) == 0:
        print("(sin registros)")
    for reg in registros:
        print(f"{reg[0]:<8}{reg[1]:<10}{reg[2]:<13}{reg[3]:<9}{reg[4]:<8}{reg[5]:<13}{reg[6]:<8}")


opcion = ""
while opcion != "4":
    print("\n===== COBROS POR VEHÍCULO =====")
    print("1. Registrar ingreso")
    print("2. Registrar salida y cobrar")
    print("3. Mostrar tabla de registros")
    print("4. Salir")
    opcion = input("Elige una opción: ").strip()

    if opcion == "1":
        registrar_ingreso()
    elif opcion == "2":
        registrar_salida()
    elif opcion == "3":
        mostrar_tabla()
    elif opcion == "4":
        print("Programa finalizado.")
    else:
        print("Opción no válida.")
