import pandas as pd

pd.read_json(
    "data/health_inspection_chi_sample.json",
    orient="records",
    lines=True,
)
