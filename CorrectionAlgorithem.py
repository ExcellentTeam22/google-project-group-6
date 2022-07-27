from string import ascii_lowercase


def check_for_correction(sentence: str):
    character_replacement(sentence)
    character_addition(sentence)
    character_removal(sentence)


def find_in_data_base(sentence: str):
    pass


def score_found_result(original_sentence: str, fixed_sentence: str, index_of_character: int):
    pass


def character_replacement(sentence: str):
    for i, ch in enumerate(sentence):
        for c in ascii_lowercase:
            sentence_to_search = sentence[:i] + c + sentence[i + 1:]
            find_in_data_base(sentence_to_search)


def character_addition(sentence: str):
    for i in range(len(sentence) + 1):  # Plus 1 so it will also add characters at the end of the string.
        for c in ascii_lowercase:
            sentence_to_search = sentence[:i] + c + sentence[i:]
            find_in_data_base(sentence_to_search)


def character_removal(sentence: str):
    for i in range(len(sentence) + 1):
        sentence_to_search = sentence[:i] + sentence[i + 1:]
        find_in_data_base(sentence_to_search)


if __name__ == '__main__':
    print(check_for_correction("Dvir Peckin"))
