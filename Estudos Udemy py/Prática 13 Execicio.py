
try:
    lista = [1, 2, 3, 4, 5]
    lista_quad = [numero ** 2 for numero in lista]
    par = [n for n in lista_quad if n % 2 == 0]
    impar = [n for n in lista_quad if n % 2 == 1]

    print(f"a sua lista de números é {lista} ")
    print(f"O quadrado desses números são: {lista_quad}")
    print(f"O par dos números são: {par}")
    print(f"Os ímpares desses numeros são: {impar}")
except Exception as error:
    print(f"Seu erro foi: {error}")
finally:
    print("Obrigado")
