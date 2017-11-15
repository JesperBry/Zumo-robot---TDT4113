import camera_sensob
from Behavior import Behavior
from config import Config


class StopSign(Behavior):
    def __init__(self, camera):
        super(StopSign, self).__init__(None)
        self.sensobs = [camera]

        self.priority = Config['stopSignPri']

        self.stopped = False

    def consider_deactivation(self):
        self.active_flag = True

    def consider_activation(self):
        self.active_flag = True

    def sense_and_act(self):
        rgb = self.sensobs[0].update()

        self.match_degree = 0
        self.motor_recommendations = None

        if self.stopped:
            self.match_degree = 1
            if rgb[1] > Config['grThr']:
                self.match_degree = 0
                self.stopped = False

        elif rgb[0] > Config['redThr']:
            self.stopped = True
            self.match_degree = 1
            self.motor_recommendations = Config['stop']


