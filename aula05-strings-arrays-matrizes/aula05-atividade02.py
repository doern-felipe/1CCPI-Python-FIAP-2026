# ▪ Preencher uma matriz 4x5 de números inteiros com os números de 1 até 20.
# ▪ Matriz solução da atividade:
#     0  1  2  3  4 
#  0  1  2  3  4  5 
#  1  6  7  8  9  10
#  2  11 12 13 14 15
#  3  16 17 18 19 20

# Criacao da Matriz:
matriz = []
numero = 1

for i in range(4):
    linha = []
    for j in range(5):
        linha.append(numero)
        numero += 1
    matriz.append(linha)

# Exibindo a Matriz:
for linha in matriz:
    print(linha)