from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd

df = pd.read_csv('drugLabels.csv')
dfList = df.values.tolist()
print(dfList)
vectorizer = CountVectorizer(tokenizer=lambda doc: doc, lowercase=False)

X = vectorizer.fit_transform(dfList)
print(vectorizer.get_feature_names())

print(X.toarray())