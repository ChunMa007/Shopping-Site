import mysql.connector

myDatabase = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="fhel123",
    auth_plugin="mysql_native_password",
)

cursorObject = myDatabase.cursor()
cursorObject.execute("CREATE DATABASE puddle")

print("database created")