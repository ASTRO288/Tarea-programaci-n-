# Ejercicio 10. Historial de vehículos

placas = []

print("Registra las placas de los vehículos (deja vacío y presiona ENTER para terminar).")

while True:
    placa = input("Placa: ").strip().upper()
    if placa == "":
        break
    placas.append(placa)

print("\n===== HISTORIAL DE VEHÍCULOS =====")
if len(placas) == 0:
    print("No se registró ningún vehículo.")
else:
    for i in range(len(placas)):
        print(f"{i + 1}. {placas[i]}")
    print(f"Total de vehículos: {len(placas)}")
