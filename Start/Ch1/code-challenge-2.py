# Python code​​​​​​‌​‌​‌​​‌‌‌​​​‌​​​​​​‌‌​‌‌ below
# Use print("messages...") to debug your solution.
import json

show_expected_result = False
show_hints = False

def get_temp_level(t1, t2):
    avg_t = (t1 + t2) / 2
    if avg_t <= 60:
        temp_level = 'cold'
    elif avg_t > 60 and avg_t < 80:
        temp_level = 'warm'
    elif avg_t >= 80:
        temp_level = 'hot'
    else:
        temp_level = 'invalid'
    return temp_level

def get_day_temp_descriptions():
    # Your code goes here
    with open("deps/sample-weather-history.json", "r") as weatherfile:
        weatherdata = json.load(weatherfile)
    
    tuple_data = list(map(lambda d:(d['date'], get_temp_level(d['tmax'], d['tmin'])), weatherdata))
    
    return tuple_data