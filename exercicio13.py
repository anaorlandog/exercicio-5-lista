#Sistema de Defesa de Castelos
#a. Descrição: O sistema de defesa de um castelo mágico precisa estar sempre ativo quando o
#exército do rei está fora. Crie um programa que receba a posição do exército (dentro ou fora
#do castelo) e use match-case para ativar ou desativar o sistema de defesa automaticamente.
#b. Conceito: Match-case, operadores lógicos, desvio condicional.

local = input("O exército está dentro ou fora do castelo?   ").lower()

match local:
    case "dentro":
        print("Sitema de defesa desativado")
    case "fora":
        print("Sistema de defesa ativado")
    case _: 
        print("Informe o local correto")
