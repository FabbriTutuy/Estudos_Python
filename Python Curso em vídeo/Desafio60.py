import math

print('=-=-=-=-= Calculo de fatorial =-=-=-=-=')
n = int(input('Escolha um número para fatorar: '))
c = n 
f = math.factorial(n)
while c > 0 :
    print(f'{c}',end = ' ')
    if c == 1:
        print('=' , end=' ')
    else :
        print('x',end = ' ')
    c-=1 
print(f'{f}')
print('=-='*20)
