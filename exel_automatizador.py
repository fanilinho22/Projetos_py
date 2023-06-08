import openpyxl as xl

listinha = ["banana", 50, 3.50]

#criar uma planilha
book = xl.Workbook()

#Criando uma pagina
book.create_sheet("frutas")
#selecionando uma pagina
frutas_page = book["frutas"]

frutas_page.append(["Frutas","Qnt","preco"])
frutas_page.append(listinha)

#salvar planilha
book.save("Planilhas de compras.xlsx")