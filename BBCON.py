# -*- coding: utf-8 -*-

from Motob import *
from Arbitrator import *
from Behavior import *
from Sensob import *
from robodemo import dancer
from zumo_button import ZumoButton

class BBCON():

    def __init__(self):
        self.behaviors = []
        self.active_behaviors = []
        self.sensobs = []
        self.motobs = [Motob([Motors()])]
        self.arbitrator = Arbitrator()

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
        for sensob in self.sensobs:
            sensob.update()

        # Update all behaviors
        for behavior in self.behaviors:
            behavior.update()
            if behavior.active_flag:
                self.activate_behavior(behavior)
            else:
                self.deactivate_behavior(behavior)

        # Invoke the arbitrator by calling arbitrator.choose action
        recommendations, stop = self.arbitrator.choose_action(self.active_behaviors)
        for i in range(len(self.motobs)):
            self.motobs[i].update(recommendations[i])

        # Wait
        time.sleep(0.5)

        # Reset the sensobs
        for sensob in self.sensobs:
            sensob.reset()


        #ZumoButton().wait_for_press() # er nødt til å ha med denne tydeligvis
        #m = Motors()
        #i = 10
        #while i > 0:
        #    m.set_value([0.2,-0.2], 1) # (speed,duration)
        #    #m.set_value([-0.2, 0.2], 1)
        #    m.forward(0.3, 1)
        #    i -= 1





    def controller(self):
        i = 30
        while i > 0:
            self.run_one_timestep()
            sleep(1)
            i -= 1