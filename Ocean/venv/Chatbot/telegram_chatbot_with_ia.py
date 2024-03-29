# -*- coding: utf-8 -*-
"""telegram_chatbot_with_ia.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1r1gm1IY_KBju0jlxajGA8NRd9Zzg9JUR

# Instalação de Bibliotecas
"""

# !pip install pytelegrambotapi
# !pip install unidecode
# !pip install pandas
# !pip install nltk
# !pip install scikit-learn

"""# Baixando nosso dataset"""

# !git clone https://github.com/gladson-sza/atrativos_turisticos_dataset.git

"""# Lendo nosso dataset

## Pandas


A biblioteca pandas é uma poderosa biblioteca em Python amplamente utilizada para análise de dados e manipulação de estruturas de dados tabulares, como DataFrames. Ela oferece funcionalidades para carregar, limpar, transformar, analisar e visualizar dados de maneira eficiente.
"""

import pandas as pd


dataset = pd.read_csv('D:\\Meu Python\\Ocean\\venv\\dataset.csv', delimiter=';')

dataset.head(20)

"""# Bibliotecas para tratar strings


"""

import string

"""# Bibliotecas de NLP

## NLTK
O Natural Language Toolkit (NLTK) é uma biblioteca em Python amplamente utilizada para processamento de linguagem natural (NLP). Ela oferece uma gama de ferramentas que tornam mais fácil a realização de análises textuais e tarefas de NLP, bem como a construção de sistemas de processamento de linguagem natural.
"""

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('stopwords')
nltk.download('punkt')

"""# Biblioteca para remoção de acentuação"""

from unidecode import unidecode

"""# Pré processamento de texto"""

def remove_pontuacao(text):
    texto_limpo = ''
    for palavra in text:
      if palavra not in string.punctuation:
        texto_limpo += palavra

    return texto_limpo

print(string.punctuation)

def preprocessamento(texto):
    # Remove pontuações e símbolos
    texto = remove_pontuacao(texto)

    # Remover acentos
    texto = unidecode(texto)

    # Converte para minúsculo
    texto = texto.lower()

    # Tokenização
    tokens = word_tokenize(texto)

    # Remover stopwords
    stop_words = stopwords.words('portuguese')
    tokens = [token for token in tokens if token not in stop_words]

    # Juntar as palavras novamente em uma string
    texto_preprocessado = ' '.join(tokens)

    return texto_preprocessado

dataset["Pergunta_Preprocessada"] = dataset["Pergunta"].apply(preprocessamento)

dataset.head(20)

"""## Vetorização"""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(dataset["Pergunta_Preprocessada"])

"""## Método para obter uma resposta a partir de uma pergunta"""



def obter_resposta(pergunta):
    # Pré processa a sentença da pergunta
    pergunta_processada = preprocessamento(pergunta)
    # print(pergunta_processada)

    # Transforma a pergunta para um vetor
    pergunta_vector = vectorizer.transform([pergunta_processada])
    # print(pergunta_vector)

    # Calcula a similaridade do cosseno
    similaridades = cosine_similarity(pergunta_vector, tfidf_matrix)
    # print(similaridades)

    # Obtém o índice da pergunta mais similar
    pergunta_index = similaridades.argmax()
    # print(pergunta_index)

    # Devolve a resposta para o usuário
    return dataset["Resposta"].iloc[pergunta_index]


q = "Onde ir em Manaus"
obter_resposta(q)

"""## Testando Chatbot"""

flags = ['Fechar', 'Sair', 'Tchau']
end = False

while not end:
    question = input()
    if question in flags:
        end = True
        print('Finalizando Chat')
        continue

    answer = obter_resposta(question)
    print(answer)

"""# Integrando com Telegram"""

# import telebot
#
# API_KEY = ''
# bot = telebot.TeleBot(API_KEY)

# @bot.message_handler(func=lambda message: True)
# def default(message):
#     resposta = obter_resposta(message.text)
#
#     bot.reply_to(
#         message,
#         resposta
#     )
#
# bot.polling()
