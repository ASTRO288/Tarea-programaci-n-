# Ejercicio 15. Conteo de espacios disponibles
# 0 = espacio libre, 1 = espacio ocupado

estacionamiento = [
    [0, 1, 0, 0, 1],
    [1, 0, 0, 1, 0],
    [0, 0, 1, 0, 0],
    [1, 1, 0, 0, 0]
]

total = 0
ocupados = 0
libres = 0

for fila in estacionamiento:
    for espacio in fila:
        total += 1
        if espacio == 1:
            ocupados += 1
        else:
            libres += 1

porcentaje = ocupados / total * 100

print("===== OCUPACIÓN DEL ESTACIONAMIENTO =====")
print(f"Total de espacios:      {total}")
print(f"Espacios ocupados:      {ocupados}")
print(f"Espacios libres:        {libres}")
print(f"Porcentaje de ocupación: {porcentaje:.1f}%")
