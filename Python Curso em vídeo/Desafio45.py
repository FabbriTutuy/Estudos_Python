import random
import time

print('Jogo JOKENPO :D')

itens = ( 'Pedra','Papel','Tesoura')
computador = random.randint(0, 2)

#OPCÇOES

print('=-'*20)
print('''SUAS OPCÇÕES :
[0] Pedra 
[1] Papel 
[2] Tesoura
''')
#JOGADOR

jogador = int(input('Qual sua Jogada ? '))

#JONKENPO

print('=-'*20)

print('JO')
time.sleep(1.1)
print('KEN')
time.sleep(1.1)
print('PO')

#RESULTADOS

print('=-'*20)
print(f'O computador jogou : {itens[computador]}')
print(f'Você jogou : {itens[jogador]}')
if computador == 0 :
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCEU')
    elif jogador == 2:
        print('COMPUTADOR VENCEU')
elif computador == 1 :
    if jogador == 0:
        print('COMPUTADOR VENCEU')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCEU')
elif computador == 2 :
    if jogador == 0 :
        print('JOGADOR VENCEU')
    elif jogador == 1:
        print('COMPUTADOR VENCEU')
    elif jogador == 2:
        print('EMPATE')
print('=-'*20)
