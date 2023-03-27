import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="localPass",
    database="testDB"
)

myCursor = mydb.cursor()
myCursor.execute("DROP TABLE IF EXISTS temperatures")
myCursor.execute("DROP TABLE IF EXISTS places")

myCursor.execute("CREATE TABLE places (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255))")
myCursor.execute(
    "CREATE TABLE temperatures (id INT AUTO_INCREMENT, placeID INT, date DATE, minTemp FLOAT, maxTemp FLOAT, PRIMARY KEY (id), FOREIGN KEY (placeId) REFERENCES places(id))")

myCursor.execute("SHOW TABLES")

for x in myCursor:
    print(x)

print("")

# calling execute() method without the second parameter - the SQL query directly contains the value to insert
myCursor.execute("INSERT INTO places (name) VALUES ('Veszprém')")
mydb.commit()

# calling execute() method with the second parameter - the SQL query does not contain the value to insert
query = "INSERT INTO places (name) VALUES (%s)"
value = ("Sopron",)
myCursor.execute(query, value)
mydb.commit()
query = "INSERT INTO places (name) VALUES (%s)"
value = ("Békéscsaba",)
myCursor.execute(query, value)
mydb.commit()

# calling executemany() to executing an SQL query multiple times, with different data
query = "INSERT INTO temperatures (placeID,date,minTemp,maxTemp) VALUES (%s,%s,%s,%s)"
values = [
    (1, "2023-01-09", 9, 9.4),
    (2, "2023-01-09", 2.6, 7.5),
    (3, "2023-01-09", 6.85, 8.64),
    (1, "2023-01-10", 4, 6.8),
    (2, "2023-01-10", 3.1, 5.6),
    (3, "2023-01-10", 4.76, 6.34)
]
myCursor.executemany(query, values)
mydb.commit()


def display(row):
    query = "SELECT name FROM places WHERE id=%s"
    cityID = (row[1],)
    myCursor.execute(query, cityID)
    city = myCursor.fetchone()[0]
    print(
        f"In {city} on day {row[2]:%Y-%m-%d} the minimum temperature was {row[3]} °C and the maximum temperature was {row[4]} °C.")


myCursor.execute("SELECT * FROM temperatures")
tempRecords = myCursor.fetchall()
print(f"The temperatures table contains {myCursor.rowcount} record(s):")
for row in tempRecords:
    display(row)

print("")

myCursor.execute("UPDATE places SET name='Veszprém city centre' WHERE name='Veszprém'")
mydb.commit()
myCursor.execute("SELECT * FROM temperatures")
tempRecords = myCursor.fetchall()
for row in tempRecords:
    display(row)
