import seaborn as sb
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)

data = pd.DataFrame({
    "x" : np.random.rand(50) ,
    "y" : np.random.rand(50) ,
    "z" : np.random.rand(50) , 
})


corr = data.corr()

sb.set_theme(style = "whitegrid" , palette = "pastel")
sb.heatmap(corr, annot=True , cmap= "coolwarm")
plt.title("Gráfico Seaborn" , fontweight = "bold")
plt.show()