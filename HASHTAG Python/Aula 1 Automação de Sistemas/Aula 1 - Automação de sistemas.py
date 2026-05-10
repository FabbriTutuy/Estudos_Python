import pyautogui
from time import sleep 
import pandas as pd

# CODGIGO D AAULA DE HOJE = usepython
# CODGIGO D AAULA DE HOJE = usepython

# pyautogui.click --> clica
# pyautogui.write -->  escreva um texto
# pyautogui.press --> aperta uma tecla
# pyautogui.hotkkey -> aperta um atalho (hotkey)

pyautogui.PAUSE = 0.8
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

# ENTRAR NO SITE DA EMPRESA
pyautogui.press("win")
pyautogui.write("edge")
pyautogui.press("enter")
sleep(2)

# ENTAR NO LINK
pyautogui.write(link)
pyautogui.press("enter")
sleep(2)

# FAZER CADASTRO NO SITE
pyautogui.click(x=677, y=366)
pyautogui.write("mestredosmagos@gmail.com")
pyautogui.press("tab")
pyautogui.write("minha_senha_:)")
pyautogui.press("tab")
pyautogui.press("enter")

tabela = pd.read_csv("produtos.csv")

# CADASTAR OS PRODUTOS
for linha in tabela.index:

    #codigo
    pyautogui.click(x=683, y=252)
    codigo = str(tabela.loc[linha,"codigo"])
    pyautogui.write(codigo)
    pyautogui.press("tab")

    #marca
    marca = str(tabela.loc[linha,"marca"])
    pyautogui.write(marca)
    pyautogui.press("tab")

    #tipo
    tipo = str(tabela.loc[linha,"tipo"])
    pyautogui.write(tipo)
    pyautogui.press("tab")

    #categoria
    categoria = str(tabela.loc[linha,"categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")

    #preço unitario
    preco_unitario = str(tabela.loc[linha,"preco_unitario"])
    pyautogui.write(preco_unitario)
    pyautogui.press("tab")

    #custo
    custo = str(tabela.loc[linha,"custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")

    #OBS
    obs = str(tabela.loc[linha,"obs"])
    if obs != "nan":

        pyautogui.write(obs)

    #ENVIANDO PRODUTO
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(5000)
    