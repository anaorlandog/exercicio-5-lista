#1. O Tesouro Escondido
#a. Descrição: Um mapa do tesouro tem duas partes, A e B. A primeira parte está escondida no X
#número de passos para o norte, e a segunda no Y número de passos para o leste. Crie um
#programa que receba os valores de X e Y e calcule a distância total que o pirata precisa
#percorrer para chegar ao tesouro (soma de X e Y).
#b. Conceito: Operadores aritméticos, variáveis.

print("------------------------------------------------------------------------------------------")

x = int(input("Por favor, informe o número de passos para X no norte  "))
y = int(input("Por favor, informe o número de passos para Y no leste  "))

distancia = x + y

print(f"A distância a percorrer é {distancia} passos para o tesouro")


print("------------------------------------------------------------------------------------------")