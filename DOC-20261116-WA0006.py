"""
Sistema de control de estacionamiento — Serie de ejercicios 1 a 19.

Ejecuta el archivo y elige el ejercicio desde el menú:

    python estacionamiento.py

Organización del código:
    1. Constantes
    2. Utilidades de entrada/salida (validación y formato)
    3. Lógica de negocio reutilizable (tarifas, matrices)
    4. Ejercicios 1-19 (uno por función)
    5. Menú principal
"""
from __future__ import annotations

import math

# =============================================================================
# 1. CONSTANTES
# =============================================================================
MOTOCICLETA = "Motocicleta"
AUTOMOVIL = "Automóvil"
CAMIONETA = "Camioneta"
CAMION = "Camión"

LIBRE = "LIBRE"

TARIFA_BASE_POR_HORA = 15          # Ejercicio 3
DESCUENTO_FRECUENTE = 0.10         # Ejercicio 5
VISITAS_PARA_DESCUENTO = 10        # Ejercicio 5
CAPACIDAD_JORNADA = 30             # Ejercicio 9
CAPACIDAD_INTERNA = 15             # Ejercicio 12
FILAS_COBROS, COLUMNAS_COBROS = 3, 4   # Ejercicios 18 y 19


# =============================================================================
# 2. UTILIDADES DE ENTRADA / SALIDA
# =============================================================================
def titulo(texto: str) -> None:
    print(f"\n{'=' * 60}\n{texto}\n{'=' * 60}")


def dinero(valor: float) -> str:
    return f"${valor:,.2f}"


def formatear_hora(minutos: int) -> str:
    """Convierte minutos desde medianoche a 'HH:MM'."""
    return f"{minutos // 60:02d}:{minutos % 60:02d}"


def formatear_duracion(minutos: int) -> str:
    return f"{minutos // 60} h {minutos % 60:02d} min"


def leer_texto(mensaje: str) -> str:
    while True:
        valor = input(mensaje).strip()
        if valor:
            return valor
        print("  ⚠ Este dato no puede quedar vacío.")


def leer_placa(mensaje: str = "Placa: ") -> str:
    while True:
        placa = leer_texto(mensaje).upper()
        if placa != LIBRE:
            return placa
        print(f"  ⚠ '{LIBRE}' no es una placa válida.")


def leer_entero(mensaje: str, minimo: int | None = None,
                maximo: int | None = None) -> int:
    while True:
        try:
            valor = int(input(mensaje))
        except ValueError:
            print("  ⚠ Ingresa un número entero válido.")
            continue
        if minimo is not None and valor < minimo:
            print(f"  ⚠ El valor mínimo permitido es {minimo}.")
        elif maximo is not None and valor > maximo:
            print(f"  ⚠ El valor máximo permitido es {maximo}.")
        else:
            return valor


def leer_flotante(mensaje: str, minimo: float | None = None) -> float:
    while True:
        try:
            valor = float(input(mensaje))
        except ValueError:
            print("  ⚠ Ingresa un número válido.")
            continue
        if not math.isfinite(valor):
            print("  ⚠ Ingresa un número válido.")
        elif minimo is not None and valor < minimo:
            print(f"  ⚠ El valor mínimo permitido es {minimo}.")
        else:
            return valor


def leer_hora(mensaje: str, minimo: int = 0) -> int:
    """Lee una hora 'HH:MM' (24 h) y la devuelve en minutos desde medianoche.

    Si se indica `minimo`, rechaza horas anteriores a ese valor.
    """
    while True:
        partes = input(mensaje).strip().split(":")
        if len(partes) == 2 and all(p.isdecimal() for p in partes):
            horas, minutos = int(partes[0]), int(partes[1])
            if 0 <= horas <= 23 and 0 <= minutos <= 59:
                total = horas * 60 + minutos
                if total >= minimo:
                    return total
                print(f"  ⚠ La hora no puede ser anterior a {formatear_hora(minimo)}.")
                continue
        print("  ⚠ Formato inválido. Usa HH:MM en 24 horas (ej. 08:30).")


def confirmar(mensaje: str) -> bool:
    while True:
        respuesta = input(f"{mensaje} (s/n): ").strip().lower()
        if respuesta in ("s", "si", "sí"):
            return True
        if respuesta in ("n", "no"):
            return False
        print("  ⚠ Responde 's' o 'n'.")


