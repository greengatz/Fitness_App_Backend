from app import conn

# insert into workouts (distance, end_time, start_time)
# 	values (4.75, (TIMESTAMP '2017-10-16 18:30:00'), (TIMESTAMP '2017-10-16 17:45:00'));

# TODO - error check with a try catch for responses
def store_workout(workout):
    cursor = conn.cursor()
    SQL = "INSERT INTO workouts (distance, end_time, start_time) VALUES (%s, TIMESTAMP %s, TIMESTAMP %s);"
    cursor.execute(SQL, (workout["distance"], workout["end_time"], workout["start_time"]))
    conn.commit()
    cursor.close()
    return 202