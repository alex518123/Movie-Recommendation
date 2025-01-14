import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter

# Carregar os dados dos filmes
movies_path = 'movies.csv'
movies = pd.read_csv(movies_path)

# Carregar os dados das tags (descrições)
tags_path = 'tags.csv'
tags = pd.read_csv(tags_path)

# Carregar os dados das avaliações
ratings_path = 'ratings.csv'
ratings = pd.read_csv(ratings_path)

# Exibição inicial dos dados
print("Movies DataFrame:")
print(movies.head())
print("\nTags DataFrame:")
print(tags.head())
print("\nRatings DataFrame:")
print(ratings.head())

# Análise básica dos dados
num_movies = movies['movieId'].nunique()
num_users = ratings['userId'].nunique()
num_tags = tags['tag'].nunique()
num_ratings = ratings.shape[0]

print(f"\nNúmero de filmes: {num_movies}")
print(f"Número de usuários: {num_users}")
print(f"Número de tags: {num_tags}")
print(f"Número de avaliações: {num_ratings}")

# Visualização da distribuição das avaliações
plt.figure(figsize=(10, 6))
sns.histplot(ratings['rating'], bins=10, kde=False)
plt.title('Distribuição das Avaliações')
plt.xlabel('Avaliação')
plt.ylabel('Contagem')
plt.show()

# Filmes mais avaliados
top_rated_movies = ratings['movieId'].value_counts().head(10)
top_rated_movies = movies[movies['movieId'].isin(top_rated_movies.index)]

plt.figure(figsize=(10, 6))
sns.barplot(y=top_rated_movies['title'],
            x=top_rated_movies['movieId'].value_counts().values)
plt.title('Top 10 Filmes Mais Avaliados')
plt.xlabel('Número de Avaliações')
plt.ylabel('Filme')
plt.show()

# Avaliações médias dos filmes
average_ratings = ratings.groupby(
    'movieId')['rating'].mean().sort_values(ascending=False).head(10)
top_average_rated_movies = movies[movies['movieId'].isin(
    average_ratings.index)]

plt.figure(figsize=(10, 6))
sns.barplot(y=top_average_rated_movies['title'], x=average_ratings.values)
plt.title('Top 10 Filmes com Melhores Avaliações Médias')
plt.xlabel('Avaliação Média')
plt.ylabel('Filme')
plt.show()

# Distribuição das tags
top_tags = tags['tag'].value_counts().head(10)

plt.figure(figsize=(10, 6))
sns.barplot(y=top_tags.index, x=top_tags.values)
plt.title('Top 10 Tags Mais Frequentes')
plt.xlabel('Contagem')
plt.ylabel('Tag')
plt.show()

# Separar os gêneros
movies['genres'] = movies['genres'].str.split('|')
movies = movies.explode('genres')

# Média das avaliações por gênero
genre_ratings = ratings.merge(movies[['movieId', 'genres']], on='movieId')
average_genre_ratings = genre_ratings.groupby(
    'genres')['rating'].mean().sort_values(ascending=False)

plt.figure(figsize=(10, 6))
sns.barplot(y=average_genre_ratings.index, x=average_genre_ratings.values)
plt.title('Média das Avaliações por Gênero')
plt.xlabel('Avaliação Média')
plt.ylabel('Gênero')
plt.show()

# Extrair o ano de lançamento dos filmes
movies['year'] = movies['title'].str.extract(r'\((\d{4})\)', expand=False)
movies['year'] = pd.to_numeric(movies['year'], errors='coerce')

# Contagem de filmes por ano
movies_per_year = movies['year'].value_counts().sort_index()

plt.figure(figsize=(14, 7))
movies_per_year.plot(kind='bar')
plt.title('Quantidade de Filmes por Ano')
plt.xlabel('Ano')
plt.ylabel('Quantidade de Filmes')
plt.show()

# Função para contar a ocorrência de gêneros


def contar_ocorrencia_generos(movies):
    genres = movies['genres'].str.split('|').explode()
    genre_counts = Counter(genres)
    return genre_counts


# Contar as ocorrências dos gêneros
genre_counts = contar_ocorrencia_generos(movies)
print("\nCenso dos Gêneros:")
print(genre_counts)

# Exibir o resultado em um gráfico de barras
fig = plt.figure(figsize=(14, 6))
ax2 = fig.add_subplot(2, 1, 2)
y_axis = list(genre_counts.values())
x_axis = list(range(len(genre_counts)))
x_label = list(genre_counts.keys())

plt.xticks(rotation=85, fontsize=15)
plt.yticks(fontsize=15)
plt.xticks(x_axis, x_label)
plt.ylabel("No. of occurrences", fontsize=24, labelpad=0)
ax2.bar(x_axis, y_axis, align='center', color='r')
plt.title("Popularidade dos Gêneros", bbox={
          'facecolor': 'k', 'pad': 5}, color='w', fontsize=30)
plt.show()
