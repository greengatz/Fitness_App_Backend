class FitnessService(object):
  def __init__(self, repo):
    print("instantiating service")
    self.fitness_repository = repo

  def validate_and_save_workout(self, workout):
    print("saving workout")
    result = self.fitness_repository.store_workout(workout)
    return '', result
