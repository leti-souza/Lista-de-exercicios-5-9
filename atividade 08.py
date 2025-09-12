# Faça um programa que leia 6 números e, ao final, exiba o produto de todos os numeros e a 
# média aritmética entre eles.
# 1 - ler 6 números
# 2 - calcular o produto entre eles
# 3 - calcular a média aritmética entre eles

produto = 1
soma = 0

for numero in range(6):
    valores = float(input("Digite um número: "))
    produto *= valores  # -> produto = produto * valores
    soma += valores    # -> soma = soma + valores

media = soma / 6
print(f"O produto dos números é {produto:.2f} e a média aritmética é {media:.2f}.")