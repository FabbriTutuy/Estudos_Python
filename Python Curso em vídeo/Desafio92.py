from datetime import datetime

registro = dict()

#APOSENTAR LEVA 35 ANOS DE CONTRIBUIÇÃO

registro["nome"] = str(input("Digite seu nome: "))
nasc = int(input("Ano de nascimento: "))
registro["idade"] = datetime.now() - nasc
registro["CTPS"] = int(input("Carteira de trabalho (0 não tem): "))

if registro["CTPS"] != 0:
    
    registro["Contratação"] = int(input("Digite seu ano de contratação: "))
    registro["Salário"] = float(input("Salário: "))
    registro["Aposentadoria"] = registro["idade"] + (registro["Contratação"] + 35) - datetime.now().year

print("=-=-=-=-= DADOS GERAL DA CLT =-=-=-=-=   ")

for k,v in registro.items():
    print(f"{k} tem valor de {v}")

if registro["CTPS"] != 0:
    print("Não tem carteira de trabalho! ")