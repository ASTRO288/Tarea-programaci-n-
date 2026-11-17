# Ejercicio 19. Reporte de ocupación e ingresos

FILAS = 3
COLUMNAS = 3
TIPOS = ["Motocicleta", "Automóvil", "Camioneta", "Camión"]
TARIFAS = [10, 15, 20, 30]

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

    indice = -1
    for r in range(len(registros)):
        if registros[r][1] == placa and registros[r][4] == "—":
            indice = r

    entrada = registros[indice][3]
    salida = leer_entero("Hora de salida (0-23): ", 0, 23)

    permanencia = salida - entrada
    if permanencia < 0:
        permanencia += 24

    horas_cobradas = permanencia if permanencia >= 1 else 1
    tarifa = TARIFAS[TIPOS.index(registros[indice][2])]
    importe = horas_cobradas * tarifa

    registros[indice][4] = salida
    registros[indice][5] = permanencia
    registros[indice][6] = importe
    estacionamiento[posicion[0]][posicion[1]] = "LIBRE"

    print(f"Permanencia: {permanencia} h (se cobran {horas_cobradas} h a ${tarifa})")
    print(f"Importe a pagar: ${importe}")
    print("Espacio liberado.")


def generar_reporte():
    print("\n========== REPORTE DE LA JORNADA ==========")

    # 1. Vehículos que permanecen dentro
    print("\n1. Vehículos dentro del estacionamiento:")
    dentro = 0
    ocupados_por_fila = []
    for i in range(FILAS):
        ocupados_fila = 0
        for j in range(COLUMNAS):
            if estacionamiento[i][j] != "LIBRE":
                dentro += 1
                ocupados_fila += 1
                print(f"   - {estacionamiento[i][j]} (fila {i + 1}, columna {j + 1})")
        ocupados_por_fila.append(ocupados_fila)
    if dentro == 0:
        print("   (ninguno)")

    # 2. Espacios libres y ocupados
    total_espacios = FILAS * COLUMNAS
    print(f"\n2. Espacios ocupados: {dentro} | Espacios libres: {total_espacios - dentro}")

    # 3. Total de vehículos atendidos (todos los que ingresaron en la jornada)
    print(f"\n3. Total de vehículos atendidos: {len(registros)}")

    # 4. Ingresos generados (por vehículos que ya salieron y pagaron)
    ingresos = 0
    for reg in registros:
        if reg[6] != "—":
            ingresos += reg[6]
    print(f"\n4. Ingresos generados: ${ingresos}")

    # 5. Tipo de vehículo con mayor número de ingresos (entradas)
    conteo = [0, 0, 0, 0]
    for reg in registros:
        conteo[TIPOS.index(reg[2])] += 1
    mayor = max(conteo)
    if mayor == 0:
        print("\n5. Tipo de vehículo con más ingresos: (sin registros)")
    else:
        ganadores = []
        for k in range(len(TIPOS)):
            if conteo[k] == mayor:
                ganadores.append(TIPOS[k])
        print(f"\n5. Tipo de vehículo con más ingresos: {', '.join(ganadores)} ({mayor})")

    # 6. Fila con mayor ocupación
    mayor_fila = max(ocupados_por_fila)
    if mayor_fila == 0:
        print("\n6. Fila con mayor ocupación: (todas las filas están vacías)")
    else:
        filas = []
        for i in range(FILAS):
            if ocupados_por_fila[i] == mayor_fila:
                filas.append(str(i + 1))
        print(f"\n6. Fila con mayor ocupación: fila {', '.join(filas)} ({mayor_fila} vehículos)")

    print("\n===========================================")


def mostrar_tabla():
    print()
    print(f"{'Espacio':<8}{'Placa':<10}{'Tipo':<13}{'Entrada':<9}{'Salida':<8}{'Permanencia':<13}{'Importe':<8}")
    if len(registros) == 0:
        print("(sin registros)")
    for reg in registros:
        print(f"{reg[0]:<8}{reg[1]:<10}{reg[2]:<13}{reg[3]:<9}{reg[4]:<8}{reg[5]:<13}{reg[6]:<8}")


opcion = ""
while opcion != "5":
    print("\n===== SISTEMA DE ESTACIONAMIENTO =====")
    print("1. Registrar ingreso")
    print("2. Registrar salida y cobrar")
    print("3. Mostrar tabla de registros")
    print("4. Generar reporte de la jornada")
    print("5. Salir")
    opcion = input("Elige una opción: ").strip()

    if opcion == "1":
        registrar_ingreso()
    elif opcion == "2":
        registrar_salida()
    elif opcion == "3":
        mostrar_tabla()
    elif opcion == "4":
        generar_reporte()
    elif opcion == "5":
        print("Programa finalizado.")
    else:
        print("Opción no válida.")
