from models.LeitorXLS import LeitorXLS

leitor = LeitorXLS('storage/xls/lista_compras.xlsx')
leitor.tratarDados()
leitor.salvarDados('storage/csv/lista_compras.csv')

# dados = pd.read_excel('lista.xlsx')

# df_pares = dados[dados.index % 2 == 0].reset_index(drop=True).copy()
# df_impares = dados[dados.index % 2 != 0].reset_index(drop=True).copy()
# df_pares['Valor_Linha_Impar'] = df_impares['Produto']
# text = "Qtde.:0,542UN: KGVl. Unit.: 17,98"
# padraoQtd = r'([\d,]+)'
# padraoUn = r'UN\s*:\s*(.*?)\s*Vl\.'
# padraoVlunit = r'([\d,]+)$'
# resultadoVlunit = re.findall(padraoVlunit,text)

# print(resultadoVlunit)

# df_pares['Quantidade'] = df_pares['Valor_Linha_Impar'].str.extract(padraoQtd)
# df_pares['Unidade'] = df_pares['Valor_Linha_Impar'].str.extract(padraoUn)
# df_pares['Valor Unitário'] = df_pares['Valor_Linha_Impar'].str.extract(padraoVlunit)
# df_pares['Quantidade'] = df_pares['Quantidade'].str.replace(',' , '.', regex=False).astype(float)
# df_pares['Valor Unitário'] = df_pares['Valor Unitário'].str.replace(',' , '.', regex=False).astype(float)
     
# dfCompras = df_pares
     
# dfCompras = dfCompras.drop(columns='Valor_Linha_Impar')

# dfCompras['Valor Total'] = dfCompras['Valor Unitário'] * dfCompras['Quantidade']

# dfCompras.columns.tolist()

# novaordem = ['Produto', 'Quantidade', 'Unidade', 'Valor Unitário' , 'Valor Total' ,'Data das Compras' , 'Nome do mercado','Chave NFCe']
     
# dfCompras = dfCompras[novaordem]

# dfCompras['Unidade'] = dfCompras['Unidade'].astype('category')
# dfCompras['Nome do mercado'] = dfCompras['Nome do mercado'].astype('category')
# dfCompras['Chave NFCe'] = dfCompras['Chave NFCe'].astype('category')

# print(dfCompras.tail(10))
     
