from time import sleep 

cores = (
    "\033[m" ,         # 0 - Sem cores
    "\033[0;30;41m",   # 1 - Vermelho
    "\033[0;30;42m",   # 2 - Verde
    "\033[0;30;43m",   # 3 - Amarelo
    "\033[0;30;44m",   # 4 - Azul
    "\033[0;30;45m",   # 5 - Roxo
    "\033[7;30m"       # 6 - Branco
)

def tamanho(msg,cor=0):
    
    frase = len(msg) +4
    
    print(cores[cor] , end="")

    print("-"*frase )
    print(f"  {msg}")
    print("-"*frase )

    print(cores[0], end="")
    

def funcionalidade(msg):

    tamanho(f"Acessando o manual do '{msg}'",cor=6)
    sleep(1)
    help(msg)


while True:
    
    tamanho("Sistema de PyHELP",cor=2)

    sleep(1)
    
    qual =  str(input("Qual funcionalidade deseja saber [SAIR] [q] - para pular a funcionalidade: ")).strip()
    
    if qual == "sair":
        break
    
    else:
        funcionalidade(qual)


tamanho("-- VOLTE SEMPRE --",cor=5)
