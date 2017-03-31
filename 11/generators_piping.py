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
    for f in glob.iglob(pat):
        yield f


def gen_lines(files):
    for file in files:
        with open(file, 'r') as f:
            for line in f:
                yield line

def gen_grep(pattern, lines):
    for line in lines:
        match = re.search(pattern, line)
        if match:
            yield match.groups()[0]

def gen_count(lines):
    pass


if __name__ == "__main__":
    # call the generators, passing one to the other
    files = gen_files('../*/*.py')
    lines = gen_lines(files)
    grep = gen_grep('^import (\w+)', lines)
    for g in grep:
        print(g)