# =============================================================================
# 3. LÓGICA DE NEGOCIO REUTILIZABLE
# =============================================================================
def horas_a_cobrar(horas: float) -> int:
    """Se cobra por hora iniciada; menos de una hora cuenta como una hora."""
    return max(1, math.ceil(horas))


def tarifa_por_estancia(horas: float) -> int:
    """Ejercicio 4: tarifa por hora según la duración de la estancia."""
    if horas <= 2:
        return 20
    elif horas <= 5:
        return 18
    else:
        return 15


def tarifa_por_tipo(tipo: str) -> int:
    """Ejercicio 6: tarifa por hora según el tipo de vehículo."""
    if tipo == MOTOCICLETA:
        return 10
    elif tipo == AUTOMOVIL:
        return 15
    elif tipo == CAMIONETA:
        return 20
    elif tipo == CAMION:
        return 30
    raise ValueError(f"Tipo de vehículo desconocido: {tipo}")


def solicitar_tipo_vehiculo() -> str:
    print("  1) Motocicleta   2) Automóvil   3) Camioneta   4) Camión")
    opcion = leer_entero("  Tipo de vehículo (1-4): ", 1, 4)
    if opcion == 1:
        return MOTOCICLETA
    elif opcion == 2:
        return AUTOMOVIL
    elif opcion == 3:
        return CAMIONETA
    return CAMION


def calcular_importe(tipo: str, horas: float) -> int:
    return tarifa_por_tipo(tipo) * horas_a_cobrar(horas)


# --- Matrices -----------------------------------------------------------------
def esta_libre(celda: int | str) -> bool:
    """Un cajón está libre si vale 0 (ejercicios 13-16) o 'LIBRE' (17-19)."""
    return celda == 0 or celda == LIBRE


def crear_estacionamiento_ejemplo() -> list[list[int]]:
    return [
        [0, 1, 0, 0, 1],
        [1, 0, 0, 1, 0],
        [0, 0, 1, 0, 0],
        [1, 1, 0, 0, 0],
    ]


def mostrar_matriz(matriz: list[list]) -> None:
    """Imprime la matriz como tabla (funciona con enteros y con cadenas)."""
    columnas = len(matriz[0])
    ancho = max([len(f"Esp. {columnas}")]
                + [len(str(celda)) for fila in matriz for celda in fila]) + 2
    print(" " * 8 + "".join(f"Esp. {c}".center(ancho) for c in range(1, columnas + 1)))
    for numero, fila in enumerate(matriz, start=1):
        print(f"Fila {numero:<3}" + "".join(str(celda).center(ancho) for celda in fila))


def ocupacion_por_fila(matriz: list[list]) -> list[int]:
    """Devuelve cuántos cajones ocupados tiene cada fila."""
    resultado = []
    for fila in matriz:
        ocupados = 0
        for celda in fila:
            if not esta_libre(celda):
                ocupados += 1
        resultado.append(ocupados)
    return resultado


def buscar_placa_en_matriz(matriz: list[list[str]], placa: str) -> tuple[int, int] | None:
    """Recorre la matriz y devuelve (fila, columna) de la placa, o None."""
    for f, fila in enumerate(matriz):
        for c, celda in enumerate(fila):
            if celda == placa:
                return f, c
    return None


# =============================================================================
# 4. EJERCICIOS
# =============================================================================
# ----------------------------- NIVEL 1 ----------------------------------------
def ejercicio_1() -> None:
    """Registro de ingreso al estacionamiento (I)."""
    placa = leer_placa()
    propietario = leer_texto("Nombre del propietario: ")
    hora_entrada = leer_hora("Hora de entrada (HH:MM): ")

    print("\n------ COMPROBANTE DE INGRESO ------")
    print(f"Placa:        {placa}")
    print(f"Propietario:  {propietario}")
    print(f"Hora entrada: {formatear_hora(hora_entrada)}")
    print("------------------------------------")


