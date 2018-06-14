from a05 import word_count

def test_count_one_word():
    assert(word_count('word')=={'word': 1}
        )

def test_count_one_of_each():
        assert(
            word_count('one of each')=={'one': 1, 'of': 1, 'each': 1}
        )

def test_count_multiple_occurrences_of_a_word():
        assert(
            word_count('one fish two fish red fish blue fish')=={'one': 1, 'fish': 4, 'two': 1, 'red': 1, 'blue': 1}
        )

def test_cramped_list():
        assert(
            word_count('one,two,three')=={'one': 1, 'two': 1, 'three': 1}
        )

def test_expanded_list():
        assert(
            word_count('one,\ntwo,\nthree')=={'one': 1, 'two': 1, 'three': 1}
        )

def test_ignores_punctuation():
        assert(
            word_count('car : carpet as java : javascript')=={'car': 1, 'carpet': 1, 'as': 1, 'java': 1, 'javascript': 1}
        )


def test_include_numbers():
        assert(
            word_count('testing 1 2 testing')=={'testing': 2, '1': 1, '2': 1}
        )

def test_normalize_case():
        assert(
            word_count('go Go GO Stop stop')=={'go': 3, 'stop': 2}
        )

def test_apostrophes():
        assert(
            word_count("First: don't laugh. Then: don't cry.")=={'first': 1, "don't": 2, 'laugh': 1, 'then': 1, 'cry': 1}
        )
def test_quotations():
        assert(
            word_count("Joe can't tell between 'large' and large.")=={'joe': 1, "can't": 1, 'tell': 1, 'between': 1, 'large': 2,
             'and': 1}
        )

def test_multiple_spaces_not_detected_as_a_word():
        assert(
            word_count(' multiple   whitespaces')=={'multiple': 1, 'whitespaces': 1}
        )

    # Additional tests for this track

def test_tabs():
        assert(
            word_count('rah rah ah ah ah\troma roma ma\tga ga oh la la\t'
                       'want your bad romance')=={'rah': 2, 'ah': 3, 'roma': 2, 'ma': 1, 'ga': 2, 'oh': 1, 'la': 2,
             'want': 1, 'your': 1, 'bad': 1, 'romance': 1}
        )

def test_non_alphanumeric():
        assert(
            word_count('hey,my_spacebar_is_broken.')=={'hey': 1, 'my': 1, 'spacebar': 1, 'is': 1, 'broken': 1}
        )


