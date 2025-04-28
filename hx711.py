# hx711.py - HX711 module for MicroPython
import time
from machine import Pin

class HX711:
    def __init__(self, dout, pd_sck, gain=128):
        self.dout = dout
        self.pd_sck = pd_sck
        self.gain = gain
        self.offset = 0
        self.scale = 1
        self.pd_sck.init(Pin.OUT)
        self.dout.init(Pin.IN, pull=None)
        self.set_gain(gain)

    def set_gain(self, gain):
        if gain == 128:
            self.gain = 1
        elif gain == 64:
            self.gain = 3
        elif gain == 32:
            self.gain = 2
        self.read()

    def read(self):
        while self.dout.value() == 1:
            pass
        value = 0
        for _ in range(24 + self.gain):
            self.pd_sck.value(1)
            value = (value << 1) | self.dout.value()
            self.pd_sck.value(0)
        return value

    def get_weight(self, times=10):
        value = sum(self.read() for _ in range(times)) / times
        return (value - self.offset) / self.scale

    def tare(self, times=15):
        self.offset = sum(self.read() for _ in range(times)) / times

    def set_scale(self, scale):
        self.scale = scale
