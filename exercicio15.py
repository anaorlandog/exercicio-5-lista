#Portal de Viagem no Tempo
#a. Descrição: Um cientista está criando um portal de viagem no tempo que só pode ser ativado se
#todos os parâmetros estiverem corretos: energia acima de 80%, coordenadas de destino
#precisas, e o tempo ajustado corretamente. Crie um programa que receba esses valores e use
#operadores lógicos para verificar se o portal pode ser ativado. Se qualquer parâmetro estiver
#incorreto, o programa deve indicar qual é o problema.
#b. Conceito: Operadores lógicos, relacionais, desvio condicional aninhado.

energia =  int(input("Informe o percentual de energia do portal  "))

destino = input("As coordenadas do destino estão corretas: Responda com sim/não").lower()

tempo = input("Os dados do tempo estão corretos? Responda com sim/não").lower()

if energia >80 and destino == "sim" and tempo == "sim":
    print("O portal pode ser ativado")
else:
    if energia <= 80:
        print("A energia do portal está baixa")
    if destino == "não":
        print("As coordenadas do destino não estão corretas")
    if tempo == "não":
        print("Os dados do tempo estão erradas")
