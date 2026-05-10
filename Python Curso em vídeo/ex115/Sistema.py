from lib.Interface import *
from lib.arquivo import *
from time import sleep

arq = "cursoemvideo.txt"

if not arquivoExiste(arq):
    criarArquivo(arq) 

while True:

    resposta = menu(["Ver pessoas cadastradas","Cadastrar nova Pessoa","Sair do Sistema"])

    if resposta == 1:

        # OPÇÃO DE LISTAR O CONTEUDO DE UM ARQUIVO
        LerArquivo(arq)

    elif resposta == 2:

        # OPÇÃO CADASTRAR UMA NOVA PESSSOA
        cabecalho("NOVO CADASTRO")
        nome =  str(input("Nome: "))
        idade = ReadInt("Idade: ")
        cadastrar(arq,nome,idade)

    elif resposta == 3:

        # OPÇÃO DE SAIR DO PROGRAMA
        cabecalho("Saindo do Sistema ")
        break    

    else:

        print("\033[0;31mERRO!! Digite uma opção válida!\033[m")

    sleep(1.5)


