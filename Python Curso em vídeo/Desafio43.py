print('-='*20)
print('INDICE DE MASSA CORPORAL ')
print('-='*20)
#IMC calculando
a = float(input('Qual é sua altura ? ')) 
p = float(input('Quanto você pesa? '))
x = p/(a**2)
print(f'Seu IMC é {x}')
#STATUS
if x <=18.5:
    print('Abaixo do peso')
elif 18.5< x <=25:
    print('Peso ideal')
elif 25 < x <=30:
    print('Sobrepeso')
elif 30 < x <35:
    print('Obesidade')
else :
    print('Obesidade morbita')
print('-='*20)
