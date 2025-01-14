# Sistema de Recomendação de Filmes

Este é um sistema de recomendação de filmes baseado em similaridade de conteúdo, utilizando dados do [Movielens Dataset](https://grouplens.org/datasets/movielens/). O sistema recomenda filmes semelhantes a partir de um filme fornecido pelo usuário, com base na análise de gêneros e tags associadas a cada filme. A recomendação é feita por meio de uma combinação de similaridade de cosseno e a média das avaliações dos filmes.

## 📂 Estrutura do Projeto

A estrutura do projeto está organizada da seguinte forma:

Movie_Recommendation/
│
├── data_loader.py       # Carregamento e processamento de dados
├── recommender.py       # Função de recomendação de filmes
├── main.py              # Interação com o usuário
└── requirements.txt     # Dependências do projeto


### Descrição dos Arquivos necessários

- **`data_loader.py`**: Contém funções para carregar os dados dos filmes, avaliações e tags. Também contém a função para contar a ocorrência de cada gênero nos filmes.
- **`recommender.py`**: Contém as funções para calcular a similaridade entre os filmes usando o método de similaridade de cosseno e para recomendar filmes com base no título do filme fornecido pelo usuário.
- **`main.py`**: O arquivo principal do projeto, que interage com o usuário, carrega os dados e exibe as recomendações de filmes.
- **`movies.csv`**: Contém informações sobre os filmes, incluindo títulos e gêneros.
- **`ratings.csv`**: Contém informações sobre as avaliações dos usuários para os filmes.
- **`tags.csv`**: Contém informações sobre as tags associadas aos filmes.
- **`requirements.txt`**: Lista as dependências necessárias para rodar o projeto.

## 📦 Instalação

### Pré-requisitos

Antes de rodar o projeto, você precisa garantir que o Python esteja instalado em sua máquina. Recomendamos o uso de um ambiente virtual.

1. **Crie um ambiente virtual** (se estiver utilizando `venv`):
   ```bash
   python -m venv venv

2. **Ative o ambiente virtual**

No Windows:
.\venv\Scripts\activate

No Linux/Mac:
source venv/bin/activate

3. **Instale as dependências**
As dependências estão listadas no arquivo requirements.txt. Para instalá-las, basta rodar o comando:
pip install -r requirements.txt

Dependências principais:
**pandas** Para manipulação de dados.
**scikit-learn** Para cálculo de similaridade e vetorização de texto.
**matplotlib** Para visualização (caso necessário, não é utilizado diretamente no código, mas pode ser útil para maior entendimento do dataset).

## 🖥️ Como Usar
1. **Baixe o Dataset**
O dataset pode ser obtido no site do [Movielens](https://grouplens.org/datasets/movielens/). Faça o download dos arquivos movies.csv, ratings.csv e tags.csv e coloque-os na pasta do projeto.

2. **Rodando o Projeto**
Para rodar o sistema de recomendação, execute o arquivo main.py:
python main.py

O sistema pedirá o nome de um filme e o número de recomendações que você deseja. Ele retornará uma lista de filmes recomendados com base na similaridade de conteúdo.

**Exemplo de interação**
Qual filme você quer recomendações? Babe (1995)
Quantas recomendações você quer? 3
3970           Yearling, The (1946)
4269               Born Free (1966)
5521    Anne of Green Gables (1985)


## 📝 Explicação do Algoritmo
O sistema utiliza um modelo de similaridade de cosseno para calcular a similaridade entre filmes, levando em consideração os seguintes fatores:

**Gêneros dos filmes** Os gêneros de cada filme são analisados e combinados com as tags associadas.
**Tags** As tags associadas a cada filme são agrupadas e combinadas com os gêneros para formar uma representação de conteúdo para cada filme.
**Média das avaliações** Para ajustar a recomendação, a média das avaliações dos filmes é levada em consideração, ponderando a similaridade com as classificações dos usuários.

Passos do algoritmo:
Carregar dados: Os dados dos filmes, avaliações e tags são carregados a partir dos arquivos CSV.
Contar gêneros: A ocorrência de cada gênero é calculada para fins de análise.
Calcular similaridade: Utiliza a similaridade de cosseno para calcular a semelhança entre os filmes com base nos gêneros e nas tags.
Recomendar filmes: O usuário fornece um título de filme com o ano de lançamento entre parênteses, e o sistema retorna uma lista dos filmes mais semelhantes.

## 📜 Licença

Este projeto está licenciado sob a Licença MIT - consulte o arquivo LICENSE para mais informações.

---

### 📧 Contato

Caso tenha dúvidas ou sugestões, entre em contato:
- Email: alexresende675@gmail.com



