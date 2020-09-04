import re
''' this class performs tokenization
splits into words and sentences '''

class Tokenizer:
    def __init__(self, data):
        self.data = data

    def word_tokens(self):
        white_space_regex = "[^\s]+"
        word_tokens = re.findall(white_space_regex, self)
        return word_tokens

    def sentence_tokens():
        pass


