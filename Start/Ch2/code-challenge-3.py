# Python code​​​​​​‌​‌​‌​​‌‌‌​​​‌​​‌​​​‌​‌​​ below
# Use print("messages...") to debug your solution.

show_expected_result = True
show_hints = False

import json
from functools import reduce

def crappy_day(acc, elem):
    ifnone = lambda x: 0 if x is None else x
    score = lambda s: (ifnone(s['awnd']) + (10 * ifnone(s['prcp'])) + ifnone(s['tmax']))/3

    score_elem = score(elem)
    score_acc = score(acc)

    if score_elem > score_acc:
        return elem
    return acc

def miserable_day():
    with open("deps/sample-weather-history.json", "r") as weatherfile:
        weatherdata = json.load(weatherfile)
    
    # Your code goes here
    start_val = {
        "date": "1900-01-01",
        "tmin": 0,
        "tmax": 0,
        "prcp": 0.0,
        "snow": 0.0,
        "snwd": 0.0,
        "awnd": 0.0
    }

    result = reduce(crappy_day, weatherdata, start_val)
    print(result)

    return result
