# Ejercicio 6. Clasificación del tipo de vehículo
import math

print("Tipos de vehículo:")
print("1. Motocicleta ($10 por hora)")
print("2. Automóvil   ($15 por hora)")
print("3. Camioneta   ($20 por hora)")
print("4. Camión      ($30 por hora)")

opcion = ""
while opcion not in ("1", "2", "3", "4"):
    opcion = input("Elige el tipo de vehículo (1-4): ")
    if opcion not in ("1", "2", "3", "4"):
        print("Opción no válida.")

if opcion == "1":
    tipo = "Motocicleta"
    tarifa = 10
elif opcion == "2":
    tipo = "Automóvil"
    tarifa = 15
elif opcion == "3":
    tipo = "Camioneta"
    tarifa = 20
else:
    tipo = "Camión"
    tarifa = 30

while True:
    try:
        horas = float(input("Horas de estancia: "))
        if horas > 0:
            break
        print("Las horas deben ser mayores que 0.")
    except ValueError:
        print("Ingresa un número válido.")

horas_cobradas = math.ceil(horas)
importe = horas_cobradas * tarifa

print(f"\nTipo: {tipo}")
print(f"Tarifa por hora: ${tarifa}")
print(f"Horas cobradas: {horas_cobradas}")
print(f"Importe a pagar: ${importe}")
