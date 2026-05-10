from rich import print
from rich import inspect


class ContaBancaria:
    
    """
    Cria uma conta bancaria e permite fazer saques e depositos
    """

    def __init__(self , id , nome , saldo = 0):
        self.id = id
        self.titular = nome
        self.saldo = saldo
        print(f"Conta {self.id} criada com sucesso. Saldo atual de R${self.saldo:,.2f}")


    def __str__(self):
        return f"A conta {self.id} de {self.titular} tem R${self.saldo:,.2f}"


    def Depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de valor R${valor:,.2f} autorizado na conta {self.id}")

    
    def Sacar(self, valor):

        if valor > self.saldo:
            print(f"Saque NEGADO de R${valor:,.2f} na conta {self.id}: Saldo Insuficiente")

        else:
            self.saldo -= valor
            print(f"Saque de valor R${valor:,.2f} autorizado na conta {self.id}")

c = ContaBancaria(id=111 , nome="Maria" , saldo=900)
inspect(c)
