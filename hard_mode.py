import sys
#from operator import itemgetter   tested with this

from word_frequency import word_frequency,clean_text


##############################################
# Takes 1 required and 1 optional file input #
# first is file to count from                #
# second is file of csv forbidden words      #
##############################################


"""
Formats and prints Histogram from dictionary of word counts
"""
def printer(word_dict):
    word_list = [(k,v) for k,v in word_dict.items()]
    word_list = sorted(word_list, key=lambda x: x[1],reverse=True)

    maximum = max(word_dict.values())
    minimum = min(word_dict.values())
    scale = (maximum-minimum)/50

    for i in range(20): # or len(word_list) ... but that's too much to read
        print('{}: '.format(word_list[i][0]) + '#'*int(1+word_list[i][1]/scale) + '({})'.format(word_list[i][1]))


"""
Opens the files, feeds them to clean_text/word_frequency
and calls printer on the result
"""
def main():
    input_string = ''
    forbidden = None

    if len(sys.argv)>2:
        with open(sys.argv[2], 'r') as second_file:
            forbidden = []
            lines = second_file.readlines()
            for line in lines:
                if clean_text(line) != []:
                    forbidden += clean_text(line)

    with open(sys.argv[1], 'r') as input_file:
        input_strings = input_file.readlines()

    word_dict = {}
    for line in input_strings:
        new_dict = word_frequency(line,forbidden)
        for key,value in new_dict.items():
            if key in word_dict:# and key != '':
                word_dict[key] += value
            else:
                word_dict[key] = value


    printer(word_dict)


if __name__ == '__main__':
    main()
