# -*- coding: utf-8 -*-

from Sensob import Sensob
from camera import Camera

class Camera_sensob(Sensob):

    def __init__(self):
        super(Camera_sensob, self).__init__()
        self.sensors = Camera()

    def rgb(self, img):
        rgb = [0, 0, 0]

        for x in range(40, 80):
            for y in range(40, 50):
                band = img.getpixel((x, y))
                rgb[0] += band[0]
                rgb[1] += rgb[1]
                rgb[2] += rgb[2]

        tot = sum(rgb)
        rgb[0] = rgb[0] / tot
        rgb[1] = rgb[1] / tot
        rgb[2] = rgb[2] / tot

    def update(self):
        self.value = self.sensors.update()
        return self.rgb(self.value)