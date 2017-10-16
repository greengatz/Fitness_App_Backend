from flask import Flask
import psycopg2
import sys

def connectToDb():
    # connect to db
    # TODO - don't actually print db credentials in log maybe?
    conn_string = "host='localhost' dbname='Pebble_Fitness_Dev' user='postgres' password='admin'"
    # print the connection string we will use to connect
    print("Connecting to database\n", conn_string)
    # get a connection, if a connect cannot be made an exception will be raised here
    return psycopg2.connect(conn_string)

# connect to the db
conn = connectToDb()

# start flask app
app = Flask(__name__)

from app import fitness_service