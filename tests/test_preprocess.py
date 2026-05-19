import sys
sys.path.insert(0, '.')
from src.data.preprocess import clean_text

def test_lowercase():
    result=clean_text('HELLO WORLD')
    assert result==result.lower()

def test_removes_punctuation():
    result=clean_text('Hello!!!')
    assert '!' not in result

def test_removes_stopwords():
    result=clean_text('This ia a test')
    assert 'is' not in result
    assert 'this' not in result

def test_empty_string():
    result=clean_text('')
    assert result==''
    