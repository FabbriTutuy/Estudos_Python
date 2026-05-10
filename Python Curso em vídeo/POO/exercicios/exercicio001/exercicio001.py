
# Declaração de Classe

class Gafanhoto:

    def __init__(self): #METODO CONSTRUTOR
        # Atributos de Instância
        self.nome = ''
        self.idade = 0
    

    # Métodos de Instância

    def Aniversario(self):
        self.idade = self.idade +1


    def Mensagem(self):
        return f'{self.nome} é gafanhoto e tem {self.idade} anos de idade'


# Declaração de Objetos

g1 = Gafanhoto()
g1.nome = 'Matheus'
g1.idade = 21
print(g1.Mensagem())

g2 = Gafanhoto()
g2.nome = 'Luara'
g2.idade = 17
g2.Aniversario()
print(g2.Mensagem())
