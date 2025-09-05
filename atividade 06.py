# Crie um programa que imprima os numeros de 1 a 30 em uma unica linha, 
# separados por um hífen (ex: 1-2-3-4-5...- 30)

Lista = []

for contagem in range(1, 31): #contagem é uma variável e Range
    Lista.append(str(contagem)) # O append adiciona um item ao final de uma lista.

numeros_lista = '-'.join(Lista)
print(numeros_lista)
#print('-'.join(str(i) for i in range(1, 31)))