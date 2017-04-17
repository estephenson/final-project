#this code taken from: https://ruslanspivak.com/lsbaws-part1/

#sets up a very basic server that waits for GET requests
#and responds with the text "Hello, World!"

#you will probably have to download the mysql python connector: https://dev.mysql.com/doc/connector-python/en/connector-python-obtaining.html

#cannot get the database to work so might just work with pandas
#could work with sqlite since that's already available, but not sure
#how to make a db from a csv using sqlite

import socket
import pandas
import sqlite3
# import mysql.connector
# import peewee
# from peewee import *

# db = MySQLDatabase("johnnydb", user="john", passwd="megajohny")

HOST, PORT = "", 8888

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(1)

print "Serving HTTP on port %s ..." % PORT

# create an internal pandas "database"
database = pandas.read_csv("CCES_clean.csv")

while True:
    client_connection, client_address = listen_socket.accept()
    request = client_connection.recv(1024)
    print request

    if "GET" in request:
        html = open("index.html")
        html_data = html.read()
        html.close()
        http_response = """\
    HTTP/1.1 200 OK

    """
        http_response += html_data
        
    if "POST" in request:
        # send something else
        pass

    client_connection.sendall(http_response)
    client_connection.close()
