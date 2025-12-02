import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
import pickle

data = {
    "review": [
        "I loved the movie",
        "It was terrible and boring",
        "Amazing performance!",
        "Worst film ever",
        "It was okay, not great",
        "Really good storyline"
    ],
    "label": [
        "Positive",
        "Negative",
        "Positive",
        "Negative",
        "Neutral",
        "Positive"
    ]
}

df = pd.DataFrame(data)

model = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("clf", LogisticRegression())
])

model.fit(df["review"], df["label"])

with open("api/ml/model.pkl", "wb") as f:
    pickle.dump(model, f)
