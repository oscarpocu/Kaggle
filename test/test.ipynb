import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from sklearn.calibration import CalibratedClassifierCV
from sklearn import metrics

df = pd.read_csv('website_classification.csv', header=0, delimiter=',')
df['category_id'] = df['Category'].factorize()[0]
df = df.drop_duplicates(subset='website_url').reset_index(drop=True)

tfidf = TfidfVectorizer(min_df=6, ngram_range=(1, 2), stop_words='english')
features = tfidf.fit_transform(df.cleaned_website_text).toarray()
labels = df.category_id

X_train, X_test, y_train, y_test,indices_train,indices_test = train_test_split(features, 
                                                               labels, 
                                                               df.index, test_size=0.3, 
                                                               random_state=1)

model = LinearSVC()
model.fit(X_train, y_train)

calibrated_svc = CalibratedClassifierCV(base_estimator=model, cv="prefit")
calibrated_svc.fit(X_train,y_train)
predicted = calibrated_svc.predict(X_test)
print("Test Accuracy LinearSVC: %.3f" % metrics.accuracy_score(y_test, predicted))
