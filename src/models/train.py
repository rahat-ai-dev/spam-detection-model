import pickle
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
def train_naive_bayes(x_train,y_train):
    model=MultinomialNB()
    model.fit(x_train,y_train)
    return model

def train_logistics_regression(x_train,y_train):
    model=LogisticRegression(max_iter=1000)
    model.fit(x_train,y_train)
    return model

def save_model(model,path='models/spam_classifier.pkl'):
    pickle.dump(model,open(path,'wb'))
    print(f'Model saved to {path}')

def load_model(path='models/spam_classifier.pkl'):
    return pickle.load(open(path,'rb'))
