# Ejercicio 8. Corte de caja
import math

total_vehiculos = 0
motocicletas = 0
automoviles = 0
camionetas = 0
camiones = 0
total_recaudado = 0

continuar = "s"

while continuar == "s":
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
        motocicletas += 1
    elif opcion == "2":
        tipo, tarifa = "Automóvil", 15
        automoviles += 1
    elif opcion == "3":
        tipo, tarifa = "Camioneta", 20
        camionetas += 1
    else:
        tipo, tarifa = "Camión", 30
        camiones += 1

    while True:
        try:
            horas = float(input("Horas de estancia: "))
            if horas > 0:
                break
            print("Las horas deben ser mayores que 0.")
        except ValueError:
            print("Ingresa un número válido.")

    importe = math.ceil(horas) * tarifa
    total_vehiculos += 1
    total_recaudado += importe
    print(f"Placa {placa} ({tipo}) debe pagar: ${importe}")

    continuar = ""
    while continuar not in ("s", "n"):
        continuar = input("¿Registrar otro vehículo? (s/n): ").lower()

print("\n========== CORTE DE CAJA ==========")
print(f"Total de vehículos atendidos: {total_vehiculos}")
print(f"Motocicletas: {motocicletas}")
print(f"Automóviles:  {automoviles}")
print(f"Camionetas:   {camionetas}")
print(f"Camiones:     {camiones}")
print(f"Importe total recaudado: ${total_recaudado}")
print("===================================")
