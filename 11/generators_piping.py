"""
Turn the following unix pipeline into Python code using generators

$ for i in ../*/*py; do grep ^import $i|sed 's/import //g' ; done | sort | uniq -c | sort -nr
   4 unittest
   4 sys
   3 re
   3 csv
   2 tweepy
   2 random
   2 os
   2 json
   2 itertools
   1 time
   1 datetime
"""
import glob
import re

def gen_files(pat):
    for file in glob.iglob(pat):
        yield file

def gen_lines(file):
    with open(file, 'r') as f:
        for line in f:
            yield line

def gen_grep(pattern, line):

    match = re.search(pattern, line)
    if match:
        yield match.groups()[0]

def gen_count(lines):
    pass


if __name__ == "__main__":
    # call the generators, passing one to the other
    files = gen_files('../*/*.py')
    lines = gen_lines(files)
    for line in gen_lines('../10/movies.py'):
        for match in gen_grep('^import (\w+)', line):
            print(match)
