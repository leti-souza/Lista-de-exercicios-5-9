# Desenvolva um programa que receba dois números inteiros e gere uma lista com todos os números pares que
# estão no intervalo entre eles (inclusive).

numero_inicial = int(input("Digite o primeiro número inteiro: "))
numero_final = int(input("Digite o último número inteiro: "))

numero_menor = min(numero_inicial, numero_final)
numero_maior = max(numero_inicial, numero_final)

numero_par = []
for numero in range(numero_menor, numero_maior + 1):
    if numero % 2 == 0:
        numero_par.append(numero)

print(numero_par)