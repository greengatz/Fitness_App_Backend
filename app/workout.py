class Workout(object):
    def __init__(self, input):
        try:
            self.distance = input["distance"]
            self.start_time = input["start_time"]
            self.end_time = input["end_time"]
        except KeyError as err:
            raise AttributeError("attribute missing from given workout", err)