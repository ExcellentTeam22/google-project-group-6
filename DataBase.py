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
        self.__words_appearances()

    def __read_zip(self):
        """
        This function reads a content of an Archive.zip file and store it
        in a dictionary defined as {filename: content}
        :return: None
        """
        with zipfile.ZipFile('Archive.zip', 'r') as zip_obj:
            for file_name in zip_obj.namelist():
                with zip_obj.open(file_name) as file:
                    self.files_content[file_name] = file.readlines()

    def __words_appearances(self):
        """
        This function go over all the words in Archive.zip file that loaded to files_content
        and stores each word in a dictionary that defined as {word: {filename: Tuple(lines appearance)}}
        The function in addition finds the most common words that the number of appearances of them is greater
        than sqrt(total_num_of_lines)
        :return: None
        """
        all_words_frequencies = dict()

        for index, key in enumerate(self.files_content.keys()):
            for row, line in enumerate(self.files_content[key]):
                self.total_num_of_lines += 1
                for byte_word in line.split():
                    string_word = byte_word.decode('utf-8')
                    clean_string_word = "".join([ch for ch in string_word if ch.isalpha()])
                    if clean_string_word:
                        self.words.setdefault(clean_string_word, {})
                        self.words[clean_string_word].setdefault(key, ())
                        self.words[clean_string_word][key] += (row,)
                        all_words_frequencies.setdefault(byte_word, 0)
                        all_words_frequencies[byte_word] += 1

        'Saves all the words that appear more than sqrt(total_num_of_lines)'
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
