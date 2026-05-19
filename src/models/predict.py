import pickle
from src.data.preprocess import clean_text
from src.features.build_features import load_vectorizer

def load_model(path='models/spam_classifier.pkl'):
    return pickle.load(open(path,'rb'))

def predict_message(message,model=None, vectorizer=None):
    if model is None:
        model=load_model()
    if vectorizer is None:
        vectorizer=load_vectorizer()

    cleaned=clean_text(message)
    vectorized= vectorizer.transform([cleaned])
    result=model.predict(vectorized)[0]

    return 'Spam' if result==1 else 'Ham'

