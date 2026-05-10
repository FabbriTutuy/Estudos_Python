num = int(input('Digite um número inteiro '))
print('-='*20)
print('''Escolha uma das base para conversão 
[1] Binario
[2] Octal
[3] Hexadecimal''')
print ('-='*20)
x = int(input('Qual será sua escolha? '))
b = bin(num)
o = oct(num)
h = hex(num)
if x == 1:
    print(f'Em Binario fica {b}')
elif x == 2 :
    print(f'Em Octal fica {o}')
elif x == 3 :
    print(f'Em Hexadecimal fica {h}')
