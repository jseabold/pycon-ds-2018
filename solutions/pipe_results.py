 (merged_visits.pipe(lambda df: df['Fail'].div(df['Pass']))
  .dropna()
  .sort_values(ascending=False))
