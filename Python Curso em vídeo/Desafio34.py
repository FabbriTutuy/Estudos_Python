s = float(input('Qual o salario do funcionario escilhido? '))
r1 = (s*10)/100+s
r2 = (s*15)/100+s
if s <=1250:
    print(f'Ele terá um aumento de 15% agora passando a ganhar R${r2} ')
else:
    print(f'Ele terá um aumento de 10% agora passando a ganhar R${r1} ')

