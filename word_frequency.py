import re

"""
Cleans input
processes input
into dictionary
"""
def word_frequency(string,forbidden=None):
    string = clean_text(string)

    return dict_word_counts(string,forbidden)


"""
normalizes string input
to lowercase, removes
whitespace and returns
a list of words
"""
def clean_text(string):
    #string = string.strip(r'[^A-Za-z]+')
    string = string.lower()
    string = re.sub(r'[^A-Za-z]+', ',', string)
    string = string.strip(r',')
    string = string.split(',')

    return string
"""
Creates a dictionary
and adds each new word
it encounters in the input string
to the dictionary
with value = number of instances
in the input string
"""
def dict_word_counts(string, forbidden):
    counts={}
    #print(string)
    if forbidden != None:
        for word in string:
            if word not in counts and word not in forbidden:

                counts[word]=len(list(filter(lambda x: x==word, string)))

        return counts

    else:
        for word in string:
            if word not in counts:
                counts[word]=len(list(filter(lambda x: x==word, string)))

        return counts


if __name__ == '__main__':
    main()
