# Faça um programa que solicite um nome de usuário e uma senha. A senha não pode
# ser igual ao nome de usuário nem conter o nome de usuário como parte dela.
# caso a regra seja violada, exiba uma mensagem de erro e peça as informações
# novamente.

while True:
    usuário = input("Por favor, digite seu nome de usuário: ").lower()
    senha = input("Por favor, Digite a sua senha: ")

    if senha == usuário:
        print(" ERROR! Por favor, digite uma senha válida!") 
    elif usuário in senha:
        print("ERROR! A senha não pode conter o nome do usuário.")
    else:
        print("Usuário e senhas Corretos!")
        break