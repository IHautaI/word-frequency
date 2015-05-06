import sys

from word_frequency import word_frequency,clean_text


def printer(word_dict):
    key_list = sorted(word_dict,key=lambda x: word_dict[x], reverse=True)
    maximum = max(word_dict.values())
    minimum = min(word_dict.values())
    scale = (maximum-minimum)

    for index in range(20):#len(key_list)):
        num = int(50*word_dict[key_list[index]]/scale)
        print(key_list[index] + ' :' + '#'*(num+1))


def main():
    input_string = ''
    forbidden = None

    if len(sys.argv)>2:
        with open(sys.argv[2], 'r') as second_file:
            forbidden = second_file.read()
            forbidden = clean_text(forbidden)

    with open(sys.argv[1], 'r') as input_file:
        input_strings = input_file.readlines()

    word_dict = {}
    for line in input_strings:
        new_dict = word_frequency(line,forbidden)
        for key,value in new_dict.items():
            if key in word_dict and key != '':
                word_dict[key] += value
            else:
                word_dict[key] = value


    printer(word_dict)







if __name__ == '__main__':
    main()
