import random 
a1 = str(input('Qual é o Nome do primeiro aluno? '))
a2 = str(input('Qual é o nome do segundo aluno? '))
a3 = str(input('Qual é o nome do terceiro aluno? '))
a4 = str(input('Qual é o nome do quarto aluno? '))
x = [a1, a2, a3, a4]
random.shuffle(x)
print('A ordem é da Apresentação será')
print(x)