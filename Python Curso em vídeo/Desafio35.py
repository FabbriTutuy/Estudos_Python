print('-='*20)
print('Analisador de Triângulos ')
print('-='*20)
r1 = float(input('Qual o primeiro segmento? '))
r2 = float(input('Qual o Segundo segmento? '))
r3 = float(input('Qual é o Terceiro segmento?'))
if r1<r2+r3 and r2<r1+r3 and r3<r1+r2 :
    print('Os segmentos podem formar um triangulo ')
else:
    print('Os Segmentos não podem formar um triangulo ')

