import random

print('Tente adivinhar o número que eu escolhi aleatoriamente de 0 a 5')
n = int(input('Digite o número que você acha '))
random = random.randint(0,5)
if n == random:
    print('Parabens você venceu ')
else:
    print('O computador venceu ')
print('---FIM---')
