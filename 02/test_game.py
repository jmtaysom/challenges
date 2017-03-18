import pytest

from game import draw_letters, check_word

def test_draw_letters():
    assert len(draw_letters()) == 7


def test_check_word():
    word = 'LIBRARY'
    hand = [letter for letter in word.upper()]
    assert check_word(hand,word)