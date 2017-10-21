from flask import Flask
from flask import request
import psycopg2
import sys
import config

from fitness_service import FitnessService
from fitness_repo import FitnessRepository

def connectToDb():
    conn_string = "host='{}' dbname='{}' user='{}' password='{}'"\
        .format(config.db_host, config.db_name, config.db_user, config.db_pass)
    print("Connecting to database {} at {} as {}\n".format(config.db_name, config.db_host, db_user))
    # get a connection, if a connect cannot be made an exception will be raised here
    return psycopg2.connect(conn_string)

# connect to the db
conn = connectToDb()

# instantiate service and repo
print("setting up service")
repo = FitnessRepository(conn)
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