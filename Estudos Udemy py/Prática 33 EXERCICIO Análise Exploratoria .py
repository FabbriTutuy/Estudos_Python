import matplotlib.pyplot as plt 
import pandas as pd

df = pd.read_csv("vendas_aula33.csv")
media_vendas = df["vendas"].mean()
pior_venda = df["vendas"].min()
pior_vendedor = pior_venda = df.loc[df["vendas"] == pior_venda, "nome"].values[0]
maior_venda = df["vendas"].max()
melhor_vendedor = df.loc[df["vendas"] == maior_venda, "nome"].values[0]
media_idade = df["idade"].mean() 


vendas = int(input("Deseja ver a tabela de vendas? 1 - Sim / 2 - Não "))
if vendas == 1:
    print(df)


inicio = input("Aperte Enter para da inicio a análise...")
print(f"A média de idade dos vendedores são : {media_idade} ")
print(f"A média de vendas é de {media_vendas} ")
print(f"O vendedor que que destacou foi {melhor_vendedor} ")
print(f"A maior venda foi de {maior_venda} ")
print(f"O vendedor com a menor venda foi {pior_vendedor} ")
print("Fique atento as análises e tome decisões estratégicas para melhorar as vendas!")

# MOSTRAR GRÁFICO DE BARRAS DAS VENDAS

histograma = int(input("Deseja ver o gráfico de barras das vendas? 1 - Sim / 2 - Não "))
if histograma == 1:
    df.plot.bar(x="nome", y="vendas", title="Vendas por Vendedor")
    plt.show()

else: 
    print("Obrigado por utilizar o sistema de análise de vendas!")

