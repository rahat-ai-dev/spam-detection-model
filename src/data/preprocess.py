import re
import nltk
nltk.download('stopwords',quiet=True)
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

stemmer=PorterStemmer()
stop_words=set(stopwords.words('english'))

def clean_text(text):
    text=text.lower()
    text=re.sub(r'[^a-z\s]','',text)
    words=text.split()
    words=[stemmer.stem(w) for w in words if w not in stop_words]
    return' '.join(words)

def preprocess_dataframe(df):
    df=df.copy()
    df['clean_message']=df['message'].apply(clean_text)
    df['label_num']=df['label'].map({'spam':1,'ham':0})
    return df
