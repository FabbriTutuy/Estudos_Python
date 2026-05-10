import time

soma = 0
for c in range (1,500):
    if c % 2 == 1 and c % 3 == 0:
        soma = soma + c
        print('{} é ímpar e multiplo de 3 e o valor atual da soma é {}'.format(c,soma))
        time.sleep(0.5)