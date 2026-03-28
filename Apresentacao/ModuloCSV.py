import csv

print('\n-------- CSV.WRITER --------\n')

cabecalho = ['produto', 'preco', 'quantidade']
linhas = [
    ['Teclado Mecânico', 250.50, 15],
    ['Mouse Gamer', 120.00, 30],
    ['Monitor 24pol', 899.00, 10]]

with open('produtos.csv', 'w', newline='', encoding='utf-8') as arquivo: # Importante: newline='' evita linhas em branco extras no Windows
    escritor = csv.writer(arquivo)

    escritor.writerow(cabecalho) # Escrevendo o cabeçalho (uma única linha)
    escritor.writerows(linhas) # Escrevendo o restante dos dados (múltiplas linhas de uma vez)
    

print("Arquivo 'produtos.csv' gerado com sucesso!\n")

print('\n-------- CSV.READER --------\n ')

with open('produtos.csv', 'r', encoding='utf-8') as arquivo:
    leitor = csv.reader(arquivo)

    next(leitor) # Pula o cabeçalho para não processar os nomes das colunas
    
    for linha in leitor:
        nome = linha[0] # primeira coluna (Produto).
        preco = linha[1] # segunda coluna (Preço).
        estoque = linha[2] # terceira coluna (Estoque)
        print(f"Produto: {nome} | Preço: R$ {preco} | estoque: {estoque}\n")

print('\n-------- CSV.DICTREADER --------\n')

with open('produtos.csv', 'r', encoding='utf-8') as arquivo:
    leitor_dicionario = csv.DictReader(arquivo)
    
    for linha in leitor_dicionario:
        print(f"O item {linha['produto']} possui {linha['quantidade']} unidades em estoque.")
