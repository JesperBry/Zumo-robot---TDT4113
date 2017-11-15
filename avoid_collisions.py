import Behavior
from config import Config


class Avoid_collisions(Behavior.Behavior):
    def __init__(self, distance, ir):
        super(Avoid_collisions, self).__init__(None)
        self.sensobs = [distance, ir]

        self.priority = Config['collisionPri']

    def consider_deactivation(self):
        self.active_flag = True

    def consider_activation(self):
        self.active_flag = True

    def sense_and_act(self):
        dist = self.sensobs[0].get_value()

        reflect = self.sensobs[1].get_value()

        self.match_degree = 0
        self.motor_recommendations = None

        if reflect > Config['reflectThr'] or dist < Config['minDist']:
            self.match_degree = 1
            self.motor_recommendations = Config['J_turn']


