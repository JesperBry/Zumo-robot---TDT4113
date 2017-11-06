# -*- coding: utf-8 -*-

class BBCON:

    def __init__(self):
        self.behaviors = []
        self.active-behaviors = []
        self.sensobs = []
        self.motobs = []
        self.arbitrator = []

    def add_behavior(self, behavior):
        self.behaviors.append(behavior)

    def add_sensob(self, sensob):
        self.sensobs.append(sensob)

    def activate_behavior(self acBehavior):
        self.activate_behavior.append(acBehavior)

    def deactive_behavior(self, behavior):
        self.behaviors.pop(behavior)

    def run_one_timestep(self):
        # Update all sensobs
        # Update all sensobs
        # Invoke the arbitrator by calling arbitrator.choose action
        # Update the motobs based on these motor recommendations
        # Wait
        # Reset the sensobs
