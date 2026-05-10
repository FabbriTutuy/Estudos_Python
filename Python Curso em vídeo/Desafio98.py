from time import sleep

def contagem(inicio,fim,passo):
    
    if passo < 0:
        passo *= -1

    if passo == 0:
        passo = 1

    print(f"Contagem que vai de {inicio} até {fim} de {passo} em {passo}:")
    sleep(2)

    if inicio < fim: 

        cont = inicio
        while cont <= fim:

            print(cont,end=" ",flush=True)
            sleep(0.4)
            cont+=passo

        print("FIM!")
    
    else:

        cont = inicio
        while cont >= fim:

            print(cont,end=" ", flush=True)
            sleep(0.4)
            cont-=passo

        print("FIM!")
        

contagem(10,25,1)
contagem(10,0,2)

print("Agora é sua vez de personalizar a contagem!")
ini = int(input("Inicio: "))
fi = int(input("Fim:    "))
pas = int(input("Passo:  "))

contagem(ini,fi,pas)

