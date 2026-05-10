print('=-=-=-=-={ Banco CEV }=-=-=-=-=')
saque = int(input('Qual valor deseja sacar: '))
n50 = n20 = n10 = n1 = 0
tdc = 0 
while True:
    if saque >= 50:
        saque -= 50
        n50 +=1
        tdc += 1
    elif saque >= 20:
        saque -= 20
        n20 += 1
        tdc += 1
    elif saque >= 10:
        saque -= 10
        n10 += 1
        tdc += 1
    elif saque >= 1:
        saque -= 1
        n1 += 1
        tdc += 1
    else:
        break
print(f'''Foram sacados {tdc} notas sendo:
{n50} Notas de R$50
{n20} Notas de R$20
{n10} Notas de R$10
{n1} Notas de R$1''')