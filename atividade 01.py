# crie um programa que solicite uma nota entre 0 e 5. Se o valor digitado for
# inválido, o programa deve exibir uma mensagem de erro e continuar solicitando a nota até que um valor
# válido seja inserido.



while True:
    nota = int(input("Digite a nota de 0 a 5: "))
    
    if nota >= 0 and nota <= 5:
        print("Nota válida", {nota})
        break
    else:
        print("Error! Por favor digite uma nota de 0 a 5.")
      
        