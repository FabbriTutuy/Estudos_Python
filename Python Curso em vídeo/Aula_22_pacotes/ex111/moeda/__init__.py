
def metade(n=0,form=False):

    result = n/2 

    if form == True:

       return f"R$ {result}".replace(".",",") 
    
    else:

        return result


def dobro(n=0,form=False):

    result = n*2

    if form == True:

       return f"R$ {result}".replace(".",",") 
    
    else:
        return result


def aumento(n=0,z=0,form=False):

    result = n + (n * (z/100))

    if form == True:

       return f"R$ {result}".replace(".",",") 
    
    else:
        return result


def reduzindo(n=0,z=0,form=False):

    result = n - (n * (z/100))

    if form == True:

       return f"R$ {result}".replace(".",",") 
    
    else:
        return result


def formatacao(msg):

    return f"R$ {msg}".replace(".",",")


def resumo(valor , increase , reduce):
    
    print("-"*32)
    print(f"{"RESUMO DO VALOR":^32}")
    print("-"*32)

    print(f"Preço analisado: {formatacao(valor):>15}")
    print(f"Dobro do preço: {dobro(valor,True):>15}")
    print(f"Metade do preço: {metade(valor,True):>15}")
    print(f"{increase}% de aumento: {aumento(valor,increase,True):>15}")
    print(f"{reduce}% de redução: {reduzindo(valor,reduce,True):>15}")

    print("-"*32)

