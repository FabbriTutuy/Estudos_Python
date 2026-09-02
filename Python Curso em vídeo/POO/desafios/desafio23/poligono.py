from abc import abstractmethod,ABC
import math

class Poligono(ABC):

    def __init__(self,lados):
        self.qtd_lados = lados

    @abstractmethod
    def perimetro() -> float:
        """Calcula e retorna o perímetro da forma."""
        pass

    @abstractmethod
    def area() -> float:
        """Calcula e retorna a área da forma."""
        pass

 
class Quadrado(Poligono):

    def __init__(self,lado=1):
        super().__init__(4)
        self.lado = lado

    def perimetro(self):
        return 4 * self.lado

    def area(self):
        return self.lado**2

class Circulo(Poligono):

    def __init__(self,raio=1):
        super().__init__(0)
        self.raio = raio

    def perimetro(self):
        return 2 * math.pi * self.raio

    def area(self):
        return math.pi * self.raio ** 2 