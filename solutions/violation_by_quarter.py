quarter = (dta.inspection_date.dt.month - 1) // 3

quarter_size = dta.groupby((quarter, violation_num)).size()

axes = quarter_size.unstack(level=0).plot.bar(
    figsize=(14, 8),
)
