# Ejercicio 14. Registro de ocupación
# 0 = espacio libre, 1 = espacio ocupado

FILAS = 4
COLUMNAS = 5

# Estacionamiento vacío al iniciar
estacionamiento = []
for i in range(FILAS):
    fila = []
    for j in range(COLUMNAS):
        fila.append(0)
    estacionamiento.append(fila)


def mostrar():
    print("\n        ", end="")
    for j in range(COLUMNAS):
        print(f"Esp {j + 1}", end="  ")
    print()
    for i in range(FILAS):
        print(f"Fila {i + 1}: ", end="")
        for j in range(COLUMNAS):
            print(f"  {estacionamiento[i][j]}  ", end="  ")
        print()


def leer_entero(mensaje, minimo, maximo):
    while True:
        texto = input(mensaje)
        if texto.isdigit() and minimo <= int(texto) <= maximo:
            return int(texto)
        print(f"  Ingresa un número entre {minimo} y {maximo}.")


continuar = "s"
while continuar == "s":
    mostrar()
    fila = leer_entero(f"\nNúmero de fila (1-{FILAS}): ", 1, FILAS)
    espacio = leer_entero(f"Número de espacio (1-{COLUMNAS}): ", 1, COLUMNAS)

    if estacionamiento[fila - 1][espacio - 1] == 0:
        estacionamiento[fila - 1][espacio - 1] = 1
        print(f"Vehículo estacionado en fila {fila}, espacio {espacio}.")
    else:
        print("Ese espacio ya está ocupado. Selecciona otro lugar.")

    continuar = ""
    while continuar not in ("s", "n"):
        continuar = input("¿Registrar otro vehículo? (s/n): ").lower()

mostrar()
