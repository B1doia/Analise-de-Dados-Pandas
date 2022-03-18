#aqui está um estudo sobre análise de dados com a biblioteca 'pandas'

# Leituda de dados
# Adção de dados
# Exclusão de dados
# Modificação dos dados



import pandas as pd

df = pd.DataFrame(columns = ['Ano', 'Valor_vendas', 'Qtde_itens', 'Mes'])
df = df.append({'Ano': 2011, 'Valor_vendas': 135000, 'Qtde_itens': 270, 'Mes': 'Jan'}, ignore_index = True)


dados_vendas_anuais = [{'Ano': 2011, 'Valor_vendas': 119000, 'Qtde_itens': 430, 'Mes': 'Fev'},
                      {'Ano': 2011, 'Valor_vendas': 185000, 'Qtde_itens': 520, 'Mes': 'Mar'},
                      {'Ano': 2011, 'Valor_vendas': 198000, 'Qtde_itens': 550, 'Mes': 'Abr'},
                      {'Ano': 2011, 'Valor_vendas': 204000, 'Qtde_itens': 560, 'Mes': 'Mai'},
                      {'Ano': 2012, 'Valor_vendas': 235000, 'Qtde_itens': 600, 'Mes': 'Jan'},
                      {'Ano': 2012, 'Valor_vendas': 254000, 'Qtde_itens': 620, 'Mes': 'Fev'},
                      {'Ano': 2012, 'Valor_vendas': 244000, 'Qtde_itens': 605, 'Mes': 'Mar'},
                      {'Ano': 2012, 'Valor_vendas': 260000, 'Qtde_itens': 640, 'Mes': 'Abr'},
                      {'Ano': 2012, 'Valor_vendas': 268000, 'Qtde_itens': 649, 'Mes': 'Mai'}]

df = df.append(dados_vendas_anuais, ignore_index= False)
df = df.append(dados_vendas_anuais, ignore_index= True)

df.index = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's']
df.loc['t'] = [2012, 273000, 657, 'Jun']
df.iloc[19]
df.iloc[19] = [2012, 278000, 667, 'Jun']

df.groupby(['Ano']).head()
df.groupby(['Ano']).sum()

df.groupby(['Ano']).count()
df[['Ano', 'Valor_vendas', 'Qtde_itens']].groupby(['Ano']).sum()
df[['Mes', 'Valor_vendas', 'Qtde_itens']].groupby(['Mes']).sum()


df.duplicated()
df.drop_duplicates()
df.sort_values(['Ano', 'Mes'])
df.drop_duplicates(inplace=True)
df = df.append({'Ano': 2011, 'Valor_vendas': 135000, 'Qtde_itens': 270, 'Mes': 'Jan'}, ignore_index = True)

df = df.drop_duplicates()

df.drop_duplicates(inplace=True)
