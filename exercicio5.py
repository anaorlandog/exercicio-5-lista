#Jornada no Deserto
#a. Descrição: Um explorador está cruzando um deserto. Ele precisa saber se a quantidade de
#água que tem é suficiente para chegar ao próximo oásis. Ele calcula que precisa de 2 litros de
#água para cada quilômetro. Crie um programa que receba a quantidade de água disponível e a
#distância até o oásis, e informe se a água é suficiente.
#b. Conceito: Operadores aritméticos, desvio condicional simples.


print("------------------------------------------------------------------------------------------")

n1 = int(input("Informe a quantidade de água que você possui"))

n2 = int(input("Informe a distância em km até o próximo oásis"))

agua = n2*2

if n1 >= agua:
    print("A quantidade de água é suficiente para chegar ao próximo oásis")
else:
    print("A quantidade de água não é suficiente, economize")

print("------------------------------------------------------------------------------------------")