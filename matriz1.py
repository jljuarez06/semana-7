matriz = [
    [1,2],
    [3,4]
]

for file in matriz:
    print(file)

#escalar
k = 5

matrizB = []
for i in range (len(matriz)):
    matrizB.append([])
    for j in range(len(matriz)):
        matrizB[i].append(k * matriz[i][j])

print("=" * 13)
print("Escalar",k)
for file in matrizB:
    print(file)