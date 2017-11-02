grouper = dta.groupby(dta.dba_name)
mcd = grouper.get_group("MCDONALD'S")


def relative_results(df):
    values = df.value_counts()
    return values['Fail'] / values['Pass']


relative_results(mcd.results)

# And we see McDonald's failed 50% as many inspections as it Passed.
