import random

#Computador
print('=-=-=-=-=-= Jogo da Adivinhação v2.0 =-=-=-=-=-=')
print('Aqui é seu computador ')
print('Tente adivinhar o número aleatoriamente de 0 a 10 ')

#Variaveis
rand = random.randint(0, 10)
acertou = False
t = 0 

#Resposta
while not acertou :
    q = int(input('Qual número você acha que é ? '))
    if q == rand:
        acertou = True
    elif q !=rand:
        acertou == False
    t += 1
print('Parabens você venceu !!! ')
print(f'Você tentou {t} vezes ')
