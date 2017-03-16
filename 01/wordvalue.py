from data import DICTIONARY, LETTER_SCORES

def load_words():
    with open(DICTIONARY) as f:
        return [line.strip('\n') for line in f]

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    pass

def max_word_value(words):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    pass

if __name__ == "__main__":
    pass # run unittests to validate
