import mysql.connector 
from mysql.connector import Error

# Módulo que establece la conexión a la base de datos MySQL.

def conex():
    try:
        myconn = mysql.connector.connect(host="localhost",
                                        user="root",
                                        passwd="",
                                        database="universidad")
        return myconn
    except Exception as ex:
        print("Error", ex)
        myconn.rollback()
