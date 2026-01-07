import pymysql

connector = pymysql.connect(
    host="localhost",
    user="newuser",
    password="root",
    port=3306

)
cursor=connector.cursor()

print("✅ MySQL connected successfully")