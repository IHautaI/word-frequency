import re

"""
Cleans input
processes input
into dictionary
"""
def word_frequency(string,forbidden):
    string = clean_text(string)
    return dict_word_counts(string,forbidden)

"""
normalizes string input
to lowercase, removes
whitespace and returns
a list of words
"""
def clean_text(string):
    string = re.sub(r'[\s]+',' ',string)
    #string = string.strip()
    string.lower()
    string= re.sub(r'[^A-Za-z\s]','',string) #drop nonalphabeticals
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
def dict_word_counts(words, forbidden=None):
    counts={}

    for word in words:
        if word not in counts and word not in forbidden:
            counts[word]=len(list(filter(lambda x: x==word,words)))

    return counts


if __name__ == '__main__':
    main()
