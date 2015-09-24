#!/usr/bin/env python3

import mysql.connector
from mysql.connector import Error
import getpass
 
 
def connect():
    """ Connect to MySQL database """
    try:
        conn = mysql.connector.connect(host='Write here', #SERVER ADDRESS
                                       database='Write here', # DEFAULT DATABASE
                                       user=input('Please enter username: '), # USERNAME prompt
                                       password=getpass.getpass('Please enter password: ')) # PASSWORD prompt
        if conn.is_connected():
            print('Connected to MySQL database')
 
    except Error as e:
        print(e)
 
    finally:
        conn.close()
 
 
if __name__ == '__main__':
    connect()
