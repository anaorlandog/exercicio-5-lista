#Guerreiro da Idade Média
#a. Descrição: Um guerreiro precisa de uma armadura especial para a batalha. Para forjar a
#armadura, ele precisa de uma liga metálica que combina ferro e ouro. O ferreiro diz que a liga
#precisa ter no mínimo 70% de ferro. Crie um programa que receba a quantidade de ferro e
#ouro em kg e verifique se a porcentagem de ferro na liga é suficiente.
#b. Conceito: Operadores aritméticos, operadores lógicos, desvio condicional simples.

print("------------------------------------------------------------------------------------------")

x = int(input("Por favor, informe a quantidade de ferro a ser utilizada"))
y = int(input("Por favor, informe a quantidade de ouro"))

z = x + y
ferro =  (x / z)*100

if ferro >= 70:
    print(f"A quantidade de ferro está adequado, corresponde a {ferro:.2f}")
else:
    print("Quantidade errada de ferro")

print("------------------------------------------------------------------------------------------")