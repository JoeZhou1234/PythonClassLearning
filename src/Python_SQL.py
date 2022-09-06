# import libraries

import mysql.connector
from mysql.connector import Error
import pandas as pd


# Connect with MySQL Database
def create_server_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(host=host_name,
                                             user=user_name,
                                             password=user_password)
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")
    return connection


# Put our MySQL Terminal password and create the connection
pw = "Lead-138"
connection = create_server_connection("localhost", "root", pw)


# Create a database (Actually just executing whatever query you input on MySQL)
def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as err:
        print(f"Error: '{err}'")


# SQL query that creates a database called mysql_python
create_database_query = "CREATE DATABASE mysql_python"

# Executing the SQL query that creates a database called mysql_python
create_database(connection, create_database_query)


# Simpler version:

# import mysql.connector
# mydb = mysql.connector.connect(
#   host="localhost",
#   user="yourusername",
#   password="yourpassword",
#   database="mydatabase"
# )
# mycursor = mydb.cursor()
# mycursor.execute("query")


# When modifying tales in the database, make sure to include:

# mydb.commit()

