#ListaDoMercado#
print('=-=-=-=-=-=-={ Lista do Mercado }=-=-=-=-=-=-=')
nomep = 0
pdp = 0
tg = 0 
cont = 0
acm = 0
npmb = 0 
pmb = 0
while True:
    nomep = str(input('Nome = '))
    pdp = float(input('Preço = '))
    tg+=pdp
    while cont == 'S' or 'N':
        cont = str(input('Quer continuar ? [S/N] ').upper().strip())
        if cont == 'S':
            nomep = str(input('Nome = '))
            pdp = float(input('Preço = '))
        elif cont == 'N':
            break
        else:
            cont = str(input('Quer continuar ? [S/N] ').upper().strip())
    if pdp > 1000:
        mm+=1
        break
    if pdp < pmb or pmb == 0:
        pmb = pdp
        npmb = nomep
        break
    if cont == 'n' or 'não':
        break
print(f'O total de R$ gastos foram R${tg}')
print(f'O total de produtos acima de R$1000.00 foram {acm}')
print(f'O produto mais barato é {npmb}')