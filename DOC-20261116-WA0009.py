# Ejercicio 2. Cálculo del tiempo de estancia

print("Escribe las horas en formato de 24 h; puedes usar decimales (8.5 = 8:30).")

while True:
    try:
        hora_entrada = float(input("Hora de entrada: "))
        if 0 <= hora_entrada < 24:
            break
        print("La hora debe estar entre 0 y 23.99.")
    except ValueError:
        print("Ingresa un número válido.")

while True:
    try:
        hora_salida = float(input("Hora de salida: "))
        if 0 <= hora_salida < 24:
            break
        print("La hora debe estar entre 0 y 23.99.")
    except ValueError:
        print("Ingresa un número válido.")

if hora_salida >= hora_entrada:
    tiempo = hora_salida - hora_entrada
else:
    # El vehículo salió después de la medianoche
    tiempo = (24 - hora_entrada) + hora_salida

minutos_totales = round(tiempo * 60)
horas, minutos = divmod(minutos_totales, 60)

print(f"\nTiempo de estancia: {tiempo:.2f} horas ({horas} h {minutos} min)")
