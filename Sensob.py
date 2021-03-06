# -*- coding: utf-8 -*-

from camera import *
from ultrasonic import *
from irproximity_sensor import *
from reflectance_sensors import *

class Sensob:

    def __init__(self):
        self.sensors = []
        self.value = None

    def update(self):
        # Fetch relevant sensor value(s) and convert them into one value
        return

    def get_value(self):
        return self.value

    def reset(self):
        for sensor in self.sensors:
            sensor.reset()

