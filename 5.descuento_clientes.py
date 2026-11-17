# Ejercicio 5. Descuentos para clientes frecuentes

while True:
    texto = input("Número de visitas del cliente en el mes: ")
    if texto.isdigit():
        visitas = int(texto)
        break
    print("Ingresa un número entero válido (0 o mayor).")

while True:
    try:
        importe = float(input("Importe de la estancia: $"))
        if importe >= 0:
            break
        print("El importe no puede ser negativo.")
    except ValueError:
        print("Ingresa un número válido.")

if visitas > 10:
    descuento = importe * 0.10
    print("Cliente frecuente: se aplica 10% de descuento.")
else:
    descuento = 0
    print("Cliente regular: tarifa normal.")

total = importe - descuento

print(f"Importe: ${importe:.2f}")
print(f"Descuento: ${descuento:.2f}")
print(f"Total a pagar: ${total:.2f}")