def ejercicio_2() -> None:
    """Cálculo del tiempo de estancia (I)."""
    entrada = leer_hora("Hora de entrada (HH:MM): ")
    salida = leer_hora("Hora de salida  (HH:MM): ", minimo=entrada)

    minutos = salida - entrada
    print(f"\nTiempo de estancia: {minutos / 60:.2f} horas ({formatear_duracion(minutos)})")


def ejercicio_3() -> None:
    """Cobro por tiempo de permanencia: $15 por hora (I)."""
    horas = leer_flotante("Tiempo de permanencia (horas): ", minimo=0)
    cobradas = horas_a_cobrar(horas)

    print(f"\nHoras cobradas: {cobradas}")
    print(f"Importe a pagar: {dinero(cobradas * TARIFA_BASE_POR_HORA)}")


# ----------------------------- NIVEL 2 ----------------------------------------
def ejercicio_4() -> None:
    """Tarifas diferenciadas (R)."""
    horas = leer_flotante("Tiempo de permanencia (horas): ", minimo=0)
    tarifa = tarifa_por_estancia(horas)
    cobradas = horas_a_cobrar(horas)

    print(f"\nTarifa aplicada: {dinero(tarifa)} por hora")
    print(f"Horas cobradas:  {cobradas}")
    print(f"Importe a pagar: {dinero(tarifa * cobradas)}")


def ejercicio_5() -> None:
    """Descuentos para clientes frecuentes (R)."""
    visitas = leer_entero("Número de visitas en el mes: ", minimo=0)
    importe = leer_flotante("Importe de la estancia: $", minimo=0)

    descuento = 0.0
    if visitas > VISITAS_PARA_DESCUENTO:
        descuento = importe * DESCUENTO_FRECUENTE
        print("\nCliente frecuente: se aplica 10% de descuento.")
    else:
        print("\nCliente regular: sin descuento.")

    print(f"Importe:   {dinero(importe)}")
    print(f"Descuento: {dinero(descuento)}")
    print(f"Total:     {dinero(importe - descuento)}")


def ejercicio_6() -> None:
    """Clasificación del tipo de vehículo (R)."""
    tipo = solicitar_tipo_vehiculo()
    horas = leer_flotante("Horas de estancia: ", minimo=0)

    print(f"\nVehículo: {tipo} — tarifa {dinero(tarifa_por_tipo(tipo))} por hora")
    print(f"Horas cobradas:  {horas_a_cobrar(horas)}")
    print(f"Importe a pagar: {dinero(calcular_importe(tipo, horas))}")


# ----------------------------- NIVEL 3 ----------------------------------------
def _jornada(con_corte: bool, capacidad: int | None) -> None:
    """Núcleo compartido por los ejercicios 7, 8 y 9 (C: cada uno amplía al anterior)."""
    atendidos = motos = autos = camionetas = camiones = 0
    recaudado = 0

    while True:
        print(f"\n--- Vehículo #{atendidos + 1} ---")
        placa = leer_placa()
        tipo = solicitar_tipo_vehiculo()
        horas = leer_flotante("  Horas de estancia: ", minimo=0)

        importe = calcular_importe(tipo, horas)
        print(f"  → {placa} ({tipo}): {horas_a_cobrar(horas)} h cobradas = {dinero(importe)}")

        # Acumuladores (ejercicio 8)
        atendidos += 1
        recaudado += importe
        if tipo == MOTOCICLETA:
            motos += 1
        elif tipo == AUTOMOVIL:
            autos += 1
        elif tipo == CAMIONETA:
            camionetas += 1
        else:
            camiones += 1

        # Control de capacidad (ejercicio 9)
        if capacidad is not None:
            disponibles = capacidad - atendidos
            print(f"  Espacios disponibles: {disponibles}")
            if disponibles == 0:
                print("  ⛔ Capacidad máxima alcanzada: no es posible recibir más vehículos.")
                break

        if not confirmar("¿Registrar otro vehículo?"):
            break

    if con_corte:
        print("\n========== CORTE DE CAJA ==========")
        print(f"Vehículos atendidos: {atendidos}")
        print(f"  Motocicletas: {motos}")
        print(f"  Automóviles:  {autos}")
        print(f"  Camionetas:   {camionetas}")
        print(f"  Camiones:     {camiones}")
        print(f"Total recaudado: {dinero(recaudado)}")


