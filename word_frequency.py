import re

"""
Cleans input
processes input
into dictionary
"""
def word_frequency(string):
    string = clean_text(string)
    return dict_word_counts(string)

"""
normalizes string input
to lowercase, removes
whitespace and returns
a list of words
"""
def clean_text(string):
    string = string.strip()
    string.lower()
    string= re.sub(r'[^A-Za-z\s]','',string) #drop nonalphabeticals
    string = re.sub(r'[\s]+',' ',string) #replace multiple whitespace w/ single
    string = string.split(" ")
    return string

"""
Creates a dictionary
and adds each new word
it encounters in the input string
to the dictionary
with value = number of instances
in the input string
"""
def dict_word_counts(words):
    counts={}

    for word in words:
        if word not in counts:
            counts[word]=len(list(filter(lambda x: x==word,words)))


    return counts
