# Ejercicio 3. Cobro por tiempo de permanencia
import math

TARIFA_POR_HORA = 15

while True:
    try:
        horas = float(input("Tiempo de permanencia (horas): "))
        if horas > 0:
            break
        print("El tiempo debe ser mayor que 0.")
    except ValueError:
        print("Ingresa un número válido.")

# Se cobra la hora completa (menos de una hora = 1 hora)
horas_cobradas = math.ceil(horas)
importe = horas_cobradas * TARIFA_POR_HORA

print(f"Horas cobradas: {horas_cobradas}")
print(f"Importe a pagar: ${importe}")
