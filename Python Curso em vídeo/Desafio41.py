print('-='*20)
print('Qual progesso ta o nadador'.upper())
print('-='*20)
n = int(input('Quantos anos o nadador? '))
if n == 0 :
    print('Mirim')
elif 0< n <=9:
    print('Mirim')
elif 9< n <=14:
    print('Infantil')
elif 14< n <=19:
    print('Junior')
elif 19< n <=20:
    print('Sênior')
else:
    print('Master')

print('-='*20)