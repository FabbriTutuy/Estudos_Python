
wage = float(input("Digite seu salário: "))
expenses = input("Digite uma despesa, se quiser parar digite 'sair' :")
total_expenses = 0

while True:
    valor_expenses = float(input("Digite o valor da despesa: "))
    expenses = input("Digite uma despesa, se quiser parar digite 'sair' :").lower()
    if expenses == "sair":
        break
    total_expenses += valor_expenses

print("")
print("----- RESUMO -----")
print(f"""Seu salário é R${wage}
O total de depesas deu R${total_expenses:.2f}""")

if wage < total_expenses:
    print(f"Voce ficou no negativo devendo R${abs(age - total_expenses):.2f}")
elif wage > total_expenses:
    print(f"Você ficou no positivo num total de R${wage - total_expenses:.2f}")
else: 
    print(f"FICOU NO LIMITE UM TOTAL DE R${wage - total_expenses:.2f}")
