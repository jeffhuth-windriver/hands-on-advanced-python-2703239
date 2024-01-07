# Python code​​​​​​‌​‌​‌​​‌‌‌​​​​‌‌​‌‌‌​‌‌​‌ below
# Use print("messages...") to debug your solution.
import json
import pprint


show_expected_result = False
show_hints = False

def is_crappyday(d):
    if (d['prcp'] > 0.7 or d['snow'] > 0.7):
        is_precip = True
    else:
        is_precip = False
    
    if (d['tmin'] + d['tmax'])/2 < 45:
        is_cold = True
    else:
        is_cold = False
    
    if (d['awnd'] is None or d['awnd'] <= 10.0):
        is_windy = False
    else:
        is_windy = True
    is_crappy = is_precip and is_cold and is_windy
    return is_crappy


def get_cold_windy_rainy_days():
    # your code goes here
    with open("deps/sample-weather-history.json", "r") as weatherfile:
        weatherdata = json.load(weatherfile)
    crappydays = list(filter(is_crappyday, weatherdata))

    return crappydays
