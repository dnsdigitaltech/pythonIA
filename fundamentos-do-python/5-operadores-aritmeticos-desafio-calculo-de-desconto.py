preco = int(input('Digite o valor do produto: '))
desconto = int(input('Digite o valor do desconto: '))
#preco = 50 # Valor em R$
#desconto = 10 # Desconto em %

novo_preco = preco - (preco * desconto / 100)

print(f'O valor com desconto é de R$ {novo_preco}')