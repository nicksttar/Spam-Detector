import pandas as pd
from joblib import load
from sklearn.feature_extraction.text import TfidfVectorizer

# Load Vectorizer and df
vectorizer = TfidfVectorizer(stop_words='english')
X = pd.read_csv('X_to_vector.csv')
X = X['Message'].squeeze()  # It needs to be because we need ser but read.csv return df
X_vector_scale = vectorizer.fit_transform(X)

# Load model
model = load('spam_filter.joblib')

# Spam detect function
def is_spam(message, proba=False):

    message = vectorizer.transform([message])

    prediction = model.predict(message)[0]

    if proba==True:
        proba = model.predict_proba(message)
        return f'Class: {prediction.upper()}\nProbability: {round(proba[0][1]*100, 3)}'
    return prediction.upper()


message = input("Write message: ")
result = is_spam(message, proba=True)
print(result)
