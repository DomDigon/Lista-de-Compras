from models.LeitorXLS import LeitorXLS

leitor = LeitorXLS('storage/xls/lista_compras.xlsx')
leitor.tratarDados()
leitor.salvarDados('storage/csv/lista_compras.csv')