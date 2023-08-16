import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_json('dados_compra.json')

print(df.head())

print(df.isnull().sum())

total_compras = len(df)

media_gasto = df['valor_compra'].mean()
min_gasto = df['valor_compra'].min()
max_gasto = df['valor_compra'].max()

produto_mais_caro = df.loc[df['valor_compra'].idxmax()]['nome_produto']
produto_mais_barato = df.loc[df['valor_compra'].idxmin()]['nome_produto']

genero_distribuicao = df['genero'].value_counts()

valor_total_genero = df.groupby('genero')['valor_compra'].sum()

plt.figure(figsize=(10, 6))

plt.subplot(1, 2, 1)
genero_distribuicao.plot(kind='bar', color=['blue', 'pink'])
plt.title('Distribuição de Gênero')
plt.xlabel('Gênero')
plt.ylabel('Quantidade')

plt.subplot(1, 2, 2)
valor_total_genero.plot(kind='bar', color=['blue', 'pink'])
plt.title('Valor Total Gasto por Gênero')
plt.xlabel('Gênero')
plt.ylabel('Valor Total Gasto')

plt.tight_layout()
plt.show()
