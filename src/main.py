from models.LeitorXLS import LeitorXLS

# iniciando o leitor de arquivos
leitor = LeitorXLS('storage/xls/lista_compras.xlsx')

# tratando os dados
leitor.tratarDados()

# salvando o arquivo tratado
leitor.salvarDados('storage/csv/lista_compras.csv')