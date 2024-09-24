#Classificação de Plantas Mágicas
#a. Descrição: Um botânico está classificando plantas mágicas em uma floresta. Ele quer saber se
#uma planta é pequena (menos de 1 metro), média (entre 1 e 3 metros), ou grande (mais de 3
#metros). Crie um programa que receba a altura da planta e informe a sua classificação.
#b. Conceito: Operadores relacionais, desvio condicional aninhado.

print("------------------------------------------------------------------------------------------")

n = float(input("Por favor, informe a altura da planta"))

if n < 1:
    print("A planta é de tamanho pequeno")
elif 1 <= n <= 3:
    print("A planta é de tamanho médio")
else:
    print("A planta é de tamanho grande")

print("------------------------------------------------------------------------------------------")