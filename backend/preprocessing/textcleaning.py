import pandas as pd 
import re 

df = pd.read_csv('./combined_data.csv')

def clean_text(text):
    text = text.lower()  # lowercase
    text = re.sub(r"http\S+|www\S+|https\S+", '', text)  # remove URLs
    text = re.sub(r"<.*?>", '', text)  # remove HTML tags
    text = re.sub(r"[^a-z\s]", '', text)  # remove special chars, punctuation, numbers
    text = re.sub(r"\s+", " ", text).strip()  # remove extra whitespace
    return text

# overwrite the same column
df['text'] = df['text'].apply(clean_text)