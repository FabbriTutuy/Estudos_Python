num1 = int(input('Escolha um número '))
num2 = int(input('Escolha outro número '))
num3 = int(input('Escolha mais um número '))
#Verificando Quem é o menor
menor = num1 
if num2<num1 and num2<num3:
    menor = num2
if num3<num1 and num3<num2:
    menor = num3
#Verificando Quem é o maior
maior = num1
if num2>num1 and num2>num3:
    maior = num2
if num3>num1 and num3>num2:
    maior = num3
#Resultado
print(f'O maior Número digitado é {maior} .')
print(f'O menor Número digitado foi {menor} .')
