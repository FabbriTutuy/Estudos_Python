
# dados = list()
# pessoas = [
#     ["Pedro" , 25],
#     ["Maria" , 31],
#     ["Ana" , 19],
# ]

#dados.append("Pedro")
#dados.append(25)

#pessoas.append(dados[:]) -> COPIA A LISTA "DADOS" INTEIRA E JOGA DENTRO DE UMA UNICA VARIAVEL 

#print(dados) 
#print(pessoas[1]) -> ["Maria" , 31]
#print(pessoas[0][0]) -> "Pedro"
#print(pessoas[1][1]) -> 31

# galera = [
#     ["João" , 21] ,
#     ["Maria" , 12] ,
#     ["Mariana" , 18]
# ]

# for p in galera:
#     print(p)

# for p in galera:
#     print(f"O {p[0]} tem {p[1]} anos")

galera = list()
dado = list()

for c in range(0,3):
    dado.append(str(input("Nome: ")))
    dado.append(int(input("Idade: ")))
    galera.append(dado[:])
    dado.clear()

for pessoa in galera:
    if pessoa[1] >= 18:
        print(f"A/O {pessoa[0]} é maior de idade")
    
    else:
        print(f"A/O {pessoa[0]} é menor de idade")