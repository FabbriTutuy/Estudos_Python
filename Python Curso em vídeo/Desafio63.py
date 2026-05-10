print('-----------------------------')
print(' Sequência de Fibonacci v1.0 ')
print('-----------------------------')

f = int(input('Quantos termos de Fibonacci você quer mostra ?  '))
contador = 3
t1 = 0
t2 = 1 
print(f'{t1} -> {t2}', end= '')
while contador <=f:
    t3 = t1 + t2
    print(f'{t3} -> ', end= '')
    contador += 1
    t1 = t2
    t2 = t3
print('Pausa ... ')
print('-'*29)