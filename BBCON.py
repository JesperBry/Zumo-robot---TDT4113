# -*- coding: utf-8 -*-

from Motob import *
from Arbitrator import *
from Behavior import *
from Sensob import *
from robodemo import dancer

class BBCON:

    def __init__(self):
        self.behaviors = []
        self.active_behaviors = []
        self.sensobs = []
        self.motobs = Motob()
        self.arbitrator = None
        self.controller()

    def add_behavior(self, behavior):
        if behavior not in self.behaviors:
            self.behaviors.append(behavior)

    def add_sensob(self, sensob):
        if sensob not in self.sensobs:
            self.sensobs.append(sensob)

    def activate_behavior(self, behavior):
        if behavior in self.behaviors:
            self.active_behaviors.append(behavior)

    def deactivate_behavior(self, behavior):
        if behavior in self.activate_behavior:
            self.active_behaviors.remove(behavior)

    def run_one_timestep(self):

        # Update all sensobs

        """
        for sensor_object in self.sensobs:
            sensor_object.update()

        # Update all behaviors

        for ac_behavior in self.active_behaviors:
            if not ac_behavior.active_flag:
                self.deactivate_behavior(ac_behavior)

        for behavior in self.behaviors:
            behavior.update()
            if behavior.active_flag:
                self.activate_behavior(behavior)
        """

        # Invoke the arbitrator by calling arbitrator.choose action

        #action = self.arbitrator.choose_behavior(self.behaviors)

        dancer()

        # Update the motobs based on these motor recommendations
        # Wait



        # Reset the sensobs

    def controller(self):
        i = 30
        while i > 0:
            self.run_one_timestep()
            sleep(1)
            i -= 1