import random

print('=-'*15)
print('VAMO JOGAR IMPAR E PAR : ')
print('=-'*15)
jo = j = v = r = c = 0
PERDEU = False
while True:
    r = int(random.randint(0 , 10))
    j = int(input('Qual número: '))
    jo = str(input('Impar ou Par [I/P] ').upper())
    t = r + j
    v+=1 
    print('=-'*20)
    print(f'O computador jogou {r} e você jogou {j} o total deu {t}')
    if jo == 'P':
        if t %2 == 1 :
            print('O computador ganhou !!!')
            print('=-'*20)
            PERDEU
        elif t %2 == 0:
            print('O jogador venceu !!!')
            print('=-'*20)
            c+=1
    elif jo == 'I':
        if t %2 == 1 :
            print('O jogador venceu !!!')
            print('=-'*20)
            c+=1
        else:
            print('O computador venceu !!!')
            print('=-'*20)
            PERDEU
print(f'Você ganhou {c} consecutivas :D')
print('=-'*20)
