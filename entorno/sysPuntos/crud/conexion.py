from os import system
system('cls')

import mysql.connector
from mysql.connector import Error
try:
    con = mysql.connector.connect(
        host='localhost',
        port='3306',
        user= 'root',
        password='finalmente.Admin$1',
        db='pruebaDjango1'
    )
    if con.is_connected():
        print('Conexión exitosa')
        cursor=con.cursor()
        cursor.execute('SELECT * FROM local')
        clientes = cursor.fetchall()
        for i in clientes:
            print(i)
except Error as e:
    print('Ocurrió una excepción => ',e)
finally:
    print('Conexión finalizada')