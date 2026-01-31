# Operadores Lógicos

# AND E um e o outro
# OR OU um ou o outro
# NOT NÃO nem um nem o outro

# Para dirigir a pessoa tem quer ser maior que 18 anos de  idade e ter carteira de motorista

usuario  = int(input('Digite seu usuário '))
senha  = int(input('Digite seu senha '))

login_valido = usuario == senha

print(f'Login Permitido: {login_valido}')