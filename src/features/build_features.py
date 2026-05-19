import pickle
from sklearn.feature_extraction.text import TfidfVectorizer

def build_tfidf(x_train,x_test,max_features=3000):
    vectorizer= TfidfVectorizer(max_features=max_features)
    x_train_tfidf=vectorizer.fit_transform(x_train)
    x_test_tfidf=vectorizer.transform(x_test)
    return x_train_tfidf, x_test_tfidf, vectorizer

def save_vectorizer(vectorizer, path='models/tfidf_vectorizer.pkl'):
    pickle.dump(vectorizer, open(path,'wb'))
    print(f'Vectorizer saved to {path}')

def load_vectorizer(path='models/tfidf_vectorizer.pkl'):
    return pickle.load(open(path,'rb'))
