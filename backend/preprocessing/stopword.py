import nltk
from nltk.corpus import stopwords
import pandas as pd
nltk.download('stopwords')

stop_words = set(stopwords.words('english'))

df = pd.read_csv('./combined_data.csv')

def remove_stopwords(text):
    tokens = text.split()
    tokens = [word for word in tokens if word not in stop_words]
    return " ".join(tokens)

df['text'] = df['text'].apply(remove_stopwords)