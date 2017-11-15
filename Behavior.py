
class Behavior:
    def __init__(self, bbcon):
        self.bbcon = bbcon          # Settes på init eller egen initialize metode
        self.senobs = []            # Skal fylles av subklasse
        self.motobs = []            # Skal fylles av subklasse
        self.active_flag = False    # Oppdateres hvert tick
        self.halt_request = False   # Oppdateres hvert tick
        self.priority = 1           # Skal fylles av subklasse
        self.match_degree = 0       # Oppdateres hvert tick
        self.weight = 0             # Oppdateres hvert tick
        self.motor_recommendations = None

    def consider_activation(self):  # Skal implementeres av subklasse
        return

    def consider_deactivation(self):# Skal implementeres av subklasse
        return

    def sense_and_act(self):        # Skal implementeres av subklasse
        return

    def update(self):               # Skal kalles hvert tick, eneste metode som skal kalles utenfra
        self.consider_deactivation() if self.active_flag else self.consider_deactivation()

        self.sense_and_act()

        self.weight = self.priority * self.match_degree

