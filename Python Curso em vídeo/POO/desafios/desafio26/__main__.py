from funcionario import *
from rich import inspect

def main():

    f1 = Horista("Arthur",25,300)
    f2 = Mensalista("Gabriela Martins",7680)
    f1.calc_sal()
    f1.analisar_sal()
    f2.calc_sal()
    f2.analisar_sal()

if __name__ == "__main__":
    main()