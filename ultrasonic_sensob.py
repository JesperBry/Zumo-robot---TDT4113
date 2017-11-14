# -*- coding: utf-8 -*-

from ultrasonic import Ultrasonic
from Sensob import Sensob

class Ultrasonic_sensob(Sensob):

    def __init__(self):
        super(Ultrasonic_sensob, self).__init__()
        self.sensor = Ultrasonic()

    def update(self):
        self.value = self.sensors.update()
        print('Values: ', self.value)