# Operadores Lógicos

# AND E um e o outro
# OR OU um ou o outro
# NOT NÃO nem um nem o outro

# Para dirigir a pessoa tem quer ser maior que 18 anos de  idade e ter carteira de motorista

idade  = int(input('Qual é sua idade? '))
carteira  = False
verificador = idade >= 18 and carteira

print(verificador)