a1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
for a in range(0, 10):
    a1 = a1 + r
    print('{} → '.format(a1-r), end='')
print('ACABOU')