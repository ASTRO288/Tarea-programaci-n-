# Ejercicio 9. Control de capacidad
import math

CAPACIDAD = 30
ocupados = 0
total_recaudado = 0

print(f"Capacidad máxima del estacionamiento: {CAPACIDAD} vehículos")

continuar = "s"

while ocupados < CAPACIDAD and continuar == "s":
    print("\n--- Nuevo vehículo ---")
    placa = input("Placa: ").upper()

    print("1. Motocicleta  2. Automóvil  3. Camioneta  4. Camión")
    opcion = ""
    while opcion not in ("1", "2", "3", "4"):
        opcion = input("Tipo de vehículo (1-4): ")
        if opcion not in ("1", "2", "3", "4"):
            print("Opción no válida.")

    if opcion == "1":
        tipo, tarifa = "Motocicleta", 10
    elif opcion == "2":
        tipo, tarifa = "Automóvil", 15
    elif opcion == "3":
        tipo, tarifa = "Camioneta", 20
    else:
        tipo, tarifa = "Camión", 30

    while True:
        try:
            horas = float(input("Horas de estancia: "))
            if horas > 0:
                break
            print("Las horas deben ser mayores que 0.")
        except ValueError:
            print("Ingresa un número válido.")

    importe = math.ceil(horas) * tarifa
    total_recaudado += importe
    ocupados += 1

    print(f"Placa {placa} ({tipo}) debe pagar: ${importe}")
    print(f"Espacios disponibles: {CAPACIDAD - ocupados}")

    if ocupados < CAPACIDAD:
        continuar = ""
        while continuar not in ("s", "n"):
            continuar = input("¿Registrar otro vehículo? (s/n): ").lower()

if ocupados == CAPACIDAD:
    print("\nEl estacionamiento está LLENO: no es posible recibir más vehículos.")

print(f"\nVehículos registrados: {ocupados}")
print(f"Espacios disponibles: {CAPACIDAD - ocupados}")
print(f"Total recaudado: ${total_recaudado}")
