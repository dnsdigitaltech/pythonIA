total_porcoes = int(input('Quantas porções o produto tem? '))
procoes_por_dia = int(input('Quantas porções você usa por dia? '))

dias  = total_porcoes / procoes_por_dia

print(f'O produto vai durar  {dias:.0f} dias!')

