# Let's be a little defensive/assertive and be sure there aren't any lower-case comments.

assert not dta.violations.str.contains("comments").any()

dta["comments"] = dta.violations.str.extract("(?<=Comments:)(.+)", expand=False)

has_comments = dta.comments.notnull()

X

tfidf_vect = TfidfVectorizer(
    stop_words='english',
    min_df=5,
    max_df=.95,
    token_pattern=r"(?u)\b[A-Za-z_][A-Za-z_]+\b"
)

X = tfidf_vect.fit_transform(dta.loc[has_comments].comments)

n_components = 10

svd = TruncatedSVD(
    n_components=n_components,
    random_state=0
)

X_reduced = svd.fit_transform(X)

X_norm = normalizer.fit_transform(X_reduced)

kmeans = KMeans()

kmeans = KMeans(n_clusters=n_clusters, random_state=0)

kmeans.fit(X_norm)

# Let's look at the top 6 words again

words = np.array(sorted(tfidf_vect.vocabulary_.keys()))

for i in range(n_components):
    idx = svd.components_[i].argsort()[::-1][:6]

    top_k = words[idx]
    print("{i}: {words}".format(i=i, words=top_k))

dta.loc[has_comments].violations[kmeans.labels_ == 0].head()
dta.loc[has_comments].violations[kmeans.labels_ == 1].head()
dta.loc[has_comments].violations[kmeans.labels_ == 2].head()
