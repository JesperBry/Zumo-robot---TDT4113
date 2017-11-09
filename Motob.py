# -*- coding: utf-8 -*-

from motors import Motors

class Motob:

    def __init__(self):
        self.motor = Motors()
        self.values = []

    def update(self):
        # Receive a new motor recommendation, load it into the value slot, and operationalize it.

    def operationalize(self):
        # Convert a motor recommendation into one or more motor settings, which are sent to the corresponding motor(s).
