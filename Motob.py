# -*- coding: utf-8 -*-

from motors import Motors

class Motob:

    def __init__(self):
        self.motor = Motors()
        self.value = None # Den nyeste motatte motor-recommendation
        # value på formen (L, 30, 1) = venstre, 30grader, full hastighet

    def update(self, motor_recommentation):
        self.value = motor_recommentation
        # Receive a new motor recommendation, load it into the value slot, and operationalize it.

    #TODO value tuppelen har et element med grader, men motorene krever duration, ikke degrees. Må kanskje konvertere fra grader til duration
    def operationalize(self):
        hva = self.value[0]
        hvordan = self.value[1]
        hastighet = self.value[2]
        if hva == 'F':
            self.motor.forward(hastighet)
        elif hva == 'B':
            self.motor.backward(hastighet)
        elif hva == 'L':
            self.motor.left(hastighet)
        elif hva == 'R':
            self.motor.right(hastighet)
        # Convert a motor recommendation into one or more motor settings, which are sent to the corresponding motor(s).
