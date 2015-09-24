#!/usr/bin/env python3

import mysql.connector
from mysql.connector import Error
import getpass
 
config = {
  'user': 'input("Please enter username: ")',               # USERNAME prompt
  'password': getpass.getpass('Please enter password: '),   # PASSWORD prompt
  'host': 'Write here',                                     # SERVER ADDRESS
  'database': 'Write here',                                 # DEFAULT DATABASE
}
 
def connect():
    """ Connect to MySQL database """
    try:
        cnx= mysql.connector.connect(**config) 
        if cnx.is_connected():
            print('Connected to MySQL database')
 
    except Error as e:
        print(e)
 
    finally:
        cnx.close()
 
 
if __name__ == '__main__':
    connect()
