import re
import string

class Controller:
    def __init__(self, text):
        self.text = text

    def remove_punctuation(self):
        """
        In text, replaces all symbols in spring.punctuation with a space.
        string.punctuation = !"#$%&'()*+, -./:;<=>?@[\]^_`{|}~
        :return: The text without any punctuation.
        """
        return re.sub(f"[{re.escape(string.punctuation)}]", ' ', self.text)

    def text_splitter(self):
        """
        Split text into words using space as separator.
        :return: A list of words
        """
        text_without_punctuation = self.remove_punctuation()
        return text_without_punctuation.split()

