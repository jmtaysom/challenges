import pytest

from data import DICTIONARY, LETTER_SCORES

def load_words():
    with open(DICTIONARY) as f:
        return [line.strip('\n').replace('-','') for line in f]

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    return sum([LETTER_SCORES[letter.upper()] for letter in word])

def max_word_value(words=load_words()):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    max_value = 0
    best_word = ''
    for word in words:
        value = calc_word_value(word)
        if value > max_value:
            max_value = value
            best_word = word
    return best_word

if __name__ == "__main__":
    pytest.main()
