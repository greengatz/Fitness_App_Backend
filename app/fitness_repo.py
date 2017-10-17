# insert into workouts (distance, end_time, start_time)
# 	values (4.75, (TIMESTAMP '2017-10-16 18:30:00'), (TIMESTAMP '2017-10-16 17:45:00'));

class FitnessRepository(object):
  def __init__(self, connection):
    print("instantiating service")
    self.connection = connection

  # TODO - error check with a try catch for responses
  def store_workout(self, workout):
    cursor = self.connection.cursor()
    SQL = "INSERT INTO workouts (distance, end_time, start_time) VALUES (%s, TIMESTAMP %s, TIMESTAMP %s);"
    cursor.execute(SQL, (workout["distance"], workout["end_time"], workout["start_time"]))
    self.connection.commit()
    cursor.close()
    return 202
