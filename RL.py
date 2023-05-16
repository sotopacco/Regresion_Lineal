import random

# Crear un array vacío
datos = []

# Generar 50 datos aleatorios y agregarlos al array
for _ in range(50):
    dato = random.randint(1, 100)  # Generar un número entero aleatorio entre 1 y 100
    datos.append(dato)

# Imprimir el array de datos generados
print(datos)