def ejercicio_7() -> None:
    """Atención de varios vehículos (R)."""
    _jornada(con_corte=False, capacidad=None)


def ejercicio_8() -> None:
    """Corte de caja (C del 7)."""
    _jornada(con_corte=True, capacidad=None)


def ejercicio_9() -> None:
    """Control de capacidad: máximo 30 vehículos (C del 8)."""
    _jornada(con_corte=True, capacidad=CAPACIDAD_JORNADA)


# ----------------------------- NIVEL 4 ----------------------------------------
def ejercicio_10() -> None:
    """Historial de vehículos (R)."""
    historial: list[str] = []
    while True:
        historial.append(leer_placa())
        if not confirmar("¿Registrar otra placa?"):
            break

    print("\nPlacas registradas:")
    for numero, placa in enumerate(historial, start=1):
        print(f"  {numero}. {placa}")


def buscar_placa(historial: list[str], placa: str) -> int:
    """Búsqueda secuencial: devuelve el índice de la placa o -1 si no existe."""
    for indice in range(len(historial)):
        if historial[indice] == placa:
            return indice
    return -1


def ejercicio_11() -> None:
    """Búsqueda de vehículos (R)."""
    historial: list[str] = []
    while True:
        historial.append(leer_placa("Placa a guardar: "))
        if not confirmar("¿Guardar otra placa?"):
            break

    print("\n--- Consulta de historial ---")
    while True:
        buscada = leer_placa("Placa a buscar: ")
        indice = buscar_placa(historial, buscada)
        if indice == -1:
            print(f"  La placa {buscada} NO está en el historial.")
        else:
            print(f"  La placa {buscada} SÍ estuvo: posición {indice + 1} de {len(historial)}.")
        if not confirmar("¿Buscar otra placa?"):
            break


def ejercicio_12() -> None:
    """Control de ingresos y egresos con capacidad de 15 vehículos (R)."""
    dentro: list[str] = []

    while True:
        print(f"\n1) Registrar ingreso     2) Registrar salida"
              f"\n3) Consultar placas      4) Vehículos estacionados"
              f"\n5) Espacios disponibles  0) Salir")
        opcion = leer_entero("Opción: ", 0, 5)

        if opcion == 0:
            break
        elif opcion == 1:
            if len(dentro) >= CAPACIDAD_INTERNA:
                print("  ⛔ Estacionamiento lleno: no se permite el ingreso.")
                continue
            placa = leer_placa()
            if placa in dentro:
                print(f"  ⚠ La placa {placa} ya se encuentra registrada dentro.")
            else:
                dentro.append(placa)
                print(f"  ✔ Ingreso registrado: {placa}")
        elif opcion == 2:
            placa = leer_placa()
            if placa in dentro:
                dentro.remove(placa)
                print(f"  ✔ Salida registrada: {placa}")
            else:
                print(f"  ⚠ La placa {placa} no está registrada en el estacionamiento.")
        elif opcion == 3:
            if not dentro:
                print("  El estacionamiento está vacío.")
            for numero, placa in enumerate(dentro, start=1):
                print(f"  {numero}. {placa}")
        elif opcion == 4:
            print(f"  Vehículos estacionados: {len(dentro)}")
        elif opcion == 5:
            print(f"  Espacios disponibles: {CAPACIDAD_INTERNA - len(dentro)}")


# ----------------------------- NIVEL 5 ----------------------------------------
def ejercicio_13() -> None:
    """Distribución de espacios: 0 = libre, 1 = ocupado (I)."""
    print("Distribución del estacionamiento (0 = libre, 1 = ocupado):\n")
    mostrar_matriz(crear_estacionamiento_ejemplo())


def ejercicio_14() -> None:
    """Registro de ocupación en una posición específica (R)."""
    estacionamiento = crear_estacionamiento_ejemplo()
    filas, columnas = len(estacionamiento), len(estacionamiento[0])

    while True:
        print()
        mostrar_matriz(estacionamiento)
        fila = leer_entero(f"\nNúmero de fila (1-{filas}): ", 1, filas)
        espacio = leer_entero(f"Número de espacio (1-{columnas}): ", 1, columnas)

        if estacionamiento[fila - 1][espacio - 1] == 0:
            estacionamiento[fila - 1][espacio - 1] = 1
            print(f"  ✔ Vehículo registrado en fila {fila}, espacio {espacio}.")
        else:
            print("  ⚠ Ese espacio ya está ocupado. Selecciona otro lugar.")

        if not confirmar("¿Registrar otro vehículo?"):
            break

    print("\nEstado final:")
    mostrar_matriz(estacionamiento)


