from Aula_22_pacotes import ex107

preco = float(input("Digite o preço: "))
print(f"A metade de {ex107.formatacao(preco)} é {ex107.metade(preco,True)}")
print(f"O dobro de {ex107.formatacao(preco)} é {ex107.dobro(preco,True)}")
print(f"Aumentando 10%, temos {ex107.aumento(preco,10,True)}")
print(f"Reduzindo 13%, temos {ex107.reduzindo(preco,13,True)}")
