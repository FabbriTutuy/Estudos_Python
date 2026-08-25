from rich import print , inspect
from classesex07 import Aluno , Professor , Funcionario , Pessoa

def main():
    a1 = Aluno("Arthur",18,"Engenharia da Computação", "T01")
    a1.fazer_aniversario()
    a1.fazer_matricula()
    a1.estudar()
    #inspect(a1,methods=True)

    p1 = Professor("Guanabara", 37, "Biologia","Mestrado")
    p1.fazer_aniversario()
    p1.dar_aula()
    p1.estudar()
    #inspect(p1)

    f1 = Funcionario("André",47,"Secretária","Secretaria")
    f1.fazer_aniversario()
    f1.bater_ponto()
    f1.estudar()
    inspect(f1,methods=True)

if __name__ == "__main__":
    main()