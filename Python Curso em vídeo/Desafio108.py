from Aula_22_pacotes import ex107 , ex108 

preco = float(input("Digite o preço: "))
print(f"A metade de {ex108.formatacao(preco)} é {ex108.formatacao(ex107.metade(preco))}")
print(f"O dobro de {ex108.formatacao(preco)} é {ex108.formatacao(ex107.dobro(preco))}")
print(f"Aumentando 10%, temos {ex108.formatacao(ex107.aumento(preco,10))}")
print(f"Reduzindo 13%, temos {ex108.formatacao(ex107.reduzindo(preco,13))}")


