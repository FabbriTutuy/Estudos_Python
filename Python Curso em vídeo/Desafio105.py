
def boletim(*notas,sit=False):

    """
    Docstring para boletim
    
    :param notas: NOTAS DE ALUNO
    :param sit: SITUAÇÃO DO ALUNO
    """
    
    listas = list()
    dicionario = dict()
    media = 0

    for n in notas:
        listas.append(n)

    dicionario["Total"] = len(listas)

    for i in listas:

        media += i
        dicionario["Média"] = media/len(listas)

        if i == max(listas):
            dicionario["Maior"] = i

        elif i == min(listas):
            dicionario["Menor"] = i

    if sit:
        
        if media >= 7:
            dicionario["Situação"] = "APROVADO"

        elif media <= 6:
            dicionario["Situação"] = "REPROVADO"

        else:
            dicionario["Situação"] = "RECUPERAÇÃO"


    return dicionario


resp = boletim(2,4,5,6,sit=True)
print(resp)

