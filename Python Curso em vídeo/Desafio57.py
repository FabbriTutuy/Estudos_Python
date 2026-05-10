print('=-=-=-=-=-=-= Validação de Dados =-=-=-=-=-=-=')
s = str(input('Qual o seu sexo? [M/F] ')).strip().upper()[0]
while s not in 'MmFf' :
    s = str(input('Seu sexo está incorreto . Digite novamente ')).strip().upper()[0]
print('Seu sexo foi informado : {}'.format(s))
