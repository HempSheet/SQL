import mysql.connector
import mysql

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Rootpass12345',
    database='testdbSQL',
)

my_cursor = mydb.cursor()

my_cursor.execute("INSERT INTO users (id, username, password, is_active, balance)"
                  "VALUES (1, 'Marly', '12345', '1', '2000')")

my_cursor.execute("INSERT INTO Session (id, user_id, created_date, expired_date, data)"
                  "VALUES (1, 1, '3:04:20', '3:10:20', 'today')")

my_cursor.execute("INSERT INTO transaction (id, created_date, type_transaction, amount, user_id)"
                  "VALUES (1, '3:04:20', 2, 1, 1)")


#-----selects for db-----
"""вибірка всіх транзакцій по користувачу"""
my_cursor.execute("SELECT user_id FROM Transaction")
row = my_cursor.fetchone()
print(row)

