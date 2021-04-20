import pymongo
import pandas as pd
from bson.objectid import ObjectId

# Cria a conexão com o MangoDB:
conn = pymongo.MongoClient("mongodb://localhost:27017/")

# Lista os banco de dados que existem:
# print(conn.list_database_names())

# Seleciona um banco de dados (Se o banco não existir ele cria automaticamente):
db = conn['LIama']

# Seleciona uma Collection:
usuarios = db['usuarios']

# Insere um registro na Collection:
pessoa = dict(nome="Teste", idade=27)
usuarios.insert_one(pessoa)

# Insere vários registros na Collection:
pessoa1 = dict(nome="João", idade=33)
pessoa2 = dict(nome="Rogério", idade=42)
usuarios.insert_many([pessoa1, pessoa2])

# Exemplo de inserção de document dentro de document:
pessoa3 = dict(nome="Documentos", dados=dict(cpf="2318900893", idade=22, altura=1.8))
usuarios.insert_one(pessoa3)

# Delete:
usuarios.delete_one({"Nome": "Teste"})

# Update
filtro = dict(nome="Documentos")
novos_valores = dict(nome="Documentoooos")
usuarios.update_one(filtro, {"$set": novos_valores})

# Find
# for i in usuarios.find():
#     print(i)
# print(pd.DataFrame(usuarios.find()))

# Criando um id com 12 caracteres:
print(ObjectId(b"abcdefghojkl"))

# Criando um id com 24 caracteres:
print(ObjectId(b"607edb00432a3ec5d8d33268"))
