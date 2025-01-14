from data_loader import carregar_dados, contar_generos
from recommender import calcular_similaridade, recomendar_filmes

# Carregar os dados
movies_path = 'movies.csv'
ratings_path = 'ratings.csv'
tags_path = 'tags.csv'
movies, tags, ratings = carregar_dados(movies_path, ratings_path, tags_path)

# Contar a ocorrência de cada gênero
censo_generos = contar_generos(movies)
print("\nCenso dos Gêneros:")
print(censo_generos)

# Calcular a média das avaliações para cada filme
ratings_mean = ratings.groupby('movieId')['rating'].mean().to_dict()

# Calcular a similaridade dos filmes
cosine_sim = calcular_similaridade(movies, tags)

# Interação com o usuário
nome_filme = input("Qual filme você quer recomendações? ")
qtde_recomendacoes = int(input("Quantas recomendações você quer? "))
recomendacoes = recomendar_filmes(
    nome_filme, qtde_recomendacoes, movies, cosine_sim, ratings_mean)
print(recomendacoes)