def ejercicio_15() -> None:
    """Conteo de espacios disponibles con ciclos anidados y acumuladores (R)."""
    estacionamiento = crear_estacionamiento_ejemplo()
    mostrar_matriz(estacionamiento)

    total = ocupados = libres = 0
    for fila in estacionamiento:
        for espacio in fila:
            total += 1
            if espacio == 1:
                ocupados += 1
            else:
                libres += 1

    print(f"\nTotal de espacios:    {total}")
    print(f"Espacios ocupados:    {ocupados}")
    print(f"Espacios libres:      {libres}")
    print(f"Porcentaje ocupación: {ocupados / total * 100:.1f}%")


def ejercicio_16() -> None:
    """Fila con mayor ocupación (R)."""
    estacionamiento = crear_estacionamiento_ejemplo()
    mostrar_matriz(estacionamiento)

    ocupacion = ocupacion_por_fila(estacionamiento)
    print()
    for numero, (fila, ocupados) in enumerate(zip(estacionamiento, ocupacion), start=1):
        print(f"Fila {numero}: {ocupados} ocupados, {len(fila) - ocupados} libres")

    maxima = max(ocupacion)
    filas_maximas = [n for n, ocupados in enumerate(ocupacion, start=1) if ocupados == maxima]
    etiqueta = "Fila" if len(filas_maximas) == 1 else "Filas"
    print(f"\n{etiqueta} con mayor ocupación: {', '.join(map(str, filas_maximas))} "
          f"({maxima} vehículo(s))")


# ----------------------------- NIVEL 6 ----------------------------------------
def ejercicio_17() -> None:
    """Registro de vehículos por cajón: la matriz guarda la placa (R)."""
    estacionamiento = [
        ["ABC123", LIBRE, "XYZ456"],
        [LIBRE, "DEF789", LIBRE],
        ["GHI321", LIBRE, LIBRE],
    ]
    filas, columnas = len(estacionamiento), len(estacionamiento[0])

    while True:
        print("\n1) Registrar vehículo en una posición"
              "\n2) Consultar dónde está una placa"
              "\n3) Mostrar estacionamiento"
              "\n0) Salir")
        opcion = leer_entero("Opción: ", 0, 3)

        if opcion == 0:
            break
        elif opcion == 1:
            placa = leer_placa()
            existente = buscar_placa_en_matriz(estacionamiento, placa)
            if existente is not None:
                print(f"  ⚠ {placa} ya está en fila {existente[0] + 1}, espacio {existente[1] + 1}.")
                continue
            fila = leer_entero(f"Fila (1-{filas}): ", 1, filas)
            espacio = leer_entero(f"Espacio (1-{columnas}): ", 1, columnas)
            ocupante = estacionamiento[fila - 1][espacio - 1]
            if ocupante == LIBRE:
                estacionamiento[fila - 1][espacio - 1] = placa
                print(f"  ✔ {placa} registrado en fila {fila}, espacio {espacio}.")
            else:
                print(f"  ⚠ Ese lugar está ocupado por {ocupante}.")
        elif opcion == 2:
            placa = leer_placa()
            posicion = buscar_placa_en_matriz(estacionamiento, placa)
            if posicion is None:
                print(f"  La placa {placa} no se encuentra en el estacionamiento.")
            else:
                print(f"  {placa} está en fila {posicion[0] + 1}, espacio {posicion[1] + 1}.")
        else:
            mostrar_matriz(estacionamiento)


# --- Registros de cobro (ejercicios 18 y 19) -------------------------------------
def numero_de_espacio(fila: int, columna: int) -> int:
    return fila * COLUMNAS_COBROS + columna + 1


def primer_espacio_libre(matriz: list[list[str]]) -> tuple[int, int] | None:
    for f, fila in enumerate(matriz):
        for c, celda in enumerate(fila):
            if celda == LIBRE:
                return f, c
    return None


