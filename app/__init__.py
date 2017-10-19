from flask import Flask
from flask import request
import psycopg2
import sys

from fitness_service import FitnessService
from fitness_repo import FitnessRepository

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

# instantiate service and repo
print("setting up service")
# repo is...
repo = FitnessRepository(conn)
# service is...
service = FitnessService(repo)

# start flask app
print("starting flask server...")
app = Flask(__name__)
print("setting up routes...")

# routes
@app.route('/')
@app.route('/index')
def baseReturn():
    return "success"

@app.route('/workouts', methods=['PUT'])
def save_workout_route():
    print(request.json)
    return service.validate_and_save_workout(request.json)

app.run(debug=True)