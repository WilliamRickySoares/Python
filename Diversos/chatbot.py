from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Crie um objeto ChatBot
chatbot = ChatBot('Meu ChatBot')

# Crie um treinador para o chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Treine o chatbot usando o conjunto de dados de treinamento em inglês
trainer.train('chatterbot.corpus.english')

# Inicie a interação com o chatbot
print('ChatBot: Olá! Como posso ajudar você hoje?')

while True:
    # Obtenha a entrada do usuário
    user_input = input('Usuário: ')

    # Obtenha a resposta do chatbot
    response = chatbot.get_response(user_input)

    # Imprima a resposta do chatbot
    print('ChatBot:', response)