def buscar_registro_activo(registros: list[dict], placa: str) -> dict | None:
    for registro in registros:
        if registro["placa"] == placa and registro["salida"] is None:
            return registro
    return None


def registrar_entrada(matriz: list[list[str]], registros: list[dict]) -> None:
    posicion = primer_espacio_libre(matriz)
    if posicion is None:
        print("  ⛔ Estacionamiento lleno.")
        return

    placa = leer_placa()
    if buscar_placa_en_matriz(matriz, placa) is not None:
        print(f"  ⚠ La placa {placa} ya se encuentra dentro.")
        return

    tipo = solicitar_tipo_vehiculo()
    entrada = leer_hora("Hora de entrada (HH:MM): ")

    fila, columna = posicion
    matriz[fila][columna] = placa
    espacio = numero_de_espacio(fila, columna)
    registros.append({
        "placa": placa, "tipo": tipo, "espacio": espacio, "entrada": entrada,
        "salida": None, "permanencia": None, "importe": None,
    })
    print(f"  ✔ {placa} asignado al espacio {espacio}.")


def registrar_salida(matriz: list[list[str]], registros: list[dict]) -> None:
    placa = leer_placa("Placa del vehículo que sale: ")
    posicion = buscar_placa_en_matriz(matriz, placa)
    registro = buscar_registro_activo(registros, placa)
    if posicion is None or registro is None:
        print(f"  ⚠ La placa {placa} no se encuentra en el estacionamiento.")
        return

    salida = leer_hora("Hora de salida (HH:MM): ", minimo=registro["entrada"])
    permanencia = salida - registro["entrada"]
    importe = calcular_importe(registro["tipo"], permanencia / 60)

    registro.update(salida=salida, permanencia=permanencia, importe=importe)
    fila, columna = posicion
    matriz[fila][columna] = LIBRE          # se libera el espacio

    print(f"  ✔ Salida de {placa} ({registro['tipo']})")
    print(f"    Permanencia: {formatear_duracion(permanencia)}")
    print(f"    Importe a pagar: {dinero(importe)}")


def mostrar_tabla(registros: list[dict]) -> None:
    if not registros:
        print("  Aún no hay registros.")
        return
    print(f"\n{'Espacio':<9}{'Placa':<10}{'Tipo':<13}{'Entrada':<9}"
          f"{'Salida':<9}{'Permanencia':<13}{'Importe':>10}")
    for r in registros:
        salida = formatear_hora(r["salida"]) if r["salida"] is not None else "—"
        permanencia = formatear_duracion(r["permanencia"]) if r["permanencia"] is not None else "—"
        importe = dinero(r["importe"]) if r["importe"] is not None else "—"
        print(f"{r['espacio']:<9}{r['placa']:<10}{r['tipo']:<13}"
              f"{formatear_hora(r['entrada']):<9}{salida:<9}{permanencia:<13}{importe:>10}")


def mostrar_reporte(matriz: list[list[str]], registros: list[dict]) -> None:
    """Ejercicio 19. 'Atendidos' = todos los vehículos que han ingresado."""
    dentro = [r for r in registros if r["salida"] is None]
    salieron = [r for r in registros if r["salida"] is not None]
    ocupados = sum(ocupacion_por_fila(matriz))
    total_espacios = FILAS_COBROS * COLUMNAS_COBROS

    print("\n============ REPORTE DE LA JORNADA ============")
    print("1. Vehículos dentro del estacionamiento:")
    if dentro:
        for r in dentro:
            print(f"   - {r['placa']} ({r['tipo']}) en espacio {r['espacio']}")
    else:
        print("   (ninguno)")

    print(f"2. Espacios ocupados: {ocupados} | libres: {total_espacios - ocupados}")
    print(f"3. Total de vehículos atendidos: {len(registros)} (con salida registrada: {len(salieron)})")
    print(f"4. Ingresos generados: {dinero(sum(r['importe'] for r in salieron))}")

    conteo: dict[str, int] = {}
    for r in registros:
        conteo[r["tipo"]] = conteo.get(r["tipo"], 0) + 1
    if conteo:
        mayor = max(conteo.values())
        tipos = [tipo for tipo, cantidad in conteo.items() if cantidad == mayor]
        print(f"5. Tipo con más ingresos: {', '.join(tipos)} ({mayor})")
    else:
        print("5. Tipo con más ingresos: (sin datos)")

    ocupacion = ocupacion_por_fila(matriz)
    maxima = max(ocupacion)
    if maxima == 0:
        print("6. Fila con mayor ocupación: (todas vacías)")
    else:
        filas = [str(n) for n, o in enumerate(ocupacion, start=1) if o == maxima]
        print(f"6. Fila con mayor ocupación: {', '.join(filas)} ({maxima} vehículo(s))")


