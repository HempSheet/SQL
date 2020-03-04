import mysql.connector
import mysql

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Rootpass12345',
    database='testdbSQL',
)

my_cursor = mydb.cursor()

#------make testdb in db-----
#my_cursor.execute("CREATE DATABASE testdbSQL")

#my_cursor.execute("SHOW DATABASES")
#for db in my_cursor:
#    print(db)


#-----make tables-----
my_cursor.execute("DROP TABLE IF EXISTS users")
my_cursor.execute("CREATE TABLE users ("
                  "id INTEGER, "
                  "username VARCHAR(50), "
                  "password VARCHAR(255), "
                  "is_active BOOL, "
                  "balance BIGINT, "
                  "PRIMARY KEY (id))")

my_cursor.execute("DROP TABLE IF EXISTS Session")
my_cursor.execute("CREATE TABLE Session ("
                  "id VARCHAR(10), "
                  "user_id INTEGER(10), "
                  "created_date TIME, "
                  "expired_date TIME, "
                  "data TEXT(200), "
                  "ip VARCHAR(10), "
                  "user_agent VARCHAR(150), "
                  "PRIMARY KEY (id), "
                  "FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE)")

my_cursor.execute("DROP TABLE IF EXISTS Transaction")
my_cursor.execute("CREATE TABLE Transaction ("
                  "id INTEGER(10), "
                  "created_date TIME, "
                  "type_transaction SMALLINT, "
                  "amount BIGINT, "
                  "user_id INTEGER(10), "
                  "PRIMARY KEY (id), "
                  "FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE)")
my_cursor.execute("SHOW TABLES")

for table in my_cursor:
    print(table[0])


#-----selects for db-----
my_cursor.execute("SELECT* FROM Session")
row = my_cursor.fetchone()

print(row)
