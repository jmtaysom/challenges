#!python3
# Code Challenge 02 - Word Values Part II - a simple game
# http://pybit.es/codechallenge02.html
from random import sample
from collections import Counter
from data import DICTIONARY, LETTER_SCORES, POUCH

NUM_LETTERS = 7


# re-use from challenge 01
def calc_word_value(word):
    """Calc a given word value based on Scrabble LETTER_SCORES mapping"""
    return sum(LETTER_SCORES.get(char.upper(), 0) for char in word)


# re-use from challenge 01
def max_word_value(words):
    """Calc the max value of a collection of words"""
    return max(words, key=calc_word_value)

def draw_letters(pouch=POUCH, n=7):
    return sample(pouch,n)

def check_word(hand,word):
    hand_count = Counter(hand)
    word_count = Counter([letter for letter in word.upper()])
    hand_count.subtract(word_count)
    return all([False if value < 0 else True for value in hand_count.values()]) and word.lower() in DICTIONARY


def main():
    hand = draw_letters()
    print(hand)


if __name__ == "__main__":
    main()
