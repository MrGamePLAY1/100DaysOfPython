import pandas as pd
import random


def random_word():
    dataframe = pd.read_csv('data/french_words.csv')
    french = dataframe['French'].to_list()
    random_french = random.choice(french)
    print(random_french)
    return random_french