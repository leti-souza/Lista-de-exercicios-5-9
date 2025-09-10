# crie um programa que imprima na tela todos os numeros múltiplos de 3 que estão no intervalo entre1 e 60.

for numeros in range(1, 61):  # seleciona apenas os números de 1 até 60.
    if numeros % 3 == 0:
        print(numeros) # verifica se o número é múltiplo de 3.


# outra forma:

for numeros in range(3, 61, 3): #começa do 3 e pulamos de 3 em 3 até 60.
    print(numeros)