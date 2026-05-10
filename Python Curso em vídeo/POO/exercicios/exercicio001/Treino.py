
class Carro:
    
    def __init__(self): # Metodo contrutor
        # Atributos Instância
        self.cor = ''
        self.ano = 0
        self.marca = ''
        self.modelo = ''

    # Metodo Instância

    def Caracteristicas(self):
        return f'Seu carro é um {self.marca} {self.modelo} de cor {self.cor} e ano {self.ano}'

    def Buzinar(self):
        return 'BIIIII'


class Moto:

    def __init__(self): # Metodo contrutor
        # Atributos Instância
        self.cor = ''
        self.ano = 0
        self.marca = ''
        self.modelo = ''

    # Metodo Instância

    def Caracteristicas(self):
        return f'Sua moto é uma {self.marca} {self.modelo} de cor {self.cor} e ano {self.ano}'

    def Buzinar(self):
        return 'BIIIIIUUU'

# CARRO

MeuCarro = Carro()
MeuCarro.cor = 'Branco'
MeuCarro.ano = 2017
MeuCarro.marca = "Nissan"
MeuCarro.modelo = "Skyline GT-R"
print(MeuCarro.Caracteristicas())
print(MeuCarro.Buzinar())

# MOTO

MinhaMoto = Moto()
MinhaMoto.cor = 'Verde'
MinhaMoto.ano = 2022
MinhaMoto.marca = 'Kasawaki'
MinhaMoto.modelo = 'Modelo mais pica'
print(MinhaMoto.Caracteristicas())
print(MinhaMoto.Buzinar())
