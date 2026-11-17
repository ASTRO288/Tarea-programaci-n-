# Ejercicio 11. Búsqueda de vehículos

placas = []

print("Registra las placas del historial (deja vacío y presiona ENTER para terminar).")
while True:
    placa = input("Placa: ").strip().upper()
    if placa == "":
        break
    placas.append(placa)

print(f"\nSe almacenaron {len(placas)} placas.")

while True:
    buscada = input("\nPlaca a buscar (vacío para salir): ").strip().upper()
    if buscada == "":
        break

    # Recorremos la lista comparando cada elemento con la placa buscada
    posicion = -1
    for i in range(len(placas)):
        if placas[i] == buscada:
            posicion = i
            break

    if posicion == -1:
        print(f"La placa {buscada} NO se encuentra en el historial.")
    else:
        print(f"La placa {buscada} SÍ está en el historial, en la posición {posicion + 1} "
              f"(índice {posicion}).")

print("Búsqueda finalizada.")
