import pandas as pd

df = pd.read_csv('./combined_data.csv')

# Drop empty/null rows
df = df.dropna(subset=['text'])

# Ensure all entries in 'text' column are strings and standardized
df['text'] = df['text'].astype(str).str.encode('utf-8', 'ignore').str.decode('utf-8')