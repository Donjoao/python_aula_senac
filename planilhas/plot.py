import numpy as np
import pandas as pd
from openpyxl import Workbook

wb = Workbook()
ws = wb.active

planilha1 = '/content/vendas1.xlsx'
planilha2 = '/content/vendas2.xlsx'
planilha3 = '/content/vendas3.xlsx'

plan1 = pd.read_excel(planilha1)
plan2 = pd.read_excel(planilha2)
plan3 = pd.read_excel(planilha3)

#print(plan1)

juntandoplanilhas = pd.concat([plan1,plan2,plan3]) #concatenando as listas.

print(juntandoplanilhas)
print(' ')

#print(juntandoplanilhas["Produtos"]) #Chamando pela Key da coluna de produtos

juntandoplanilhas['Total Venda'] = juntandoplanilhas['Preço'] * juntandoplanilhas['Unidades'] #Criando a coluna "Total Venda" e seu valor é acolua de preço vezes a coluna

total_vendas_por_vendedor = juntandoplanilhas.groupby('Vendedor')['Total Venda'].sum()

print(juntandoplanilhas)
print(' ')
print(  total_vendas_por_vendedor)
print(' ')

print(total_vendas_por_vendedor.plot(kind='bar'))
wb.save('planilha_final.xlsx')