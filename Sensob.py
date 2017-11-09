# -*- coding: utf-8 -*-

class Sensob:

    def __init__(self):
        self.sensors = []
        self.value = None

    def update(self):
        return

    def get_value(self):
        return self.value

    def reset(self):
        for sensor in self.sensors:
            sensor.reset()
