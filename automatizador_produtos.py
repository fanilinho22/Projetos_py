import csv

caminho_tabela = 'tabela_produtos.csv'

# Sistema de direcionamento do usuário para sua função
def mainloop():
    while True:
        comando = input("O que você gostaria de fazer?\n1 - Adicionar novo produto\n2 - Apagar produto existente\n3 - Ver produtos existentes\n4 - Sair\n")
        if comando == '1':
            pega_info()
            adicionar_produto(anome, apreco, aquant, _id, caminho_tabela)
        elif comando == '2':
            remove_produto(caminho_tabela)
        elif comando == '3':
            ler_tabela_produtos(caminho_tabela)
        elif comando == '4':
            break
        else:
            print("Você selecionou um argumento inválido.")

# Pega as informações do usuário para adicionar na tabela
def pega_info():
    global anome, apreco, aquant, _id

    _id = input("ID do produto em estoque: ")
    anome = input("Nome do produto: ")
    apreco = input("Preço do produto: ")
    aquant = input("Quantidade de produtos em estoque: ")

    apreco = "R$" + apreco

# Função para ler os dados da tabela de produtos
def ler_tabela_produtos(caminho_arquivo):
    with open(caminho_arquivo, 'r') as arquivo_csv:
        leitor = csv.DictReader(arquivo_csv)
        for linha in leitor:
            print(linha)

# Função para adicionar um novo produto à tabela
def adicionar_produto(nome, preco, quantidade, _id, caminho_arquivo):
    novo_produto = {'ID': _id, 'Nome': nome, 'Preco': preco, 'Quantidade': quantidade}
    with open(caminho_arquivo, 'a', newline='') as arquivo_csv:
        campos = ['ID', 'Nome', 'Preco', 'Quantidade']
        escritor = csv.DictWriter(arquivo_csv, fieldnames=campos)
        if arquivo_csv.tell() == 0:
            escritor.writeheader()
        escritor.writerow(novo_produto)

#pega o id do produto que o usuario gostaria de remover da lista 
def remove_produto(caminho_arquivo):
    escolha = input("Qual é o ID do produto que você gostaria de remover? ")
    remover_produto(caminho_arquivo, escolha)

#pega o id que o usuario passou e procura dentro da index 0 onde esta o _id, assim adicionando esse produto em uma lista para depois ser removida
def remover_produto(caminho_arquivo, escolha):
    linhas_removidas = []
    produtos_atualizados = []
    with open(caminho_arquivo, 'r') as arquivo_csv:
        leitor = csv.DictReader(arquivo_csv)
        campos = leitor.fieldnames
        produtos = list(leitor)
        for produto in produtos:
            if produto[campos[0]] == escolha:
                linhas_removidas.append(produto)
            else:
                produtos_atualizados.append(produto)

    with open(caminho_arquivo, 'w', newline='') as arquivo_csv:
        campos = ['ID', 'Nome', 'Preco', 'Quantidade']
        escritor = csv.DictWriter(arquivo_csv, fieldnames=campos)
        escritor.writeheader()
        for produto in produtos_atualizados:
            escritor.writerow(produto)


mainloop()
