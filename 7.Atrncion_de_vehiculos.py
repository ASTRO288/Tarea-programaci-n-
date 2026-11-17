# Ejercicio 7. Atención de varios vehículos
import math

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
    print(f"Placa {placa} ({tipo}) debe pagar: ${importe}")

    continuar = ""
    while continuar not in ("s", "n"):
        continuar = input("¿Registrar otro vehículo? (s/n): ").lower()

print("\nRegistro finalizado.")
