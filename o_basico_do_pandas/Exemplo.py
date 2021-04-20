# Scalar = 45
# Vetor = [1, 1, 2, 2]
# Matriz = [[1, 2], [3, 4]]

import pandas as pd

# Cria um data Frame:
# matriz = [['Carlos', 25], ['Rogério', 14], ['Carlos', 18]]
# df = pd.DataFrame(matriz, columns=["nome", "idade"])

# print(df)
# print(df.set_index("nome"))
# print(df["nome"])
# print(df["nome"][0])
# print(df[df["nome"] == "Carlos"])

# CSV:
df = pd.read_csv("teste.csv")
# print(df)         # Imprime as colunas e valores;
# print(df.dtypes)    # Retorna os tipo de dados de cada campo;
# print(df.columns)    # Retorna o indice das colunas;
# print(df.values)    # Retorna uma lista com os valores;

# Salva em um aquivo CSV:
# axis=0 indica que está se referindo a uma linha
# axis=1 indica que está se referindo a uma coluna
# df = df.drop("cpf", axis=1)
# df.to_csv("teste.csv", index=False)

# DataFrame to Json:
df = df.to_json(orient="records")   # orient="records" monta exatamente como tem que mandar pro MongoDB
print(df)
