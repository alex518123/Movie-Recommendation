import pandas as pd


def carregar_dados(movies_path, ratings_path, tags_path):
    # Carregar os dados dos filmes
    movies = pd.read_csv(movies_path)
    print(movies.shape)
    print(movies.head())

    # Carregar os dados das tags
    tags = pd.read_csv(tags_path)
    print(tags.shape)
    print(tags.head())

    # Carregar os dados das avaliações
    ratings = pd.read_csv(ratings_path)
    print(ratings.shape)
    print(ratings.head())

    return movies, tags, ratings


def contar_generos(movies):
    # Função para contar a ocorrência de cada gênero
    generos = movies['genres'].str.split('|').explode().value_counts()
    return generos
