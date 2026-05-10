n = int(input('Escolha um número inteiro qualquer: '))

for c in range(1, n+1):
    if n % c == 0: 
        print(f' {c} Não é um número primo.', end=' , ')
print('É um número primo.')