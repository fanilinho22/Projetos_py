import csv

caminho_tabela = 'tabela_produtos.csv'

#sistema de direcionamento do usuario para sua funcao 
def usuario():
    while True:
        comando = input("O que voce gostari de fazer?\n1- Adicionar novo produto\n2- Ler tabela produtos\n3- Sair\n")
        if comando == '1':
            pega_info()
            adicionar_produto(caminho_tabela, anome, apreco, aquant)
        elif comando == '2':
            ler_tabela_produtos(caminho_tabela)
        elif comando == '3':
            break
        else:
            print("Voce selecionou o argumento errado")

#pega as informacoes do usuario para adicionar na tabela
def pega_info():
    global anome, apreco, aquant

    anome = input("Nome do produto\n")
    apreco = input("Preco do produto\n")
    aquant = input("Quantidade de produtos em estoque\n")
    
    apreco += ("R$")

# Função para ler os dados da tabela de produtos
def ler_tabela_produtos(caminho_arquivo):
    with open(caminho_arquivo, 'r') as arquivo_csv:
        leitor = csv.DictReader(arquivo_csv)
        for linha in leitor:
            print(linha)

# Função para adicionar um novo produto à tabela
def adicionar_produto(caminho_arquivo, nome, preco, quantidade):
    novo_produto = {'Nome': nome, 'Preço': preco, 'Quantidade': quantidade}
    with open(caminho_arquivo, 'a', newline='') as arquivo_csv:
        campos = ['Nome', 'Preço', 'Quantidade']
        escritor = csv.DictWriter(arquivo_csv, fieldnames=campos)
        escritor.writerow(novo_produto)
    

usuario()
