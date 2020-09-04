import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB

# reading the processed csv file
df = pd.read_csv("marathi_news_headlines", encoding="utf-8")
X = df.iloc[:, 0]
y = df.iloc[:, 1]
print(f"Labels = {pd.unique(y)}")
print(f"Total records =  {len(X)}")

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=3)

print(f"Total training records = {len(X_train)}")
print(f"Total testing records = {len(X_test)}")

# vectorizing the words in out dataset
vectorizer = TfidfVectorizer(max_features=1000, decode_error="ignore")
vectorizer.fit(X_train)
# print(f"Stop words = {vectorizer.stop_words_}")
# print(f"Vocabulary = {vectorizer.vocabulary_}")

# multinomial works well with sparse matrix
clf = MultinomialNB()
clf.fit(vectorizer.transform(X_train), y_train)

y_pred = clf.predict(vectorizer.transform(X_test))
print(f"Accuracy = {accuracy_score(y_test, y_pred) * 100}")
print(f"Classification report = {classification_report(y_test, y_pred)}")

# accuracies achieved
# MutiNomailNB : 88, 81, 79, 85, 82
