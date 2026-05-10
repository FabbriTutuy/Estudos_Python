import random
a1 = str(input('Qual o nome do Primeiro aluno? '))
a2 = str(input('Qual o nome do Segundo aluno? '))
a3 = str(input('Qual o nome do terceiro aluno? '))
a4 = str(input('Qual o Nome do Quarto aluno? '))
al = (a1,a2,a3,a4)
x = random.choice(al)
print (f'O aluno escolhido foi {x} ')
