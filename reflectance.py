from Sensob import Sensob
from reflectance_sensors import ReflectanceSensors

class Reflectance(Sensob):

    def __init__(self):
        super(Reflectance, self).__init__()
        self.sensors = [ReflectanceSensors()]

    def update(self):
        self.value = self.sensors[0].update()
        print("Reflectance", self.value)
        return self.value