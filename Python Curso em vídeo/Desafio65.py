r = 0
n = 0
media = 0 
cont = 0
maior = 0
menor = 0
while r  !='n':
    n = int(input('Escolha um número inteiro '))
    r = str(input('Quer continuar [s/n]').strip().lower())
    media += n
    cont += 1
    if n > maior:
        maior = n
    elif n < maior > menor:
        menor = n
print(f' A média foi {media/cont} o maior sendo {maior} e o menor sendo {menor}')
print('Volte sempre!!!')
