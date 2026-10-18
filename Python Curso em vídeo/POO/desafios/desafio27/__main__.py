from personagem import *
from rich import inspect

def main():

    p1 = Mago("Gandalf",1500)
    p2 = Guerreiro("Myaser",3300)
    
    p1.atacar(p2,230)
    #p2.atacar(p2,145)

    p2.status_personagem()

    #p1.curar()
    #p2.curar()

    #inspect(p1,methods=True)

if __name__ == "__main__":
    main()