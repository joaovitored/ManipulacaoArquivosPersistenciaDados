#criação do arquivo exemplo.txt e caso ele já exista, ele vai substituir o texto que já está existe
with open("exemplo.txt", "w", encoding="utf-8") as arquivo:
        criartexto = arquivo.write("Criação de texto: \nLorem ipsum dolor sit amet, consectetur adipiscing elit. \n"
         "Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua." )
        print(criartexto)

try:
#tenta achar o arquivo e ler
    with open("exemplo.txt","r", encoding="utf-8") as arquivo:
        conteudo = arquivo.read()

#caso ele não encontre o arquivo
except FileNotFoundError:
    print("O arquivo não foi encontrado")

    #só dispara a mensagem caso o arquivo tenha alguma proteção ou esteja sendo usado em algum lugar
except PermissionError as erropermissao:
    print(f"Você não possui permissão para acessar o arquivo. Erro: {erropermissao}")
else:
    print(conteudo)

#texto base
"""
Lorem Ipsum is simply dummy text of the printing and typesetting industry.
 Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,
  when an unknown printer took a galley of type and scrambled it to make a type specimen book.
  It has survived not only five centuries, but also the leap into electronic typesetting,
   remaining essentially unchanged.
   It was popularised in the 1960s with the release of Letraset sheets containing
   Lorem Ipsum passages, and more recently with desktop
publishing software like Aldus PageMaker including versions of Lorem Ipsum.

"""