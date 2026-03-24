#Introduzir modulo json para serialização de dados

import json

# crie uma lista de dados com usuários contidos em dicionários
dadosUsuarios = [{'nome': 'Ana Maria', 'idade': 30, 'cidade': 'Recife', 'sexo': 'F'}, 
                 {'nome': 'Antonio Fagundes', 'idade': 32, 'cidade': 'Recife', 'sexo': 'M'}, 
                 {'nome': 'Larissa Tomato', 'idade': 12, 'cidade': 'Jaboatao', 'sexo': 'F'}, 
                 {'nome': 'Eduardo Berinjela', 'idade': 26, 'cidade': 'Recife', 'sexo': 'M'}]

# com json.dump() você pode criar um arquivo json, e se um arquivo com o mesmo nome já estiver 
# criado na mesma pasta ele o sobrescreve.

with open('dadosUsuarios.json', 'w') as usuarios:
    json.dump(dadosUsuarios, usuarios)


# com json.load() você lê arquivos json
with open('dadosUsuarios.json', 'r') as usuarios:
    lista = json.load(usuarios)
    print(lista)
