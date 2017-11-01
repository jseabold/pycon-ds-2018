from sklearn.pipeline import Pipeline
from sklearn.preprocessing.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import train_test_split


(violations_train, violations_test,
 y_train, y_test) = train_test_split(violations.values, y, test_size=.25)

estimator = Pipeline(steps=[
    ('tfidf', TfidfVectorizer(
        stop_words='english',
        min_df=50,
        max_df=.85,
        token_pattern=r"(?u)\b[A-Za-z_][A-Za-z_]+\b")),

    ('tsvd', TruncatedSVD(
        n_components=10,
        random_state=0)),

    ('rf', RandomForestClassifier(
        n_estimators=500,
        random_state=0))
])

estimator.fit(violations_train, y_train)

roc_auc_score(y_test, estimator.predict_proba(violations_test)[:, 1])
