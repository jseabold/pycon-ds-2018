import numpy as np

words = np.array(sorted(tfidf_vect.vocabulary_.keys()))

# the words are lexicographically ordered

print(words[:15])


for i in range(n_components):
    idx = np.abs(svd.components_[i]).argsort()[::-1][:6]

    top_k = words[idx]
    print("{i}: {words}".format(i=i, words=top_k))
