import collections
import zipfile

import numpy

from singletonDecorator import singleton

"""
    This class represent a data base that holds all the files contents and
    provide several searching methods.
"""
@singleton
class DataBase:
    def __init__(self):
        self.total_num_of_lines = 0
        self.files_content = collections.defaultdict(list)
        self.words = dict()
        self.frequencies = dict()
        self.__read_zip()

    def __read_zip(self):
        """
        This function reads a content of an Archive.zip file and store it
        in a dictionary defined as {filename: content}
        :return: None
        """
        with zipfile.ZipFile('Archive.zip', 'r') as zip_obj:
            for file_name in zip_obj.namelist():
                with zip_obj.open(file_name) as file:
                    for row, byte_line in enumerate(file.readlines()):
                        self.total_num_of_lines += 1
                        str_line = byte_line.decode('utf-8')
                        if str_line and str_line != '\n':
                            self.files_content[file_name] += [str_line]
                        self.__words_appearances(str_line, row, file_name)

    def __words_appearances(self, line, row, file_name):
        """
        This function go over all the words in Archive.zip file that loaded to files_content
        and stores each word in a dictionary that defined as {word: {filename: Tuple(lines appearance)}}
        The function in addition finds the most common words that the number of appearances of them is greater
        than sqrt(total_num_of_lines)
        :return: None
        """
        all_words_frequencies = dict()

        for word in line.split():
            lower_case_word = word.lower()
            if self.words.get(lower_case_word) is None:
                self.words[lower_case_word] = dict()
            if self.words[lower_case_word].get(file_name) is None:
                self.words[lower_case_word][file_name] = tuple()
            self.words[lower_case_word][file_name] += (row,)
            if all_words_frequencies.get(lower_case_word) is None:
                all_words_frequencies[lower_case_word] = 0
            all_words_frequencies[lower_case_word] += 1

        # 'Saves all the words that appear more than sqrt(total_num_of_lines)'
        for key in all_words_frequencies.keys():
            if all_words_frequencies[key] > numpy.sqrt(self.total_num_of_lines):
                self.frequencies.setdefault(key, all_words_frequencies[key])

    def get_total_num_of_lines(self):
        return self.total_num_of_lines

    def get_files_content(self):
        return self.files_content

    def get_words(self):
        return self.words

    def get_frequencies(self):
        return self.frequencies