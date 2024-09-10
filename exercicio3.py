#Adivinhação de Animais
#a. Descrição: Imagine que você é um mago que pode adivinhar o animal favorito das pessoas.
#Crie um programa que pergunte à pessoa se seu animal favorito é mamífero ou réptil. Se for
#mamífero, o programa deve sugerir que é um cachorro; se for réptil, o programa deve sugerir
#que é uma tartaruga.
#b. Conceito: Desvio condicional composto, variáveis.

print("------------------------------------------------------------------------------------------")

x = input("O seu animal favorito é um mamífero ou réptil?")

if x.lower() == "mamífero":
    print("O seu animal preferio é um cachorro")
elif x.lower() == "réptil":
    print("O seu animal preferido é a tartaruga")
else:
    print("Não consegui adivinhar seu animal favorito")
    

print("------------------------------------------------------------------------------------------")