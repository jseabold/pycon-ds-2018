from sklearn.feature_extraction.text import CountVectorizer
from load_data import dta


dta = dta.drop(["violations"], axis='columns').join(
    dta.violations.str.split("|", expand=True)
    .unstack()
    .dropna()
    .str.strip()
    .reset_index(level=0, drop=True)
    .to_frame()
    .rename(columns={0: 'violations'}),
    how='right'
)

count_vectorizer = CountVectorizer(stop_words='english')
count_vectorizer.fit(dta.violations)
count_matrix = count_vectorizer.transform(dta.violations)


top_idx = count_matrix.sum(0).argmax()
count_vectorizer.get_feature_names()[top_idx]
