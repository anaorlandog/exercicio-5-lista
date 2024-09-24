#A Batalha Final
#a. Descrição: Um herói precisa decidir qual arma usar na batalha final. Ele tem três armas: uma
#espada, um arco e uma lança. Cada arma tem um poder de ataque e uma durabilidade. A
#escolha deve considerar que o poder de ataque seja maior que 50 e a durabilidade maior que
#70. Crie um programa que receba os valores de ataque e durabilidade das três armas e
#determine qual é a mais adequada. Se nenhuma atender, o programa deve sugerir que o herói
#busque uma nova arma.
#b. Conceito: Operadores lógicos, relacionais, desvio condicional aninhado.

from random import randint

espada_atq = randint(30,120)
espada_dur = randint(40,80)

arco_atq = randint(20,90)
arco_dur = randint(80,150)

lanca_atq = randint(70,100)
lanca_dur = randint(30,120)

if espada_atq > 50 and espada_dur > 70:
    print("Espada")
elif arco_atq >50 and arco_dur > 70:
    print("Arco")
elif lanca_atq > 50 and lanca_dur > 70:
    print("Lança")
else:
    print("Escolha outra arma")

