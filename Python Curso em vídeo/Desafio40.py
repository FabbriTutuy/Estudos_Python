n1 = float(input('Qual foi sua primeira nota? '))
n2 = float(input('Qual foi sua segunda nota? '))
x = (n1+n2)/2
if x < 5 :
    print('Você foi reprovado ')
elif 7> x >=5 :
    print('Você ficará de recuperação ')
else :
    print('Parabens você foi aprovado ')
