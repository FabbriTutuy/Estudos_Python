import pandas as pd

df = pd.read_csv("Minha_Planilha_Aula_31.csv")

print(df)

df = df.drop_duplicates()

print(df)

