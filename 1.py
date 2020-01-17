import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Rootpass12345",
    database="testdb",
)

my_cursor = mydb.cursor()

#------make testdb in db-----
# my_cursor.execute("CREATE DATABASE testdb")

#my_cursor.execute("SHOW DATABASES")
#for db in my_cursor:
#    print(db)


#-----make tables-----
#my_cursor.execute("CREATE TABLE users (name VARCHAR(255), email VARCHAR(255), age INTEGER(10), "
#                  "user_id INTEGER AUTO_INCREMENT PRIMARY KEY)")
#my_cursor.execute("SHOW TABLES")
#for table in my_cursor:
#    print(table[0])

#-----insert into db-----
#sqlstuff = "INSERT INTO users (name, email, age) VALUES (%s, %s, %s)"
#record1 = ("John", "john@cooder.com", 40)

#my_cursor.execute(sqlstuff, record1)
#mydb.commit()

#-----selects for db-----
my_cursor.execute("SELECT* FROM users")
row = my_cursor.fetchone()
print(row)
