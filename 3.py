import mysql.connector
import mysql

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Rootpass12345",
    database="testdbSQL",
)

my_cursor = mydb.cursor()

#------make testdb in db-----
#my_cursor.execute("CREATE DATABASE testdbSQL")

#my_cursor.execute("SHOW DATABASES")
#for db in my_cursor:
#    print(db)


#-----make tables-----
#my_cursor.execute("CREATE TABLE users ("
#                  "id INTEGER, "
#                  "username VARCHAR(50), "
#                  "password VARCHAR(255), "
#                  "is_active BOOL, "
#                  "balance BIGINT)")
#my_cursor.execute("SHOW TABLES")

my_cursor.execute("DROP TAABLE IF EXIST Session, "
                  "CREATE TABLE Session ("
                  "id VARCHAR, "
                  "user_id INTEGER, "
                  "created_date TIME, "
                  "expired_date TIME, "
                  "data TEXT, "
                  "ip VARCHAR, "
                  "user_agent VARCHAR)")
my_cursor.execute("SHOW TABLES")

my_cursor.execute("DROP TAABLE IF EXIST Transaction, "
                  "CREATE TABLE Transaction ("
                  "id INTEGER, "
                  "created_date TIME, "
                  "type_transaction SMALINT, "
                  "amount BIGINT, "
                  "user_id INTEGER)")
my_cursor.execute("SHOW TABLES")

for table in my_cursor:
    print(table[0])


#-----selects for db-----
my_cursor.execute("SELECT* FROM users")
row = my_cursor.fetchone()

print(row)
