import re


def normalize_token(token):
    token = token.lower()
    # try eliminating everything except a-z
    term = re.sub(r"[^a-z]+", "", token)
    # if we removed everything, try keeping only numbers
    if len(term) == 0:
        # replace everything that is not 0-9
        term = re.sub(r"\D+", "", token)
    return term


class Document:
    """
    This class represents the data in a single web page and includes
    methods to compute term frequency
    """

    def __init__(self, path):
        """
        Takes a path to a document and initializes the document data
        """
        self.path = path
        self.words = list()
        self.unique_words = set()
        self.frequency = dict()
        with open(path) as file:
            lines = file.readlines()
            for line in lines:
                line_words = line.split()
                for word in line_words:
                    token = normalize_token(word)
                    self.words.append(token)
                    if token not in self.unique_words:
                        self.unique_words.add(token)
        for token in self.words:
            self.frequency[token] = (self.words.count(token) / len(self.words))

    def get_path(self):
        """
        Returns the path of the file that this document represents
        """
        return self.path

    def get_words(self):
        """
        Returns a list of the unique, normalized words in this document
        """
        return list(self.unique_words)

    def term_frequency(self, word):
        """
        Returns the term frequency of a given term by looking it up in the
        precomputed dictionary and normalizes the term. If a term does not
        appear in a given document, it should have a term frequency of 0
        """
        word = normalize_token(word)
        if word not in self.frequency:
            return 0
        return self.frequency[word]
