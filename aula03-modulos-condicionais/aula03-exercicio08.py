# EXERCÍCIO 8:
# ▪ Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado
# no salário atual:
# ▪ Salários até R$ 280,00 (incluindo): aumento de 20%.
# ▪ Salários entre R$ 280,00 e R$ 700,00: aumento de 15%.
# ▪ Salários entre R$ 700,00 e R$ 1500,00: aumento de 10%.
# ▪ Salários de R$ 1500,00 em diante: aumento de 5%.
# ▪ Após o aumento ser realizado, informe na tela:
# ▪ O salário antes do reajuste.
# ▪ O percentual de aumento aplicado.
# ▪ O valor do aumento.
# ▪ O novo salário, após o aumento.

salario = float(input("Digite seu salário: "))

if salario <= 280.00:
    aumento = salario * 0.2
    novo_salario = salario + aumento
    print(f"\nSeu salário de R${salario:.2f} obteve um aumento de 20%.")
    print(f"20% é equivalente a R${aumento:.2f}.")
    print(f"Seu novo salário é de R${novo_salario:.2f}!")

elif 280.00 < salario < 700.00:
    aumento = salario * 0.15
    novo_salario = salario + aumento
    print(f"\nSeu salário de R${salario:.2f} obteve um aumento de 15%.")
    print(f"15% é equivalente a R${aumento:.2f}.")
    print(f"Seu novo salário é de R${novo_salario:.2f}!")

elif 700.00 <= salario < 1500.00:
    aumento = salario * 0.1
    novo_salario = salario + aumento
    print(f"\nSeu salário de R${salario:.2f} obteve um aumento de 10%.")
    print(f"10% é equivalente a R${aumento:.2f}.")
    print(f"Seu novo salário é de R${novo_salario:.2f}!")

elif salario >= 1500.00:
    aumento = salario * 0.05
    novo_salario = salario + aumento
    print(f"\nSeu salário de R${salario:.2f} obteve um aumento de 5%.")
    print(f"5% é equivalente a R${aumento:.2f}.")
    print(f"Seu novo salário é de R${novo_salario:.2f}!")