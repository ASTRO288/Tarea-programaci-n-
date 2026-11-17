# Ejercicio 4. Tarifas diferenciadas
import math

while True:
    try:
        horas = float(input("Tiempo de permanencia (horas): "))
        if horas > 0:
            break
        print("El tiempo debe ser mayor que 0.")
    except ValueError:
        print("Ingresa un número válido.")

if horas <= 2:
    tarifa = 20
elif horas <= 5:
    tarifa = 18
else:
    tarifa = 15

horas_cobradas = math.ceil(horas)   # hora iniciada = hora completa
importe = horas_cobradas * tarifa

print(f"Tarifa aplicada: ${tarifa} por hora")
print(f"Horas cobradas: {horas_cobradas}")
print(f"Importe a pagar: ${importe}")
