#A Caverna dos Desafios
#a. Descrição: Um aventureiro encontrou uma caverna cheia de portas, cada uma com um número
#de 1 a 5. Atrás de cada porta há um desafio. Crie um programa que receba o número da porta
#escolhido pelo aventureiro e use match-case para mostrar qual desafio ele enfrentará.
#b. Conceito: Match-case, operadores relacionais.

porta = int(input("Informe um número de 1 a 5 para escolher a porta   "))

match porta:
    case 1: 
        print("O desafio escolhido foi vá até ao pé de laranja")
    case 2: 
        print("O desafio escolhido foi: cave um buraco")
    case 3: 
        print("O desafio escolhido foi: descanse")
    case 4:
        print("O desafio escolhido foi: plante um pé de maçã")
    case 5: 
        print("O desafio escolhido foi: volte para a porta 1")
    case _:
        print("Escolha um número válido")