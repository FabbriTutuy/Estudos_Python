
class carro:
    def __init__(self, cor , modelo , ano):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano

    def buzinar(self):
        print("Biiii")

    def acelerar(self):
        print("Acelerando...")
    
    def freiar(self):
        print("Freiando...")

    def luz(self):
        print("Acender as luzes...")

meu_carro = carro("preto", "Honda Civic", "2023")

print(meu_carro.buzinar())


class pc:
    def __init__(self, ram , memoria , processador):
        self.ram = ram
        self.memoria = memoria
        self.processador = processador

    def ligar(self):
        print("Ligando....piii....piii....piii....")
        return ""

    def desligar(self):
        print("Desligandooo.....piiii....piii....")

    def leds(self):
        print("Leds acesso...")

meu_pc = pc("4GB", "564GB", "I3 1200")

print(meu_pc.processador)
print(meu_pc.ram)
print(meu_pc.ligar())