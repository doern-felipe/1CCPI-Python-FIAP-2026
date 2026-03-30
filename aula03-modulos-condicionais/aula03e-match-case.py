escolha_usuario = 0
# 0 > sai do programa
# 1 > entra no programa

match escolha_usuario:
    case 0:
        print("Sair do Programa")
    case 1:
        print("Entrar no Programa")
    case _:
        print("ERRO!")