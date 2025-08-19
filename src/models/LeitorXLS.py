import pandas as pd
import re
import csv


class LeitorXLS:

    def __init__(self, caminho_arquivo):
        self.dados = pd.read_excel(caminho_arquivo)
        self.listaItens = []

    def tratarDados(self):

        lista = self.dados.iterrows()

        # Iterating over rows
        for index, row in lista:

            # print(f"{index} {row['Produto']}")

            if (index % 2 == 0):
                print(row["Produto"])
                pattern = r"(?P<produto>.*)\(Código:\s(?P<codigo>[0-9]+)\s\)"
                match = re.search(pattern, row['Produto'], re.IGNORECASE)
                produto = row['Produto']
                codigo = 0
                
                if(match):
                    produto = match.group('produto')
                    codigo = match.group('codigo')
                
                item = {}
                item['produto'] = produto
                item['codigo'] = codigo
                item['data_compra'] = row['Data das Compras'].strftime("%Y-%m-%d")
                item['mercado'] = row['Nome do mercado']
                item['chave_nfce'] = row['Chave NFCe']
            else:
                produto = row['Produto']
                pattern = r"Qtde\.:(?P<qtd>[0-9,]+)UN:\s(KGVl|GVl|LVl|PAVl|MLVl|CJVl|UNVl)\.\sUnit\.\:\s+(?P<unidade>[0-9,]+)"
                match = re.search(pattern, produto, re.IGNORECASE)
                qtd = 0
                unidade = 0
                
                if (match):
                    qtd = match.group('qtd')
                    unidade = match.group('unidade')

                item['qtd'] = qtd
                item['unidade'] = unidade
                
                self.listaItens.append(item)

    def salvarDados(self, path):
        with open(path, mode='w', newline='', encoding='utf-8') as arquivo_csv:
            # Criando um escritor de dicionários
            escritor = csv.DictWriter(
                arquivo_csv, fieldnames=self.listaItens[0].keys(), delimiter=';')

            # Escrevendo os cabeçalhos
            escritor.writeheader()

            # Escrevendo as linhas no arquivo CSV
            escritor.writerows(self.listaItens)

            print(f"Dados escritos com sucesso em {path}.")
