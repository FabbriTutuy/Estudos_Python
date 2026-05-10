
try:
    a = int(input("Digite um número inteiro: "))
except Exception as e:
    print(e)
else:
    print("Seu código não tem problemas")
finally:
    print("Obrigado :)")