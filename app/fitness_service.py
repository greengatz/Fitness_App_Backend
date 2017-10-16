import json
from flask import request

from app import app
from app import fitness_repo

@app.route('/')
@app.route('/index')
def baseReturn():
    return "success"

@app.route('/workouts', methods=['PUT'])
def putRoute():
    result = fitness_repo.store_workout(request.json)
    return '', result