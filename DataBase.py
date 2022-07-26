import collections
import zipfile
from singletonDecorator import singleton


@singleton
class DataBase:
    def __init__(self):
        self.files_content = collections.defaultdict(list)
        self.words = dict()
        self.read_zip()
        self.words_appearances()

    def get_files_content(self):
        return self.files_content

    def get_words(self):
        return self.words

    def read_zip(self):
        with zipfile.ZipFile('Archive.zip', 'r') as zip_obj:
            for file_name in zip_obj.namelist():
                with zip_obj.open(file_name) as file:
                    self.files_content[file_name] = file.readlines()

    def words_appearances(self):
        for index, key in enumerate(self.files_content.keys()):
            for row, line in enumerate(self.files_content[key]):
                for word in line.split():
                    word = word.decode('utf-8')
                    res = "".join([ch for ch in word if ch.isalpha()])
                    if res:
                        self.words.setdefault(res, {}).setdefault(key, []).append(row)