from document import Document
from math import log
import os
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


class SearchEngine:
    """
    This class represents a corpus of Document objects and
    includes methods to compute the tf–idf statistic between
    each document and a given query
    """

    def __init__(self, directory):
        """
        Takes a str path to a directory and constructs an inverted
        index associating each term in the corpus to the list of
        documents that contain the term
        """
        self.inverted_index = dict()
        self.documents = []
        for filename in os.listdir(directory):
            path = os.path.join(directory, filename)
            doc = Document(path)
            self.documents.append(doc)
            words = doc.get_words()
            if len(words) != 0:
                for word in words:
                    if word in self.inverted_index:
                        self.inverted_index[word].append(doc)
                    else:
                        self.inverted_index[word] = [doc]

    def _calculate_idf(self, term):
        """
        Takes a str term and returns the inverse document frequency
        of that term. If the term is not in the corpus, returns 0
        """
        if term not in self.inverted_index:
            return 0
        else:
            return log(len(self.documents) / len(self.inverted_index[term]))

    def search(self, query):
        """
        Takes a str query that contains one or more terms and returns a list
        of document paths sorted in descending order by tf–idf statistic.
        It normalizes the terms before processing and if there are no matching
        documents, returns an empty list
        """
        docs = self.documents
        tfidf_list = []
        terms = query.split()
        for doc in docs:
            tfidf = 0
            for term in terms:
                term = normalize_token(term)
                tfidf += doc.term_frequency(term) * self._calculate_idf(term)
            if tfidf > 0:
                tfidf_list.append((doc, tfidf))
        tfidf_list.sort(key=lambda x: x[1], reverse=True)
        path_list = [i[0].get_path() for i in tfidf_list]
        return path_list
