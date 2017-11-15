# -*- coding: utf-8 -*-

from ultrasonic import Ultrasonic
from Sensob import Sensob

class Ultrasonic_sensob(Sensob):

    def __init__(self):
        super(Ultrasonic_sensob, self).__init__()
        self.sensors = [Ultrasonic()]

    def update(self):
        for sensor in self.sensors:
            sensor.update()
        self.value = self.sensors[0].value
        return self.value
