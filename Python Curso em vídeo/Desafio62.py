print('=-=-=-=-= Gerador de PA v2.0 =-=-=-=-=')
a = int(input('Primeiro termo da PA: ').strip())
b = int(input('Razão da PA: ').strip())
termo = a
c = a
total = 0 
mais = 10 
while mais != 0:
    total = total + mais 
    while c <= total:
        print(f'{termo} -> ', end = '')
        termo+=b
        c += 1
    print('Pausa...')
    mais = int(input('Qunatos termos você que adicionar? '))
print('Fim :D')