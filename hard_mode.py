import sys

from word_frequency import word_frequency


def main():
    input_string = ''
    with open(sys.argv[0], 'r') as input_file:
        input_string = input_file.read()



    if len(sys.argv)>1:
        forbidden = None
        with open(sys.argv[1], 'r') as second_file:
            forbidden = second_file.read()
            forbidden = forbidden.split(',')

    print(word_frequency(input_string, forbidden=forbidden))


if __name__ == '__main__':
    main()
