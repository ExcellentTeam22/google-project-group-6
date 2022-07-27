import DataBase

db = DataBase.DataBase()
words = db.get_words()


def validate_input(sentence: str):
    for word in sentence.split():
        if not words.get(word):
            return set()
        if db.get_frequencies().get(word):
            sentence = sentence.replace(word, "")
    if not sentence:
        return set()


def find_in_data_base(sent: str):
    sentence = sent  # Because we change the given sentence, so we want to have also the original sentence
    validate_input(sent)

    word_min_frequency = sentence.split()[0]
    min_frequency = len(words.get(word_min_frequency).keys())
    for word in sentence.split():
        if len(words.get(word).keys()) < min_frequency:
            min_frequency = len(words.get(word).keys())
            word_min_frequency = word
    sentence = sentence.replace(word_min_frequency, "")
    file_names_intersection = {}
    for word_intersection in sentence.split():
        file_names_intersection = set(words.get(word_min_frequency).keys())\
            .intersection(set(words.get(word_intersection).keys()))

    if not sentence:
        result = set()
        for key in words.get(word_min_frequency).keys():
            for line in list(words.get(word_min_frequency)[key]):
                result.add((key,  db.get_files_content()[key][line].decode("utf-8")))
        return result

    files_and_lines_numbers = list()
    lines_numbers = list()
    for file_name in file_names_intersection:
        for word_intersection in sentence.split():
            lines_numbers = set(words.get(word_min_frequency)[file_name])\
                .intersection(set(words.get(word_intersection)[file_name]))
        files_and_lines_numbers.append({file_name: lines_numbers})

    result = set()
    for file_and_lines_numbers in files_and_lines_numbers:
        for line in list(file_and_lines_numbers.values())[0]:
            if sent in db.get_files_content()[list(file_and_lines_numbers.keys())[0]][line].decode("utf-8"):
                result.add((list(file_and_lines_numbers.keys())[0], db.get_files_content()[list(file_and_lines_numbers.keys())[0]][line]))
    return result


if __name__ == '__main__':
    for item in find_in_data_base("Internet"):
        print(item)






