import mysql.connector

database = mysql.connector.connect(
    host = 'localhost',
    user = 'person',
    passwd = 'password123'
)

cursorObject = database.cursor()

cursorObject.execute("CREATE DATABASE elderco")

print('All Done!')