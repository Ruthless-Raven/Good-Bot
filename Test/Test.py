import unittest
import pytest
import Good-Bot

import random
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from newspaper import Article

import warnings
from sklearn.feature_extraction.text import CountVectorizer


class MyTestCase(unittest.TestCase):
    def test_greetingresponsea(self):
        assert greeting_response("hi") in ['Hello', 'hi', 'hey', 'sup', 'yo', 'Greetings'] # add assertion here

    def test_greetingresponseb(self):
        assert greeting_response("Hello") in ['Hello', 'hi', 'hey', 'sup', 'yo', 'Greetings']

    def test_greetingresponsec(self):
        assert greeting_response("hey") in ['Hello', 'hi', 'hey', 'sup', 'yo', 'Greetings']

    def test_greetingresponsed(self):
        assert greeting_response("sup") in ['Hello', 'hi', 'hey', 'sup', 'yo', 'Greetings']

    def test_greetingresponsee(self):
        assert greeting_response("yo") in ['Hello', 'hi', 'hey', 'sup', 'yo', 'Greetings']

    def test_greetingresponsef(self):
        assert greeting_response("Greetings") in ['Hello', 'hi', 'hey', 'sup', 'yo', 'Greetings']

    def test_indexsorta(self):
        assert index_sort(['a', 'b', 'c']) == 3


    # Test of our bot_response() function
    user_input = 'hello world'
    sentence_list.append(user_input)
    bot_response = ''
    cm = CountVectorizer().fit_transform(sentence_list)
    similarity_scores = cosine_similarity(cm[-1], cm)
    similarity_scores_list = similarity_scores.flatten()
    index_sort(similarity_scores_list)
    print(similarity_scores_list)


if __name__ == '__main__':
    unittest.main()
