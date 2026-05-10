
# def mostrarlinha():
#     print("-"*30)


# mostrarlinha()

# def mensagem(msg):
#     print('-'*20)
#     print(msg)
#     print("-"*20)

# mensagem("SISTEMA DE ALUNOS")

# def soma(a,b):
#     print(f"O A = {a} e B = {b}")
#     print(f"A soma de A + B = {a+b}")

# soma(b=8,a=9)
# soma(a=4,b=9)
# soma(7,4)

# def contador(*num): # * --> ESSE SIMBOLO SIGNIFICA QUE O USUARIO VAI PASSAR VARIOS NUMEROS SEM TER UM FIXO
#     for v in num:
#         print(v,end=" ")
#     print("FIM!")

# contador(2,3,4,6,8,8)
# contador(2,6,8,0)
# contador(1,6,9)

valores = [1,3,5,7,9]

def dobra(lst):
    pos = 0
    while pos<len(lst):
        lst[pos] *= 2
        pos+=1

print(valores)
dobra(valores)
print(valores)        