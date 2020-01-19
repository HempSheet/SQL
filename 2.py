import psycopg2
conn = psycopg2.connect(dbname="testdb",
                        user="root",
                        password="Rootpass12345",
                        host='localhost'
                        )
cursor = conn.cursor()

#----make tables----
#cursor.execute("CREATE TABLE users (name VARCHAR(255), email VARCHAR(255), age INTEGER(10), "
#                  "user_id INTEGER AUTO_INCREMENT PRIMARY KEY)")
#cursor.execute("SHOW TABLES")
#for table in cursor:
#    print(table[0])


#-----selects for db-----
cursor.execute("SELECT* FROM users")
row = cursor.fetchone()
print(row)
cursor.close()
