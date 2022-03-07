import unittest
import pytest

from sklearn.feature_extraction.text import CountVectorizer


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here


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
