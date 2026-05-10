#Números
n1 = int(input(' Escolha um Número '))
n2 = int(input('Escolha outro Número '))

#Menu
print('=-=-=-=-=-=-=-= Menu de Opções =-=-=-=-=-=-=-=')

print('[1] = Somar')
print('[2] = Multiplicar')
print('[3] = maior ')
print('[4] = números novos ')
print('[5] = Sair do programa ')

#Variaveis 
soma1 = n1+n2
multin1 = n1*n2

#Resultado 
r = int(input('Qual sua escolha? '))
if r == 1:
    print(f'O resultado da soma é : {soma1}')
elif r == 2:
    print(f'O resultado da Multiplicação é : {multin1}')
elif r == 3 :
    if n1>n2 :
        print(f'O maior é o {n1}')
    elif n2>n1:
        print(f'O maior é o {n2}')
    elif n2 == n1:
        print('Os dois tem o mesmo valor ')
elif r == 4 :
    n3 = int(input('Qual outro número você quer colocar? '))
    print('=-=-=-=-=- Menu diferente =-=-=-=-=')
    print('[1] = Somar ')
    print('[2] = Multiplicar ')
    print('[3] = Maior ')
    print('[4] = Sair do programa ')
    r2 = int(input('Qual sua escolha ? '))
    if r2 == 1 :
        print(f'A soma entre {n1} e {n2} é {soma2} , pois {n1} + {n2} + {n3} = {soma1 + n3}')
    elif r2 == 2:
        print(f'O resultado da multiplicação é {multin2} pois {n1} x {n2} x {n3} = {multin1 * n3}')
    elif r2 == 3:
        if n1>n2 and n2>n3:
            print(f'O maior é {n1}')
        elif n2>n1 and n1>n3:
            print(f'O maior é {n2}')
        elif n3>n1 and n1>n2 :
            print(f'O maior é {n3}')
        elif n3 == n2 == n1:
            print('Os três tem o mesmo valor ')
    elif r2 == 4:
        print('Obrigado(a)')
elif r == 5 :
    print (' Obrigado(a) :D')
print('-='*23)
#FIM :D
