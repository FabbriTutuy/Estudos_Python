# Dicionário para armazenar os dados por produto
relatorio = {}

# Abrir e ler o arquivo
with open('vendas.txt', 'r', encoding='utf-8') as arquivo:
    for linha in arquivo:
        produto, quantidade, preco_unitario = linha.strip().split(',')
        quantidade = int(quantidade)
        preco_unitario = float(preco_unitario)
        
        if produto not in relatorio:
            relatorio[produto] = {
                'quantidade_total': 0,
                'preco_unitario': preco_unitario,
                'valor_total': 0.0
            }

        relatorio[produto]['quantidade_total'] += quantidade
        relatorio[produto]['valor_total'] += quantidade * preco_unitario

# Gerar e imprimir o relatório formatado
print("===== RELATÓRIO DE VENDAS =====\n")
for produto, dados in relatorio.items():
    print(f"Produto: {produto}")
    print(f"Quantidade Vendida: {dados['quantidade_total']}")
    print(f"Preço Unitário: R$ {dados['preco_unitario']:.2f}")
    print(f"Valor Total: R$ {dados['valor_total']:.2f}")
    print("-" * 30)
