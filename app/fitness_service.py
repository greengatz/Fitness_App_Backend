from workout import Workout

class FitnessService(object):
  def __init__(self, repo):
    print("instantiating service")
    self.fitness_repository = repo

  def validate_and_save_workout(self, workout):
    try:
      validated_workout = Workout(workout)
      result = self.fitness_repository.store_workout(validated_workout)
      return '', result
    except AttributeError as err:
      return str(err), 400

