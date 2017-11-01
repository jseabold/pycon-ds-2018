import numpy as np
import pandas as pd


def float_to_zip(zip_code):
    # convert from the string in the file to a float
    try:
        zip_code = float(zip_code)
    except ValueError:  # some of them are empty
        return np.nan

    # 0 makes sure to left-pad with zero
    # zip codes have 5 digits
    # .0 means, we don't want anything after the decimal
    # f is for float
    zip_code = "{:05.0f}".format(zip_code)
    return zip_code


dta = pd.read_csv(
    "data/health_inspection_chi.csv",
    index_col='inspection_id',
    parse_dates=['inspection_date'],
    converters={
        'zip': float_to_zip
    },
    usecols=lambda col: col != 'location',
    dtype={
        'results': 'category',
        'risk': 'category',
        'inspection_type': 'category',
        'facility_type': 'category'
    }
)
