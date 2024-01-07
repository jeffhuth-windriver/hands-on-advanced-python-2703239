# Python code​​​​​​‌​‌​‌​​‌‌‌​​​‌​‌​​​‌​​‌‌‌ below
# Use print("messages...") to debug your solution.

import json
import random

show_expected_result = False
show_hints = False

def select_days(year, month):
    # Your code goes here
    with open("deps/sample-weather-history.json", "r") as weatherfile:
        weatherdata = json.load(weatherfile)

    year_month = f"{year}-{month}"
    print(year_month)
    month_data = list(filter(lambda d: d['date'][0:7] == year_month, weatherdata))

    rnd_days = random.sample(month_data, k=5)

    # return the list
    return rnd_days
