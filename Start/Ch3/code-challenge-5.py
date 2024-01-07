# Python code​​​​​​‌​‌​‌​​‌‌‌​​​‌​‌​​‌‌‌​​‌‌ below
# Use print("messages...") to debug your solution.

show_expected_result = False
show_hints = False

def count_days():
    import json
    import statistics

    # open the sample weather data file and use the json module to load and parse it
    with open("deps/sample-weather-history.json", "r") as weatherfile:
        weatherdata = json.load(weatherfile)

    # select the days from the summer months from all the years
    winters = ["-12-","-01-","-02-"]
    winter_months = [d for d in weatherdata if any([month in d['date'] for month in winters])]

    def average_temp(day):
        return (day['tmin'] + day['tmax']) / 2

    avg_temps = [average_temp(d) for d in winter_months]
    mean_temp = statistics.mean(avg_temps)
    upper_outlier = mean_temp + (statistics.stdev(avg_temps) * 2)
    max_outliers = [t for t in avg_temps if t >= upper_outlier]

    return len(max_outliers)
