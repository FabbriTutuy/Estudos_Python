from rich import print,inspect
from poligono import *

def main():
    q1 = Quadrado(20)

    print(f"Perimetro = {q1.perimetro():.1f} m")
    print(f"Area = {q1.area():.1f} m²") 


    c = Circulo(9)
    print(f"Perimetro = {c.perimetro():.1f} m")
    print(f"Área = {c.area():.1f} m²")

if __name__ == "__main__":
    main()