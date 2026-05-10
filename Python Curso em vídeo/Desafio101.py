from datetime import date

def voto(idade):
    
    ano = date.today()
    idade = ano.year - nascimento
    print(f"Quem tem {idade} anos") 

    if idade >= 60:
        print("NÃO É OBRIGATÓRIO VOTAR")

    elif idade >=18:
        print("É OBRIGATÓRIO VOTAR")

    else:
        print("NÃO PODE VOTAR")


nascimento = int(input("Digite o ano que você nasceu: "))

voto(nascimento)