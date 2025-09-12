# Suponha que a população de uma cidade A seja de 90.000 habitantes, com uma taxade crescimento anual de 3.5%
# e que a população de uma cidade B seja 250.000 habitantes, com uma taxa de crescimento anual de 1.2%.
# Desenvolva um programa que calcule e informe o número de anos necessários para que a população
# da cidade A ultrapasse ou iguale a população da cidade B, considerando as taxas de crescimento constante.

cidade_A = 90000
cidade_B = 250000
taxa_crescimento_A = 0.035
taxa_crescimento_B = 0.012

anos = 0

while cidade_A < cidade_B: # enquanto a população da cidade A for MENOR que a população da cidade B
    cidade_A = cidade_A + (cidade_A * taxa_crescimento_A) # população da cidade A cresce 3.5% ao ano
    cidade_B = cidade_B + (cidade_B * taxa_crescimento_B) # população da cidade B cresce 1.2% ao ano
    anos += 1  # anos = anos + 1
    s = anos + 1  # contador de anos

#    print(f"Após {anos} anos, a população da cidade A será de {float(cidade_A)} habitantes"
 #         f"\n e a população da cidade B será de {float(cidade_B)} habitantes.")

print(f"Serão necessários {anos} anos para que a população da cidade A ultrapasse ou iguale a população da cidade B.")  