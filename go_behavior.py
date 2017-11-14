# -*- coding: utf-8 -*-

from Behavior import *
from config import Config

class Go(Behavior):

    def __init__(self):
        super(Go, self).__init__(None)

    def consider_activation(self):
        self.active_flag = True

    def consider_deactivation(self):
        self.active_flag = True

    def sense_and_act(self):
        self.match_degree = 1
        self.motor_recommendations = Config['forward']