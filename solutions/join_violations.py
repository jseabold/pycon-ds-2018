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


dta.head()
