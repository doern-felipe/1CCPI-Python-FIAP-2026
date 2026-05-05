# EXERCÍCIO 7:
# ▪ Faça um programa que receba o ano de nascimento da pessoa e retorne:
# ▪ Se o voto é obrigatório este ano;
# ▪ Se o voto é opcional este ano;
# ▪ Se o voto é proibido este ano.

idade = int(input("Digite sua idade: "))

if idade < 16:
    print("Voto proibido este ano.")

elif idade == 16 or idade == 17 or idade >= 70:
    print("Voto opcional este ano.")
    
else:
    print("Voto obrigatório este ano.")