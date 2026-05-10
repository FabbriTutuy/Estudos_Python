from sklearn.datasets import fetch_california_housing
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns    # pip install seaborn
import numpy as np

# Carregar dataset como DataFrame
data = fetch_california_housing(as_frame=True)
df = data.frame

# Calcular matriz de correlação
corr = df.corr()

# Opcional: focar só em algumas colunas
# cols = ["MedInc", "HouseAge", "AveRooms", "AveBedrms", "Population", "AveOccup", "Latitude", "Longitude", "MedHouseVal"]
# corr = df[cols].corr()

# Gerar máscara para metade superior (opcional, para deixar o mapa mais limpo)
mask = np.triu(np.ones_like(corr, dtype=bool))

# Plot
plt.figure(figsize=(12, 9))
sns.heatmap(
    corr,
    mask=None,            # oculta metade superior
    cmap="coolwarm",      # paleta de cores
    annot=True,           # escreve os valores dentro das células
    fmt=".2f",            # formato dos números
    linewidths=0.5,       # linhas entre células
    vmax=1, vmin=-1,      # escala dos valores
    cbar_kws={"shrink": 0.75}
)
plt.title("Matriz de Correlação - California Housing")
plt.tight_layout()
plt.show()
# plt.savefig("heatmap_correlacao.png", dpi=150)  # salvar em arquivo (opcional)