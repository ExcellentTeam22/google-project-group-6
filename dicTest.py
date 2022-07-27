import numpy
import DataBase


def check_sen(sent: str):
    db = DataBase.DataBase()
    sentence = sent

    for word in sentence.split():
        if not db.get_words().get(word):
            return
        if db.get_frequencies().get(word):
            sentence = sentence.replace(word, "")
    if not sentence:
        return
    word_min_frequency = sentence.split()[0]
    min_frequency = len(db.get_words().get(word_min_frequency).keys())
    for word in sentence.split():
        if len(db.get_words().get(word).keys()) < min_frequency:
            min_frequency = len(db.get_words().get(word).keys())
            word_min_frequency = word
    sentence = sentence.replace(word_min_frequency , "")
    file_names_intersection = {}
    for word_intersection in sentence.split():
        file_names_intersection = set(db.get_words().get(word_min_frequency).keys())\
            .intersection(set(db.get_words().get(word_intersection).keys()))

    if not sentence:
        print(db.get_words().get(word_min_frequency))
    files_and_lines_numbers = list()
    lines_numbers = list()
    for file_name in file_names_intersection:
        for word_intersection in sentence.split():
            lines_numbers = db.get_words().get(word_min_frequency)[file_name].intersection(set(db.get_words().get(word_intersection)[file_name]))
        files_and_lines_numbers.append({file_name: lines_numbers})

    result = set()
    for file_and_lines_numbers in files_and_lines_numbers:
        print(list(file_and_lines_numbers.keys())[0])
        print(list(file_and_lines_numbers.values()))
        for line in list(file_and_lines_numbers.values())[0]:
            if sent in db.get_files_content()[list(file_and_lines_numbers.keys())[0]][line].decode("utf-8"):
                result.add(db.get_files_content()[list(file_and_lines_numbers.keys())[0]][line])
    print(result)


if __name__ == '__main__':
    check_sen("Advanced Bash-Scripting Guide")












    # {'I': {'d.txt': (0, 1, 2, 3)}, 'am': {'d.txt': (0, 1, 2, 3), 'v.txt': (3,)}, 'dvir': {'d.txt': (0,), 'v.txt': (6,)},
    #  'Rachel': {'d.txt': (1,)}, 'Elhanan': {'d.txt': (2,)}, 'Yaniv': {'d.txt': (3,)}, 'PI': {'v.txt': (0,)},
    #  'Reference': {'v.txt': (0, 2, 4, 7, 9)}, 'API': {'v.txt': (1, 7, 8, 8, 9)}, 'Client': {'v.txt': (1,)},
    #  'Libraries': {'v.txt': (1,)}, 'CLI': {'v.txt': (2,)}, 'Components': {'v.txt': (4,)}, 'Design': {'v.txt': (5,)},
    #  'Docs': {'v.txt': (5,)}, 'Kubernetes': {'v.txt': (8, 8, 9)}, 'Overview': {'v.txt': (8, 8)}, 'of': {'v.txt': (8,)},
    #  'the': {'v.txt': (8,)}, 'for': {'v.txt': (8,)}, 'v': {'v.txt': (9,)}}
    # {'am': 5, 'Reference': 5, 'API': 5}





