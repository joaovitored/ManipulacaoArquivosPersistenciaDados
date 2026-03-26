# Crie um progama que leia um arquvo CSV de dados (ex: alunos e notas), processe as informações e salve um relatório em formato JSON

import csv
import json

# Usuando o básico nós lemos o arquivo csv
with open('CSValunoNotas.csv', 'r', newline='', encoding='utf-8') as arquivo_csv:
    dados_csv = csv.reader(arquivo_csv)
    for linha in dados_csv:
        print(linha)

''' 
    Usando list ele guarda os dados em uma lista organizada 
    O csv.DictReader lê a primeira linha e interpreta como categoria transformando as proximas em dicionário
'''
with open('CSValunoNotas.csv', 'r', newline='', encoding='utf-8') as arquivo_csv:
    dados_csv = list(csv.DictReader(arquivo_csv))

# Aqui usamos o dump do json para criar um relarório onde is dados_csv são jogados em um arquivo JSON
with open('relatorioAlunoNotas.json', 'w', encoding='utf-8') as arquivo_json:
    json.dump(dados_csv, arquivo_json, indent=4, ensure_ascii=False)