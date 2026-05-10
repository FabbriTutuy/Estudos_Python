
def controle_terreno():

    print("----------------------")
    print(" CONTROLE DE TERRENOS ")
    print("----------------------")

    largura = float(input("LARGURA (m): "))
    comprimento = float(input("COMPRIMENTO (m): "))
    
    print(f"A área de um terreno{largura}x{comprimento} é {largura*comprimento}m²")

controle_terreno()