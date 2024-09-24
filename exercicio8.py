#Calculadora de Bônus
#a. Descrição: Um rei deseja distribuir bônus aos seus cavaleiros com base em suas conquistas. Se
#um cavaleiro completou mais de 10 missões, ele recebe um bônus de 100 moedas de ouro. Se
#completou entre 5 e 10 missões, recebe 50 moedas de ouro. Se completou menos de 5, recebe
#10 moedas de ouro. Crie um programa que receba o número de missões completadas e
#informe o valor do bônus.
#b. Conceito: Desvio condicional aninhado, operadores relacionais.

n = int(input("Informe o número de missões realizadas   "))

if n > 10:
    bonus1 = n * 100
    print(f"O valor do bônus a receber é de {bonus1}")
elif 5 <= n <= 10:
    bonus2 = n * 50
    print(f"O valor do bônus a receber é de {bonus2}")
else:
    bonus3 = n * 10
    print(f"O valor do bônus a receber é de {bonus3}")