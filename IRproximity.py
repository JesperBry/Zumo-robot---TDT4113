# -*- coding: utf-8 -*-

from Sensob import Sensob
from irproximity_sensor import IRProximitySensor

class IRProximity_sensob(Sensob):

    def __init__(self):
        super(IRProximity_sensob, self).__init__()
        self.sensors = IRProximitySensor()

    def update(self):
        self.value = self.sensors.update()
        print("IRProximity:", self.value)