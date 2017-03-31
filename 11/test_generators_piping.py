import pytest
from generators_piping import gen_files, gen_lines

def test_gen_files():
    files = gen_files('../*/*py')
    assert next(files) == '../01/data.py'

def test_gen_lines():
    lines = gen_lines(['../10/movies.py', '../10/movies.py'])
    assert next(lines) == 'import random\n'