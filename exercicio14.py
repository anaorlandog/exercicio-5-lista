#O Julgamento do Sábio
#a. Descrição: Um sábio está julgando um duelo entre dois guerreiros. Ele quer saber qual
#guerreiro deve ser considerado vencedor, com base em suas habilidades de ataque e defesa.
#Crie um programa que receba os valores de ataque e defesa dos dois guerreiros e determine o
#vencedor (aquele com maior soma de ataque e defesa). Se houver empate, o programa deve
#considerar a defesa como critério de desempate.
#b. Conceito: Operadores aritméticos, relacionais, desvio condicional aninhado.

ataque1 = int(input("Poder de ataque do guerreiro 1  "))
defesa1 = int(input("Poder de defesa do guerreiro 1  "))
soma1 =  ataque1 + defesa1

ataque2 = int(input("Poder de ataque do guerreiro 2  "))
defesa2 = int(input("Poder de defesa do guerreiro 2  "))
soma2 =  ataque1 + defesa1

if soma1 > soma2:
    print("O guerreiro 1 é vencedor")
elif soma2 > soma1:
    print("O guerreiro 2 é o vencedor")
else:
    if soma1 > soma2:
        print("O guerreiro 1 é o vencedor por defesa")
    elif soma2 > soma1:
        print("O guerreiro 2 é o vencedor por defesa")
    else:
        print("O duelo empatou")