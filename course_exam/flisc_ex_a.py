import csv
from datetime import datetime
import collections


def formatDate(str_date):
    if len(str_date) == 8:
        date_format = '%Y%m%d'
        date_object = datetime.strptime(str_date, date_format)
        return date_object


def calculate_temp_results(sorted_items):
    first_date = next(iter(sorted_items.items()))
    last_date = collections.OrderedDict(sorted_items.items()).popitem(last=True)
    highest_diff = abs(float(first_date[1][1]) - float(last_date[1][1]))
    sum_of_days = 0
    for value in sorted_items.values():
        second_value = float(value[1])
        sum_of_days += second_value
    avg_temp = sum_of_days / (len(sorted_items.values()))
    return {
        'DIFF_DATE_START': first_date[1][0],
        'DIFF_DATE_END': last_date[1][0],
        'HIGH_DIFF': highest_diff,
        'AVG_TEMP': avg_temp
    }


def print_results(results):
    print(
        f"Highest diff temperature: {results['HIGH_DIFF']} , recorded between dates: [{results['DIFF_DATE_START']}] - [{results['DIFF_DATE_END']}]")
    print(f"Average temperature: {results['AVG_TEMP']}")


n = int(input("Insert desired number of days to calculate temperatures: "))
with open('t_o_Budapest_19012021.csv', 'r') as file:
    reader = csv.reader(file)
    temp_by_day = {}
    for i, row in enumerate(reader):
        if i != 0 and i <= n:
            temp_by_day[i] = [formatDate(row[0].split(';')[0]), row[0].split(';')[1]]
    sorted_temps = sorted(float(str(t[1]).strip()) for t in temp_by_day.values())
    sorted_days_with_temp = dict(sorted(temp_by_day.items(), key=lambda x: float(x[1][1])))

result = calculate_temp_results(sorted_days_with_temp)
print(
    f"Timeframe for results : [{sorted_days_with_temp[1][0].strftime('%Y-%m-%d')}] - [{sorted_days_with_temp[n][0].strftime('%Y-%m-%d')}]")
print_results(result)
