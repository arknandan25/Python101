#!/usr/bin/env python3
# from dataclasses import dataclass
#
# from dataclasses_jsonschema import JsonSchemaMixin
#
#
# @dataclass
# class X(JsonSchemaMixin):
#     "A 2D point"
#     x: str
#     y: str
#
# print(X('ewe', 'wewe'))

data = {
   "first_name": "Jonathan",
   "middle_name": None,
   "last_name": "Hsu",
   "family": {
      "mother": "Mary",
      "father": "Peter",
      "brother": "Charles",
      "sister": None,
      "eeee": [],
   },
    "tmp": {
        "a": None,
        "b": None,
    },
    "lol": {
        "jhund": {
            "sss": None,
            "uuu": "skdksnd",
        },
        "lll": None,
        "gggg": [1,2,3,4,5]
    }
}

from typing import Dict

def clean_null_terms(input_dict: Dict):
    """

    :param input_dict:
    :return:
    """
    clean = {}
    for k, v in input_dict.items():
        if isinstance(v, Dict):
            # import pdb
            # pdb.set_trace()
            nested = clean_null_terms(v)
            if len(nested.keys()) > 0:
                clean[k] = nested
        elif isinstance(v, list):
            clean[k] = v
        elif v is not None:
            clean[k] = v
    return clean
    # print(clean)

import json
print(json.dumps(clean_null_terms(data), indent=4))
