import pandas as pd
import matplotlib.pyplot as plt

data_frame = pd.read_csv("Minha_Planilha_Aula_31.csv")

data_frame = data_frame.drop_duplicates()

data_frame["Cidade"].hist()
plt.show()
