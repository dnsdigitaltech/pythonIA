nome = input('Digite o seu nome: ')
idade = input('Digite a sua idade: ')

fruta_favorita = input('Qual é a sua fruta favorita? ')

print('olá ', nome+',', ' você tem ', idade, 'de idade')

#f-string  -> ajuda na hora de escrever um print() e concatenar valores

print(f'Olá {nome}, você tem {idade} de idade e a sua fruta favorita é {fruta_favorita}')