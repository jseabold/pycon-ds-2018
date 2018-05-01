import matplotlib.pyplot as plt

fig, axes = plt.subplots(nrows=2, figsize=(12, 10))

axes[0].hist(kmeans.labels_, bins=n_clusters)
axes[1].hist((dta.violations.str.extract("(\d+)(?=\.)", expand=False)
              .astype(int)
              .rank(method='dense')), bins=n_clusters);

# dta.violations[kmeans.labels_ == 0].iloc[:5].values
# dta.violations[kmeans.labels_ == 1].iloc[:5].values
# dta.violations[kmeans.labels_ == 2].iloc[:5].values
