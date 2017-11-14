import Behavior, ultrasonic_sensob, IRproximity, camera_sensob
from config import Config


class Avoid_collisions(Behavior.Behavior):
    def __init__(self, distance=ultrasonic_sensob.Ultrasonic_sensob(), ir=IRproximity.IRProximity_sensob(), camera=camera_sensob.Camera_sensob()):
        super(Avoid_collisions, self).__init__(None)
        self.sensobs = [distance, ir, camera]

        self.priority = Config['collisionPri']

    def consider_deactivation(self):
        self.active_flag = True

    def consider_activation(self):
        self.active_flag = True

    def sense_and_act(self):
        dist = self.sensobs[0].get_value()

        ir = self.sensobs[1].get_value()

        if (ir[0] or ir[1]) or dist < Config['minDist']:
            self.match_degree = 1
            self.motor_recommendations = Config['J_turn']

        self.match_degree = 0
        self.motor_recommendations = None

