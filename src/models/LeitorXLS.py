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
            
            print(f"{index} {row['Produto']}")

            if (index % 2 == 0):
                #([0-9]+)\s([a-zA-Z ]+(\s)?([0-9,]+)?(g|kg|l))
                # regex = r"([a-zA-Z ]+)(.*)\(Código: ([0-9]+)\s\)"
                item = {}
                # matches = re.finditer(regex, row['Produto'], re.MULTILINE)
                # for matchNum, match in enumerate(matches, start=1):
                #     group = match.groups()
                #     print(group)
                    # print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
                        
                    # for groupNum in range(0, len(match.groups())):
                    #     groupNum = groupNum + 1
                        
                    #     print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))
                # produto = 
                item['produto'] = row['Produto']
                item['data_compra'] = row['Data das Compras']
                item['mercado'] = row['Nome do mercado']
                item['chave_nfce'] = row['Chave NFCe']
            else:
                item['qtd'] = row['Produto']
                self.listaItens.append(item)

    def salvarDados(self, path):
        with open(path, mode='w', newline='', encoding='utf-8') as arquivo_csv:
            # Criando um escritor de dicionários
            escritor = csv.DictWriter(arquivo_csv, fieldnames=self.listaItens[0].keys(), delimiter=';')

            # Escrevendo os cabeçalhos
            escritor.writeheader()

            # Escrevendo as linhas no arquivo CSV
            escritor.writerows(self.listaItens)

            print(f"Dados escritos com sucesso em {path}.")
