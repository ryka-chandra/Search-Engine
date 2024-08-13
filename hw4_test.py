import org.junit.Assert.*;
from document import Document
from search_engine import SearchEngine


def test_get_words(doc1, doc2, doc3):
    """
    Tests get_words method in Document class
    """
    assert_equals(sorted(['bestttttt', 'food', 'in', 'is', 'sush', 'the', 'world']), sorted(doc1.get_words()))
    assert_equals(sorted(['clr', 'emerald', 'favorite', 'green', 'is', 'my']), sorted(doc2.get_words()))
    assert_equals(sorted(['best', 'country', 'creek', 'go', 'high', 'i', 'in', 'north', 'school', 'the', 'to']), sorted(doc3.get_words()))

def test_term_frequency(doc1, doc2, doc3):
    """
    Tests term_frequency method in Document class
    """
    assert_equals(0.2222222222222222, doc1.term_frequency('_food_'))
    assert_equals(0.16666666666666666, doc2.term_frequency('favorite!!'))
    assert_equals(0.08333333333333333, doc3.term_frequency('COuntrY'))

def test_get_path(doc1, doc2, doc3):
    """
    Tests get_path method in Document class
    """
    assert_equals('ryka_test_corpus/best_food.txt', doc1.get_path())
    assert_equals('ryka_test_corpus/favorite_color.txt', doc2.get_path())
    assert_equals('ryka_test_corpus/high_school.txt', doc3.get_path())

def test_calculate_idf(se):
    """
    Tests _calculate_idf method in SearchEngine class
    """
    assert_equals(0.4054651081081644, se._calculate_idf('in'))
    assert_equals(0, se._calculate_idf('%%i!!n!!'))
    assert_equals(0, se._calculate_idf('@#$ '))
    assert_equals(1.0986122886681098, se._calculate_idf('emerald'))
    
    #tests blank parameter
    assert_equals(0, se._calculate_idf(''))

def test_single_item_query(se):
    """
    Tests search method in SearchEngine class for one word
    and a series of odd characters with no space between them
    """
    assert_equals([], se.search('  hi'))
    assert_equals(['ryka_test_corpus/favorite_color.txt'], se.search('EMerald'))
    assert_equals(['ryka_test_corpus/high_school.txt'], se.search('&$nor*t^h'))
    assert_equals(['ryka_test_corpus/best_food.txt'], se.search('sush1'))
    assert_equals(['ryka_test_corpus/best_food.txt', 'ryka_test_corpus/high_school.txt'], se.search('in'))

def test_multiple_item_query(se):
    """
    Tests search method in SearchEngine class for multiple
    words and odd characters
    """
    assert_equals(['ryka_test_corpus/high_school.txt'], se.search('h   i there'))
    assert_equals([], se.search('@&$* ___ &#*($#   $(&'))
    assert_equals(['ryka_test_corpus/best_food.txt', 'ryka_test_corpus/high_school.txt'], se.search('in the the'))
    assert_equals([], se.search('c0lor    '))
    assert_equals(['ryka_test_corpus/favorite_color.txt'], se.search('   ()[]() c0l0r'))

def test_blank_query(se):
    """
    Tests search method in SearchEngine class with blank parameter
    """
    assert_equals([], se.search(''))

def main():
    doc1 = Document('ryka_test_corpus/best_food.txt')
    doc2 = Document('ryka_test_corpus/favorite_color.txt')
    doc3 = Document('ryka_test_corpus/high_school.txt')
    se = SearchEngine('ryka_test_corpus/')

    #tests all the Document methods with ryka_test_corpus
    test_term_frequency(doc1, doc2, doc3)
    test_get_words(doc1, doc2, doc3)
    test_get_path(doc1, doc2, doc3)

    #tests every Search Engine method with ryka_test_corpus
    test_calculate_idf(se)
    test_single_item_query(se)
    test_multiple_item_query(se)
    test_blank_query(se)

if __name__ == '__main__':
    main()
