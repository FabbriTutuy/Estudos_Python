print('=-=-=-=-=-= Análise de dados do grupo =-=-=-=-=-=')
i = s = mn = 0
c  = qc = 0 
ia = hc = 0
while True:
    c+=1
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('    Cadastre uma pessoa    ')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    i = int(input(f'Qual idade da {c}ª pessoa : '))
    s = str(input(f'Qual o sexo da {c} pessoa  [H/M]: ').upper())
    qc = str(input('Quer continuar ? [S/N] ').upper())
    if s !='M' or 'F' :
        s = str(input(f'Qual o sexo da {c} pessoa  [H/M]: ').upper())
    if s != 'S' or 'N':
        qc = str(input('Quer continuar ? [S/N] ').upper())
    if s == 'M' and i <= 20:
        mn+=1
    if s == 'H':
        hc+=1
    else:
        break
    if i >= 18:
        ia+=1
    else:
        break
    if qc == 'S':
        i = int(input(f'Qual idade da {c}ª pessoa : '))
        s = str(input(f'Qual o sexo da {c} pessoa  [H/M]: ').upper())
        qc = str(input('Quer continuar ? [S/N] ').upper())
    else:
        break
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print(f'Tem um total de {ia} pessoas acima de 18 anos ')
print(f'Tem um total de {hc} homens cadastrados')
print(f'Existe um total de {mn} mulheres cadastradas abixo de 20 anos ')
print(f'Fim... Foram registrado um total de {c} pessoas')
print('=-=-=-=-=-=-=-=-=-=-= Fim :D =-=-=-=-=-=-=-=-=-=-')