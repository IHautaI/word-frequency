import sys

from word_frequency import word_frequency


def main():
    input_string = ''
    with open(sys.argv[0], 'r') as input_file:
        input_string = input_file.read()

        print(word_frequency(input_string)) 

if __name__ == '__main__':
    main()
