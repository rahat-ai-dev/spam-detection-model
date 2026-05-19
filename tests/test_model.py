import pickle
from src.models.predict import predict_message

def test_spam_prediction():
    result=predict_message("Free prize! Click now to win cash!")
    assert result in ["SPAM", "Spam", "spam"]

def test_ham_prediction():
    result=predict_message("hey, are you coming to the meeting tomorrow?")
    assert result in ["HAM", "Ham", "ham"]


def test_model_loads():
    model=pickle.load(open('models/spam_classifier.pkl','rb'))
    assert model is not None
