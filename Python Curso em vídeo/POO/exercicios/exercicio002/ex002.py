
# Declaração de Classe

class Gafanhoto:
    """
    Essa classe cria um gafanhoto que estuda python
    para criar uma nova pessoa, use 
    variavel = Gafanhoto(nome, idade)
    """
    def __init__(self, nome = 'vazio' , idade = 0): #METODO CONSTRUTOR
        # Atributos de Instância
        self.nome = nome
        self.idade = idade
    

    # Métodos de Instância

    def Aniversario(self):
        self.idade = self.idade +1
    

    def __str__(self):
        return f'{self.nome} é gafanhoto e tem {self.idade} anos de idade'
    

    def __getstate__(self):
        return f'Estado: nome = {self.nome} ; idade = {self.idade}'

# Declaração de Objetos

g1 = Gafanhoto('Matheus',28)
print(g1)

print(g1.__doc__)
print(g1.__dict__)
print(g1.__getstate__())
print(g1.__class__)