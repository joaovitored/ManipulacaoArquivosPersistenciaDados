#lista dos modos:
'''

 o "w" cria um novo arquivo ou sobreescreve o existente

with open("exemplo.txt", "w", encoding="utf-8") as arquivo:
    arquivo.writelines(["\nOlá,mundo!\n"])
    arquivo.write("Esta é uma nova linha.")
'''
import csv

''' 
o "a" significa anexo, ela é adicionada no final do texto

with open("exemplo.txt", "a", encoding="utf-8") as arquivo:
    arquivo.writelines(["\nOlá,mundo!\n"])
    arquivo.write("Esta é uma nova linha.")
'''


'''
o "r" significa read, ele faz a leitura do arquivo

with open("exemplo.txt", "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)
    
'''

'''
o "r+" signifca read + write, ou seja, faz a leitura e adiciona e escrita

with open("exemplo.txt", "r+", encoding="utf-8") as arquivo:
    texto = arquivo.read()
    arquivo.write("Nova informação")

'''

'''
ela vai ler os dados binários de uma imagem. Não aparece imagem, somente o código binario

with open("image.jpg", "rb") as f:
    dados_binarios = f.read()

print(dados_binarios)
'''

'''
o wb escreve somente dados binários

dados_binarios = bytes([0x48, 0x65, 0x6C, 0x6C, 0x6F])  # "Hello" em ASCII
with open("dados.bin", "wb") as arquivo:
    arquivo.write(dados_binarios)

'''


