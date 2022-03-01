import random
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from newspaper import Article

import warnings

warnings.filterwarnings('ignore')

# Download punkt package
nltk.download('punkt', quiet=True)

# Get the article
URL = input("GOOD BOT: Please paste the URL that you would like for me to look at")
article = Article(URL)
article.download()
article.parse()
article.nlp()
corpus = article.text

# Print the articles text
print(corpus)

# Tokenization and a list of sentences
text = corpus
sentence_list = nltk.sent_tokenize(text)

# Print
print(sentence_list)


# A function to return a random greeting response to a users greeting
def greeting_response(text):
    text = text.lower()

    # Bots greeting response
    bot_greetings = ['Hello', 'hi', 'hey', 'sup', 'yo', 'Greetings']
    # Users greeting
    user_greetings = ['hi', 'hey', 'hello', 'greetings', 'sup', 'yo', 'wassup', 'what is up', 'good morning',
                      'good afternoon', 'good evening']

    for word in text.split():
        if word in user_greetings:
            return random.choice(bot_greetings)


def index_sort(list_var):
    length = len(list_var)
    list_index = list(range(0, length))

    x = list_var
    for i in range(length):
        for j in range(length):
            if x[list_index[i]] > x[list_index[j]]:
                temp = list_index[i]
                list_index[i] = list_index[j]
                list_index[j] = temp
    return list_index


# Create the bots response
def bot_response(user_input):
    user_input = user_input.lower()
    sentence_list.append(user_input)
    bot_response = ''
    cm = CountVectorizer().fit_transform(sentence_list)
    similarity_scores = cosine_similarity(cm[-1], cm)
    similarity_scores_list = similarity_scores.flatten()
    index = index_sort(similarity_scores_list)
    index = index[1:]
    response_flag = 0
    j = 0
    for i in range(len(index)):
        if similarity_scores_list[index[i]] > 0.0:
            bot_response = bot_response + ' ' + sentence_list[index[i]]
            response_flag = 1
            j = j + 1
        if j > 2:
            break
    if response_flag == 0:
        bot_response = bot_response + ' ' + "I apologize, I don't understand."
    sentence_list.remove(user_input)

    return bot_response


# Start the chat
print('Good Bot: I am Good Bot. Ask any questions on the URL. If you want to exit, type bye.')
exit_list = ['exit', 'see you later', 'bye', 'quit', 'break', 'goodbye']
while True:
    user_input = input()
    if user_input.lower() in exit_list:
        print('Good Bot: Terminating sequence. Talk to you later')
        break
    else:
        if greeting_response(user_input) != None:
            print('Doc Bot: '+greeting_response(user_input))
        else:
            print('Good Bot: '+bot_response(user_input))

# Test of our bot_response() function
user_input = 'hello world'
sentence_list.append(user_input)
bot_response = ''
cm = CountVectorizer().fit_transform(sentence_list)
similarity_scores = cosine_similarity(cm[-1], cm)
similarity_scores_list = similarity_scores.flatten()
index_sort(similarity_scores_list)
print(similarity_scores_list)