from motors import Motors
from config import Config

class Motob:
    def __init__(self, motors):
        self.motors = motors
        self.values = []

    def update(self, values):
        self.values = values
        print("Motob value", self.values)
        self.operationalize()

    def operationalize(self):
        m = Motors()
        m.set_value(self.values, Config['motorDuration'])
        #for i in range(len(self.motors)):
        #    self.motors[i].set_value(self.values, Config['motorDuration'])
