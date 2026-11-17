# Ejercicio 13. Distribución de espacios
# 0 = espacio libre, 1 = espacio ocupado

estacionamiento = [
    [0, 1, 0, 0, 1],
    [1, 0, 0, 1, 0],
    [0, 0, 1, 0, 0],
    [1, 1, 0, 0, 0]
]

print("DISTRIBUCIÓN DEL ESTACIONAMIENTO (0 = libre, 1 = ocupado)\n")

# Encabezado de columnas
print("        ", end="")
for j in range(len(estacionamiento[0])):
    print(f"Esp {j + 1}", end="  ")
print()

# Recorrido con ciclos anidados
for i in range(len(estacionamiento)):
    print(f"Fila {i + 1}: ", end="")
    for j in range(len(estacionamiento[i])):
        print(f"  {estacionamiento[i][j]}  ", end="  ")
    print()
