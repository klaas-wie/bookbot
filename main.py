from stats import count_words, count_chars, list_dicts, beautify

import sys

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file = sys.argv[1]

    text = read_file(file)

    char_count = count_chars(text)
    word_count = count_words(text)
    dict_list = list_dicts(char_count)

    beautify(file, word_count, dict_list)

def read_file(file):

    with open(file) as f:
        text = f.read()

    return text


main()
    