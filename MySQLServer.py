import mysql.connector
from mysql.connector import Error
def create_database():
    connection = None
    cursor = None
    try:
        connection = mysql.connector.connect(
            host ='localhost',
            user = '',
            password = ''
        )
        if connection.isconnected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully")
    except Error as e:
        print(f"Error while connecting to MySQL: {e}")  
    finally:
        if cursor is not None and cursor.close is not None:
           cursor.close()
        if connection is not None and connection.isconnected():
            connection.close()
            print("MySQL connection is closed")
if __name__ == "__main__":
    create_database()