# Ejercicio 16. Identificación de la fila con mayor ocupación
# 0 = espacio libre, 1 = espacio ocupado

estacionamiento = [
    [0, 1, 0, 0, 1],
    [1, 0, 0, 1, 0],
    [1, 1, 1, 0, 0],
    [1, 1, 0, 0, 0]
]

ocupados_por_fila = []
mayor = -1

print("===== OCUPACIÓN POR FILA =====")
for i in range(len(estacionamiento)):
    ocupados = 0
    libres = 0
    for espacio in estacionamiento[i]:
        if espacio == 1:
            ocupados += 1
        else:
            libres += 1
    ocupados_por_fila.append(ocupados)
    print(f"Fila {i + 1}: {ocupados} ocupados, {libres} libres")
    if ocupados > mayor:
        mayor = ocupados

print()
filas_mayores = []
for i in range(len(ocupados_por_fila)):
    if ocupados_por_fila[i] == mayor:
        filas_mayores.append(i + 1)

if len(filas_mayores) == 1:
    print(f"La fila con mayor ocupación es la fila {filas_mayores[0]} ({mayor} vehículos).")
else:
    print(f"Hay empate entre las filas {filas_mayores} con {mayor} vehículos cada una.")
