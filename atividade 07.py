# Desenvolva um programa que leia 7 numeros inteiros e, ao final, informe
# qual foi o menor numero digitado.

Lista = None # variável para armazenar menor numero.

for i in range(7): # Repetimos o processo 7 vezes (índices de 0 a 6).
    numeros = int(input(f"Digite o numero {i+1} número inteiro: "))

    if Lista is None or numeros < Lista:
        Lista = numeros # Vai atualiza o menor numero digitado.
    print("O menor número digitado foi: ", Lista)