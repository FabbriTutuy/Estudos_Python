print ('~-~-~-~-~-~ Contador de números ~-~-~-~-~-~')
n = 0
s = 0
cont = 0
while n  !=999:
    n = int(input('Digite um número de 0 a 999 sendo que 999 para o programa: '))
    s = s + n
    cont+=1
print (f'você digitou {cont - 1} vezes sem contar')
print (f'A soma de todos esses números é {s-999} exceto: 999')