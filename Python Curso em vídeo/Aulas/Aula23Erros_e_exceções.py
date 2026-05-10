
## --> TRATAMENTO DE ERRO <-- ##

try:
    a = int(input("Numerador: "))
    b = int(input("Denominador: "))
    r = a/b

except (ValueError, TypeError) as erro:
    print(f"Problema encontrado foi {erro.__class__}") # __class__ fala qual valor foi o erro

except ZeroDivisionError:
    print(f"Não foi possivel dividir o numero por zero")

except KeyboardInterrupt:
    print("O usuario preferio não informar os dados ")

else:
    print(f"O resultado é {r:.1f}")

finally:
    print("Volte sempre , Muito obrigado")

