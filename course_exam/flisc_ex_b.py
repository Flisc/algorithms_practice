import csv
from datetime import datetime
import collections

import mysql.connector

mydb = mysql.connector.connect(
    host="sql7.freemysqlhosting.net",
    user="sql7588068",
    password="1hABITXwHw",
    database="sql7588068"
)
myCursor = mydb.cursor()


def formatDate(str_date):
    if len(str_date) == 8:
        date_format = '%Y%m%d'
        date_object = datetime.strptime(str_date, date_format)
        return date_object


def setup_yearly_data(input):
    for date, temperature_str in input.items():
        year = date.year
        temperature = float(temperature_str)
        data_by_year[year].append(temperature)


def setup_monthly_data(setup_monthly_data):
    result = {}
    for date, value in temp_by_date.items():
        year = date.year
        month = date.month
        if year not in result:
            result[year] = {month: {'max': float(value), 'min': float(value)}}
        elif month not in result[year]:
            result[year][month] = {'max': float(value), 'min': float(value)}
        else:
            result[year][month]['max'] = max(result[year][month]['max'], float(value))
            result[year][month]['min'] = min(result[year][month]['min'], float(value))

    return result


data_by_year = {i: [] for i in range(1901, 2022)}


def calculate_daily_by_year():
    yearly_temperatures = {}
    for year, temperatures in data_by_year.items():
        yearly_temperatures[year] = {
            'highest': max(temperatures),
            'lowest': min(temperatures),
            'average': sum(temperatures) / len(temperatures)
        }
    return yearly_temperatures


def setup_db_tables():
    myCursor.execute("DROP TABLE IF EXISTS flisc_month_temperatures")
    myCursor.execute("DROP TABLE IF EXISTS flisc_year_temperatures")
    myCursor.execute(
        "CREATE TABLE flisc_year_temperatures ( id INT AUTO_INCREMENT PRIMARY KEY, year VARCHAR(10), daily_lowest double, daily_highest double, daily_average double) ENGINE = InnoDB")
    mydb.commit()
    myCursor.execute("""CREATE TABLE flisc_month_temperatures
(
    id              INT AUTO_INCREMENT PRIMARY KEY,
    year_id         INT,
    month           INT,
    lowest_temp  double,
    highest_temp double,
    FOREIGN KEY (year_id) REFERENCES flisc_year_temperatures (id)
) ENGINE = InnoDB""")
    mydb.commit()


def save_data_to_db_table1(yearly_temperatures):
    query = 'INSERT INTO flisc_year_temperatures(year, daily_lowest, daily_highest, daily_average) VALUES (%s, %s , %s, %s)'
    values = [
        (k, v['lowest'], v['highest'], v['average']) for k, v in yearly_temperatures.items()
    ]
    myCursor.executemany(query, values)
    mydb.commit()


def save_data_to_db_table2(monthly_data, year_db_data, values_table_2):
    query = 'INSERT INTO flisc_month_temperatures(year_id, month, lowest_temp , highest_temp) VALUES (%s, %s , %s, %s)'
    myCursor.executemany(query, values_table_2)
    mydb.commit()


def show_detailed_data():
    month_name = input("Details for month: ")
    number_by_month = {
        'January': 1,
        'February': 2,
        'March': 3,
        'April': 4,
        'May': 5,
        'June': 6,
        'July': 7,
        'August': 8,
        'September': 9,
        'October': 10,
        'November': 11,
        'December': 12
    }
    query = """
    select year, month, lowest_temp as lowest_per_month, highest_temp as highest_per_month, daily_lowest, daily_highest, daily_average
    from flisc_month_temperatures fmt
    join  flisc_year_temperatures fyt on fmt.year_id = fyt.id
    where month = %s
    """
    monthID = (number_by_month[month_name],)
    myCursor.execute(query, monthID)
    details = myCursor.fetchall()
    for row in details:
        print(
            f"Year: {row[0]}, Month: {month_name}, Lowest/month: {row[2]}, highest/month: {row[3]}, daily/min: {row[4]}, daily/max: {row[5]}, daily/avg: {row[6]}")


with open('t_o_Budapest_19012021.csv', 'r') as file:
    reader = csv.reader(file)
    temp_by_date = {}
    for i, row in enumerate(reader):
        if i != 0:
            temp_by_date[formatDate(row[0].split(';')[0])] = row[0].split(';')[1]

setup_yearly_data(temp_by_date)
yearly_temperatures = calculate_daily_by_year()
setup_db_tables()
save_data_to_db_table1(yearly_temperatures)

monthly_data = setup_monthly_data(temp_by_date)
myCursor.execute(" SELECT id, year FROM flisc_year_temperatures")
year_db_data = myCursor.fetchall()
values_table_2 = []
for year_db in year_db_data:
    month_data = monthly_data[int(year_db[1])]
    for month, temps in month_data.items():
        values_table_2.append(
            (year_db[0], month, temps['min'], temps['max'])
        )
save_data_to_db_table2(monthly_data, year_db_data, values_table_2)
show_detailed_data()
