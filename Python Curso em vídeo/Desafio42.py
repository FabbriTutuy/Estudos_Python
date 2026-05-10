print('-='*20)
print('Analaisador de triângulos'.upper())
print('-='*20)
r1 = float(input('Qual o primeiro segmento do triângulo? '))
r2 = float(input('Qual o segundo segmento? '))
r3 = float(input('Qual o terceiro segmento? '))
if r1<r2+r3 and r2<r1+r3 and r3<r1+r2:
    print('Os segmentos pode formar um triângulo ', end='')
    if r1 == r2 == r3 :
        print('Equilátero')
    elif r1!=r2!=r3!=r1:
        print('Escaleno')
    else:
        print('Isósceles') 
else:
    print('Os segmentos não podem formar um triângulo')

