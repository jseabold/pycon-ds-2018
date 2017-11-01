import numpy as np

y = np.random.poisson(lam=5, size=1000)
bins = np.bincount(y)

print(bins.argmax())
