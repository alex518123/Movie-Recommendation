from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd


def calcular_similaridade(movies, tags):
    # Juntar as tags e os gêneros dos filmes em uma única string
    movies['tags'] = movies['movieId'].map(tags.groupby(
        'movieId')['tag'].apply(lambda x: ' '.join(x)).to_dict()).fillna('')
    movies['dados_filme'] = movies['genres'] + ' ' + movies['tags']

    # Vetorizar a coluna
    count_vectorizer = CountVectorizer(stop_words='english')
    count_data = count_vectorizer.fit_transform(movies['dados_filme'])

    # Calcular a similaridade dos cossenos
    cosine_sim = cosine_similarity(count_data, count_data)
    return cosine_sim


def recomendar_filmes(titulo, qty, movies, cosine_sim, ratings_mean):
    # Verificar se o filme existe no DataFrame
    if titulo not in movies['title'].values:
        return f"Desculpe, o filme '{titulo}' não foi encontrado no banco de dados."

    index = pd.Series(movies.index, index=movies['title']).drop_duplicates()
    idx = index[titulo]

    # Obter as pontuações de similaridade dos filmes
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Ajustar as pontuações de similaridade com base na média das avaliações
    for i, score in sim_scores:
        movie_id = movies.loc[i, 'movieId']
        sim_scores[i] = (i, score * ratings_mean.get(movie_id, 0))

    # Ordenar as pontuações para ver quem está mais próximo do outro
    sim_scores_ordered = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Retornar as recomendações similares
    recommendations_qty = qty + 1  # Inclui o próprio filme na contagem
    recommendations = sim_scores_ordered[1:recommendations_qty]

    # Pegar os índices dos filmes das recomendações
    movies_indexes = [i[0] for i in recommendations]

    # Retornar o título dos filmes recomendados
    return movies['title'].iloc[movies_indexes]
