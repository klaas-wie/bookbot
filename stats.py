def count_words(text):

    count = len(text.split())

    return count

def count_chars(text):

    text = text.lower()
    chars = list(text)
    uniques = set(chars)
    char_dict = {}

    for unique in uniques:
        char_dict[unique] = chars.count(unique)

    return char_dict

def sort_on(dict):
    return dict["count"]

def list_dicts(char_dict):

    dict_list = []
    temp_dict = {}

    for key in char_dict:

        if key.isalpha():

            temp_dict["char"] = key
            temp_dict["count"] = char_dict[key]

            dict_list.append(temp_dict)
            temp_dict = {}

    dict_list.sort(key=sort_on, reverse=False)

    return dict_list

def beautify(filepath, word_count, dict_list):

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for dict in dict_list:
        print(f"{dict["char"]}: {dict["count"]}")

    print("============= END ===============")


