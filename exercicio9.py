#Escolha de Feitiços
#a. Descrição: Um mago tem três feitiços: fogo, água e terra. Crie um programa que receba a
#escolha do usuário (1 para fogo, 2 para água, 3 para terra) e use o comando match-case para
#exibir o feitiço escolhido.
#b. Conceito: Match-case, variáveis.

feitiço = int(input("Inform o número do feitiço que deseja: 1 - Fogo 2 - Água 3 - Terra    "))

match feitiço:
    case 1: 
        print("O feitiço escolhido foi FOGO!")
    case 2: 
        print("O feitiço escolhido foi ÁGUA!")
    case 3: 
        print("O feitiço escolhido foi TERRA!")
    case _:
        print("Escolha inválida, escolha de novo")