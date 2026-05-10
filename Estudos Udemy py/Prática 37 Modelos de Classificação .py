import pandas as pd
import sklearn 
df = pd.read_csv("base.csv")

print(df)

x = df[["custo_produto" , "custo_frete" , "preco_venda" , "lucro"]]
y = df["retorno"]

x_train , x_test , y_train , y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.2 ,  random_state=42)

scaler = sklearn.preprocessing.StandardScaler()
x_train = scaler.transform(x_test)
x_test = scaler.transfrom(x_train)

knn = sklearn.neighbors.KNeighborsClassifier(n_neighborns=5)
knn.fit(x_train , x_test)
y_pred = knn.predict(x_test)

print("KNN")
print("Acurácia dos testes:", sklearn.metrics.classification_report(y_test, y_pred))

log = sklearn.linear_model.LogisticRegression()
log.fit(x_train , x_test)
y_pred_log = log.predict(x_test)


print("Regressão Logistica")
print("Acurácia dos testes:", sklearn.metrics.classification_repot(y_test , y_pred_log))