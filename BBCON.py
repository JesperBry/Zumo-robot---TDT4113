# -*- coding: utf-8 -*-

from Motob import Motob
from Sensob import *

class BBCON:

    def __init__(self):
        self.behaviors = []
        self.active_behaviors = []
        self.sensobs = []
        self.motobs = Motob()
        self.arbitrator = []

    def add_behavior(self, behavior):
        if behavior not in self.behaviors:
            self.behaviors.append(behavior)

    def add_sensob(self, sensob):
        if sensob not in self.sensobs:
            self.sensobs.append(sensob)

    def activate_behavior(self, behavior):
        if behavior in self.behaviors:
            self.active_behaviors.append(behavior)

    def deactive_behavior(self, behavior):
        if behavior in self.activate_behavior:
            self.active_behaviors.remove(behavior)

    def run_one_timestep(self):
        # Update all sensobs
        # Invoke the arbitrator by calling arbitrator.choose action
        # Update the motobs based on these motor recommendations
        # Wait
        # Reset the sensobs