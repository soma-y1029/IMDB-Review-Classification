import csv
import torch
from string import punctuation
from collections import Counter

from nltk.corpus import stopwords

def tokenize(reviews):
    '''

    :param reviews:
    :return:
    '''
    # put all reviews in one string
    # at the same time, remove any punctuation
    all_string = ''
    for word in reviews:
        all_string += ''.join([letter.lower() for letter in word if letter not in punctuation])

    # get stop words from nltk library
    stop_words = stopwords.words('english')

    # split all string with space split and append to tokens if the word is not stop word
    tokens = []
    for word in all_string.split(' '):
        if len(word) > 0 and word not in stop_words:
            tokens.append(word)

    return tokens

file_path = 'IMDB Dataset.csv'
if __name__ == '__main__':
    # data preparation
    # read and prepare given data set and store it in dictionary
    with open(file_path, mode='r') as dataset:
        reader = csv.DictReader(dataset)
        pos_reviews, neg_reivews = [], []
        for row in reader:
            if row['sentiment'] == 'positive':
                pos_reviews.append(row['review'])
            else:
                neg_reivews.append(row['review'])

        pos_tokens = tokenize(pos_reviews)
        neg_tokens = tokenize(neg_reivews)
        pos_word_count = Counter(pos_tokens)
        neg_word_count = Counter(neg_tokens)
        print(pos_word_count.most_common(10))
        print(neg_word_count.most_common(10))
