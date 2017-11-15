# -*- coding: utf-8 -*-

from ultrasonic import Ultrasonic
from Sensob import Sensob

class Ultrasonic_sensob(Sensob):

    def __init__(self):
        super(Ultrasonic_sensob, self).__init__()
        self.sensors = Ultrasonic()

    def update(self):
        self.sensors.update()
        self.value = self.sensors.value
        return self.value
