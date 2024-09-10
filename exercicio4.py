#Contagem de Moedas
#a. Descrição: Um colecionador de moedas tem 3 tipos de moedas: de 1 real, de 50 centavos e de
#25 centavos. Escreva um programa que receba a quantidade de cada tipo de moeda e calcule o
#valor total que o colecionador tem.
#b. Conceito: Operadores aritméticos, tipos de dados (float).

print("------------------------------------------------------------------------------------------")

x = int(input("Informe a quantidade de moedas de R$1,00  "))

y = float(input("Informe a quantidade de moedas de R$0,50  "))

z = float(input("Informe a quantidade de moedas de R$0,25  "))

total = x*1 + y*0.5 + z*0.25

print(f"O valor total é R${total:.2f}")

print("------------------------------------------------------------------------------------------")