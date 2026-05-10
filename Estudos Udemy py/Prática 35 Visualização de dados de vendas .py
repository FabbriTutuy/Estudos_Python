import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [2,4,6,8,10]

plt.scatter(x,y , color="red" , marker="o")

plt.title("Analise de X e Y em dispersão - Listas")
plt.xlabel("Categorias")
plt.ylabel("Valores")

plt.show()