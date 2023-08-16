filmes = [
    {"titulo": "O Senhor dos Anéis", "ano": 2001, "avaliacao": 8.8},
    {"titulo": "Matrix", "ano": 1999, "avaliacao": 9.3},
    {"titulo": "Interestelar", "ano": 2014, "avaliacao": 8.6}
]

avaliacoes = [filme["avaliacao"] for filme in filmes]
media_avaliacoes = sum(avaliacoes) / len(avaliacoes)

max_avaliacao = float('-inf')
filme_maior_avaliacao = None

for filme in filmes:
    if filme["avaliacao"] > max_avaliacao:
        max_avaliacao = filme["avaliacao"]
        filme_maior_avaliacao = filme["titulo"]

min_avaliacao = float('inf')
ano_filme_menor_avaliacao = None

for filme in filmes:
    if filme["avaliacao"] < min_avaliacao:
        min_avaliacao = filme["avaliacao"]
        ano_filme_menor_avaliacao = filme["ano"]

print(f"Média das avaliações dos filmes: {media_avaliacoes:.2f}")
print(f"Filme com a maior avaliação: {filme_maior_avaliacao}")
print(f"Ano de lançamento do filme com a menor avaliação: {ano_filme_menor_avaliacao}")
