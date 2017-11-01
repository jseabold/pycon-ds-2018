import json
from pprint import pprint


def remove_entry(record):
    try:
        del record['location']
    # this is called recursively on objects so not all have it
    except KeyError:
        pass

    return record


def parse_json(record):
    return json.loads(record, object_hook=remove_entry)


with open("data/health_inspection_chi_sample.json") as json_file:
    dta = [parse_json(line) for line in json_file]


pprint(dta[0])
