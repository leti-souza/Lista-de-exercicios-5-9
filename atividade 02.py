# Desenvolva um programa que leia e valide as seguintes informações de uma formulário:
# Nome: Mínimo de 4 caracteres.
# Idade: Entre 1 e 100 anos.
# Salário: DEve ser um valor positivo.
# Gênero: 'f' (feminino), 'm'm (masculino) ou 'o' (outro).
# situação Empregatícia: 'e' (empregado), 'd' (desempregado),'a' (autonomo).

nome = input("Digite seu nome (mínimo 4 caracteres): ")
while len(nome) < 4: # enquanto o tamanho do nome for menor que 4 vai pedir para o usuário digitar novamente
    nome = input("Nome inválido. Digite seu nome (mínimo 4 caracteres): ") 
    
idade = int(input("Digite sua idade (entre 1 e 100 anos): "))
while idade < 1 or idade > 100:  # enquanto a idade for menor que 1 ou maior que 100 vai pedir para o usuário digitar novamente
    idade = int(input("Idade inválida. Digite sua idade (entre 1 e 100 anos): "))
    
salario = float(input("Digite seu salário (valor positivo): "))
while salario <= 0: # enquanto o salário for menor ou igual a 0 vai pedir para o usuário digitar novamente
    salario = float(input("Salário inválido. Digite seu salário (valor positivo): "))
    
genero = input("Digite seu gênero ('f' - feminino, 'm' - masculino, 'o' - outro): ").lower()
while genero not in ['f', 'm', 'o']: # enquanto o gênero não estiver entre as opções válidas vai pedir para o usuário digitar novamente
    genero = input("Gênero inválido. Digite seu gênero ('f' - feminino, 'm' - masculino, 'o' - outro): ").lower()
    
situacao_empregaticia = input("Digite sua situação empregatícia ('e'- empregado, 'd'- desempregado, 'a'- autônomo): ").lower()
while situacao_empregaticia not in ['e', 'd', 'a']: # enquanto a situação empregatícia não estiver entre as opções válidas vai pedir para o usuário digitar novamente
    situacao_empregaticia = input("Situação empregatícia inválida. Digite sua situação empregatícia ('e'- empregado, 'd'- desempregado, 'a'- autônomo): ").lower()

print("Formulário preenchido com sucesso!")  
print(f"Nome: {nome}")
print(f"Idade: {idade}")   
print(f"Salário: {salario:.2f}")
print(f"Gênero: {genero}")
print(f"Situação Empregatícia: {situacao_empregaticia}")  