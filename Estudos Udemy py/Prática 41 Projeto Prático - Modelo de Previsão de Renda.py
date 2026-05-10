import sklearn as sk
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

# Carregar dados
df = pd.read_csv("dados_venda_pratica41.csv")

print("[!] Previsão de Renda [!]")
print("Ao realizar um investimento em marketing, gostariam de saber qual seria a estimativa para o número de vendas retornado.")
print("O modelo de previsão já está funcionando! Gostaria de ver os resultados?")

escolha = 0

while True:

    escolha = int(input("""[1] Visualizar gráfico de resultados
[2] Realizar teste de previsão
[3] Sair
Escolha uma opção: """))

    if escolha == 1:
        # Preparar dados para o modelo
        X = df[["vendas"]].values  # Variável independente (vendas)
        y = df[["investimento"]].values   # Variável dependente (renda)
        
        # Criar e treinar o modelo
        modelo = LinearRegression()
        modelo.fit(X, y)
        
        # Gerar previsões
        y_pred = modelo.predict(X)
        
        # Plotar gráfico
        plt.figure(figsize=(10, 6))
        plt.scatter(X, y, color='blue', label='Dados reais')
        plt.plot(X, y_pred, color='red', linewidth=2, label='Linha de tendência')
        plt.xlabel('Vendas')
        plt.ylabel('Renda')
        plt.title('Previsão de Renda com Base em Vendas')
        plt.legend()
        plt.grid()
        plt.show()
        
        print(f"Coeficiente (inclinação): {modelo.coef_[0][0]:.2f}")
        print(f"Intercepto: {modelo.intercept_[0]:.2f}")
        
    
    elif escolha == 2:
        # Preparar dados
        X = df[["vendas"]].values
        y = df[["investimento"]].values
        
        # Treinar modelo
        modelo = LinearRegression()
        modelo.fit(X, y)
        
        # Fazer previsão
        venda_teste = float(input("Digite o valor de vendas para fazer a previsão: "))
        previsao = modelo.predict([[venda_teste]])
        
        print(f"Com {venda_teste} em vendas, a renda prevista é de: {previsao[0][0]:.2f}")
        
    
    elif escolha == 3:
        print("Saindo...")
        break
    
    else:
        print("Opção inválida!")
        print("Tente novamente. ")

print("Obrigado por usar o sistema de previsão de renda!")