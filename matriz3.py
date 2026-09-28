print("--- DATOS DE LA MATRIZ A ---")
matriz_A = []
for i in range(2):
    matriz_A.append([])
    for j in range(2):
        matriz_A[i].append(int(input(f"ingrese el valor {i+1}, {j+1} para A: ")))


print("\n--- DATOS DE LA MATRIZ B ---")
matriz_B = []
for i in range(2):
    matriz_B.append([])
    for j in range(2):
        matriz_B[i].append(int(input(f"ingrese el valor {i+1}, {j+1} para B: ")))

matriz_C = []
for i in range(2):
    matriz_C.append([])
    for j in range(2):
        
        suma_posicion = matriz_A[i][j] + matriz_B[i][j]
        matriz_C[i].append(suma_posicion)


print("\nMatriz A:")
for fila in matriz_A:
    print(fila)

print("\nMatriz B:")
for fila in matriz_B:
    print(fila)

print("\nLa matriz suma (A + B) es:")
for fila in matriz_C:
    print(fila)