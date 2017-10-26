import pandas as pd
import requests

# pull a small sample of the City of Chicago Health Inspection data

response = requests.get(
    "https://data.cityofchicago.org/resource/cwig-ma7x.json",
    params="$limit=25000"
)

dta = pd.read_json(response.content, orient='records')

dta.to_csv("./health_inspection_chi.csv", index=False)
dta.iloc[:1000].to_csv("./health_inspection_chi_sample.csv", index=False)
dta.iloc[:1000].to_json("./health_inspection_chi_sample.json",
                        orient='records', lines=True)
