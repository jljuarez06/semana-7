filas = int(input("introduce el numero de filas: "))
columnas = int(input("introduce el numero de columnas: "))

matriz = []

for i in range(filas):
    fila = []
    for j in range(columnas):

        valor = eval(input(f"introduce el numero para la posicion [{i}][{j}]: "))
        fila.append(valor)
    matriz.append(fila)

print("\nTu matriz final es: ")
for fila in matriz:
    print(fila)