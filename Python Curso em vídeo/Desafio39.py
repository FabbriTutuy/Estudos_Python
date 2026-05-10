n = str(input('Qual é seu nome ? '))
i = int(input('Qual é sua idade? '))
c1 = 18 - i
if i < 18:
    print(f'Você ainda vai se alistar no exercito, {n}.')
    print(f'Falta ainda {c1} anos para se alistar no exercito.')
elif i == 18 :
    print(f'Você chegou na idade de se alistar no exercito, {n}.')
elif i > 18 :
    print(f'Já passou do tempo de alistamento, {n}.')
    print(f'Você passou do prazo a {c1} anos .')
