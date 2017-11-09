# -*- coding: utf-8 -*-

from Behavior import Behavior

class Arbitrator:

    def __init__(self):
        pass

    def choose_action(self, behaviors):
        winning_behavior = None
        max_weight = -1

        # Skal velge en "vinner behavior" og sende dens motor-recommendation til BBCON
        for behavior in behaviors:
            if behavior.weight > max_weight:
                max_weight = behavior.weight
                winning_behavior = behavior

        return winning_behavior.motor_recommendations, winning_behavior.halt_request