def _sistema_cobros(con_reporte: bool) -> None:
    matriz = [[LIBRE] * COLUMNAS_COBROS for _ in range(FILAS_COBROS)]
    registros: list[dict] = []

    while True:
        print("\n1) Registrar entrada\n2) Registrar salida y cobrar\n3) Ver tabla de registros")
        if con_reporte:
            print("4) Reporte de ocupación e ingresos")
        print("0) Salir")
        opcion = leer_entero("Opción: ", 0, 4 if con_reporte else 3)

        if opcion == 0:
            break
        elif opcion == 1:
            registrar_entrada(matriz, registros)
        elif opcion == 2:
            registrar_salida(matriz, registros)
        elif opcion == 3:
            mostrar_tabla(registros)
        else:
            mostrar_reporte(matriz, registros)

    if con_reporte:
        mostrar_reporte(matriz, registros)


def ejercicio_18() -> None:
    """Registro de cobros por vehículo (C del 17)."""
    _sistema_cobros(con_reporte=False)


def ejercicio_19() -> None:
    """Reporte de ocupación e ingresos (C del 18)."""
    _sistema_cobros(con_reporte=True)


# =============================================================================
# 5. MENÚ PRINCIPAL
# =============================================================================
EJERCICIOS = {
    1: ("Registro de ingreso", ejercicio_1),
    2: ("Tiempo de estancia", ejercicio_2),
    3: ("Cobro por permanencia", ejercicio_3),
    4: ("Tarifas diferenciadas", ejercicio_4),
    5: ("Descuento a clientes frecuentes", ejercicio_5),
    6: ("Tipo de vehículo", ejercicio_6),
    7: ("Atención de varios vehículos", ejercicio_7),
    8: ("Corte de caja", ejercicio_8),
    9: ("Control de capacidad", ejercicio_9),
    10: ("Historial de vehículos", ejercicio_10),
    11: ("Búsqueda de vehículos", ejercicio_11),
    12: ("Control de ingresos y egresos", ejercicio_12),
    13: ("Distribución de espacios", ejercicio_13),
    14: ("Registro de ocupación", ejercicio_14),
    15: ("Conteo de espacios", ejercicio_15),
    16: ("Fila con mayor ocupación", ejercicio_16),
    17: ("Vehículos por cajón", ejercicio_17),
    18: ("Registro de cobros", ejercicio_18),
    19: ("Reporte de ocupación e ingresos", ejercicio_19),
}

NIVELES = (
    ("Nivel 1. Fundamentos", range(1, 4)),
    ("Nivel 2. Condicionales", range(4, 7)),
    ("Nivel 3. Estructuras repetitivas", range(7, 10)),
    ("Nivel 4. Listas", range(10, 13)),
    ("Nivel 5. Matrices", range(13, 17)),
    ("Nivel 6. Integración", range(17, 20)),
)


def mostrar_menu() -> None:
    titulo("SISTEMA DE CONTROL DE ESTACIONAMIENTO")
    for nombre, numeros in NIVELES:
        print(f"\n{nombre}")
        for n in numeros:
            print(f"  {n:>2}. {EJERCICIOS[n][0]}")
    print("\n   0. Salir")


def main() -> None:
    while True:
        mostrar_menu()
        opcion = leer_entero("\nElige un ejercicio: ", 0, len(EJERCICIOS))
        if opcion == 0:
            print("¡Hasta luego!")
            break
        nombre, ejercicio = EJERCICIOS[opcion]
        titulo(f"Ejercicio {opcion}. {nombre}")
        ejercicio()
        input("\nPresiona Enter para volver al menú...")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nPrograma finalizado.")
