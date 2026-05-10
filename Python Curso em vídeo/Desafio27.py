n = str(input('Qual é seu nome ?')).strip()
nome1 = n.split()
print (f'Seu primeiro nome é {nome1[0]}')
print (f'Seu ultimo nome é {nome1[len(nome1)-1]}')
