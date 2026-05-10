
#__str__ and __repr__

class veiculo:
    def __init__(self, cor , modelo , ano, tipo):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.tipo = tipo 
    
    def __str__(self):
        return f"{self.modelo} - ({self.ano}), {self.cor} - {self.tipo}"
        
    def __repr__(self):
        return f"Carro (cor = '{self.cor}' , Modelo = '{self.modelo}', ano = {self.ano}, tipo = {self.tipo})"

    def buzinar(self):
        print("Biiii")

    def acelerar(self):
        print("Acelerando...")
    
    def freiar(self):
        print("Freiando...")

    def luz(self):
        print("Acender as luzes...")


class carro(veiculo):
    def __init__(self, cor, modelo, ano):
        super().__init__(cor, modelo, ano, tipo="Carro")

    def buzinar(self):
        print("Biibii")

class moto(veiculo):
    def __init__(self, cor, modelo, ano):
        super().__init__(cor, modelo, ano, tipo ="Moto")
    
    def buzinar(self):
        print("Buubi")

class caminhao(veiculo):
    def __init__(self, cor, modelo, ano):
        super().__init__(cor, modelo, ano, tipo="Caminhão")

class trem(veiculo):
    def __init__(self, cor, modelo, ano):
        super().__init__(cor, modelo, ano, tipo="Trem")

minha_moto = moto("Preto", "Kawasaki", "2023")
print(minha_moto.buzinar())
print(minha_moto)
print(repr(minha_moto))