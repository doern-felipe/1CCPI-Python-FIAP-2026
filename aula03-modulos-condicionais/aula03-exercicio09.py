# EXERCÍCIO 9:
# ▪ Faça um programa que recebe:
# ▪ o código do estado de origem da carga de um caminhão, supondo que é um número inteiro de 1 a 5
# ▪ o peso da carga do caminhão em toneladas
# ▪ o código da carga, supondo que é um número inteiro de 10 e 40
# ▪ Seu programa deve calcular:
# ▪ o peso da carga do caminhão convertido em quilos
# ▪ o preço da carga do caminhão
# ▪ valor do imposto que e cobrado com base no preço da carga e do estado de origem
# ▪ o valor total transportado pelo caminhão (carga + impostos)

# ▪ Utilize as seguintes tabelas:
# estado             |   imposto
# 1                  |   35%
# 2                  |   25%
# 3                  |   15%
# 4                  |   5%
# 5                  |   isento

# código da carga    |   preço por kg
# 10 a 20            |   100,00
# 21 a 30            |   250,00
# 31 a 40            |   340,00

# ▪ Obs.: considere que o usuário irá digitar tudo corretamente.

# --- --- --- --- ---

# Menu:
print("""
 _________________________           ____________________________________
|estado        |  imposto |         |código da carga    |   preço por kg|
|1             |  35%     |         |10 a 20            |   100,00      |
|2             |  25%     |         |21 a 30            |   250,00      |
|3             |  15%     |         |31 a 40            |   340,00      |
|4             |  5%      |         |___________________|_______________|
|5             |  isento  |
|______________|__________|
""")

# Receber informações:
cod_est_org = int(input("Digite o Código do Estado de Origem da carga: "))
peso_carga_t = float(input("Digite o peso da carga em toneladas(T): "))
cod_carga = int(input("Digite o Código da carga: "))

# Toneladas para Quilogramas:
peso_carga_kg = peso_carga_t * 1000

# Preço da Carga:
if 10 <= cod_carga <= 20:
    preco_carga = peso_carga_kg * 100.00
elif 21 <= cod_carga <= 30:
    preco_carga = peso_carga_kg * 250.00
elif 31 <= cod_carga <= 40:
    preco_carga = peso_carga_kg * 340.00

# Valor do Imposto:
if cod_est_org == 1:
    valor_imposto = preco_carga * 0.35
elif cod_est_org == 2:
    valor_imposto = preco_carga * 0.25
elif cod_est_org == 3:
    valor_imposto = preco_carga * 0.15
elif cod_est_org == 4:
    valor_imposto = preco_carga * 0.05
elif cod_est_org == 5:
    valor_imposto = preco_carga * 0

# Valor Total:
valor_total = preco_carga + valor_imposto
print(f"O valor total a ser pago é R${valor_total:.2f}.")