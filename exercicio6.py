#Campeonato de Corrida de Dragões
#a. Descrição: Em um campeonato de corrida de dragões, cada dragão corre uma determinada
#distância em um certo tempo. Crie um programa que receba a distância e o tempo de dois
#dragões diferentes e determine qual dragão é mais rápido, ou se ambos têm a mesma
#velocidade.
#b. Conceito: Operadores aritméticos, operadores relacionais, desvio condicional composto.

print("------------------------------------------------------------------------------------------")

n1 = float(input("Informe a distância que o do dragão 1 percorre "))

n2 = float(input("Informe o tempo em que ele corre o dragão 1  "))

n3 = float(input("Informe a distância que o do dragão 2 percorre "))

n4 = float(input("Informe o tempo em que ele corre o dragão 2  "))

t1= n1/n3
t2 = n2/n4

if t1>t2:
    print("O dragão 1 é mais rápido")
elif t2>t1:
    print("O dragão 2 é mais rápido")
else:
    print("Os dois tem a mesma velocidade")

print("------------------------------------------------------------------------------------------")