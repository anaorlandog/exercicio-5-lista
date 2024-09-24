#Decisão da Coroa Real
#a. Descrição: O conselho real precisa tomar uma decisão crítica: selecionar o próximo
#governante entre três candidatos, baseado na sua pontuação em uma série de provas. Crie um
#programa que receba as notas dos três candidatos e determine qual deles teve a maior média.
#Caso duas ou mais médias sejam iguais, o programa deve exibir uma mensagem informando
#que há um empate.
#b. Conceito: Operadores aritméticos, relacionais, desvio condicional aninhado.

nota1_candidato1 = float(input("Nota 1 do Candidato 1: "))
nota2_candidato1 = float(input("Nota 2 do Candidato 1: "))
nota3_candidato1 = float(input("Nota 3 do Candidato 1: "))
media_candidato1 = (nota1_candidato1 + nota2_candidato1 + nota3_candidato1) / 3

nota1_candidato2 = float(input("Nota 1 do Candidato 2: "))
nota2_candidato2 = float(input("Nota 2 do Candidato 2: "))
nota3_candidato2 = float(input("Nota 3 do Candidato 2: "))
media_candidato2 = (nota1_candidato2 + nota2_candidato2 + nota3_candidato2) / 3

nota1_candidato3 = float(input("Nota 1 do Candidato 3: "))
nota2_candidato3 = float(input("Nota 2 do Candidato 3: "))
nota3_candidato3 = float(input("Nota 3 do Candidato 3: "))
media_candidato3 = (nota1_candidato3 + nota2_candidato3 + nota3_candidato3) / 3

if media_candidato1 > media_candidato2 and media_candidato1 > media_candidato3:
    print("O Candidato 1 é o vencedor")
elif media_candidato2 > media_candidato1 and media_candidato2 > media_candidato3:
    print("O Candidato 2 é o vencedor")
elif media_candidato3 > media_candidato1 and media_candidato3 > media_candidato2:
    print("O Candidato 3 é o vencedor")
else:
    print("Temos um empate!")