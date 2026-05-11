# EXERCÍCIO 1
# ▪ Faça um programa que exiba a mensagem “Olá, Mundo”.
# ▪ Essa mensagem deverá ser exibida repetidamente.
# ▪ Ao final de toda interação da repetição, você deve perguntar ao usuário se ele deseja exibir a mensagem
# novamente.
# ▪ Se sim, exiba novamente. Senão, saia do loop e exiba a mensagem “Fim”.

while True:
    print("Olá, Mundo")
    
    resposta = input("Deseja exibir a mensagem novamente? (s/n): ")
    
    if resposta != 's':
        break

print("Fim")