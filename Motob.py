from motors import Motors

class Motob:
    def __init__(self, motors):
        self.motors = motors
        self.values = []

    def update(self, values):
        self.values = values
        print("motob value", self.values)
        self.operationalize()

    def operationalize(self):
        for i in range(len(self.motors)):
            self.motors[i].set_value(self.values)
