import RPi.GPIO as io


class Motor(object):
    def __init__(self, positive_pin, negative_pin):
        io.setmode(io.BCM)

        super(Motor, self).__init__()
        self.positive_pin = positive_pin
        self.negative_pin = negative_pin

        if self.positive_pin != self.negative_pin:
            io.setup(self.positive_pin, io.OUT)
            io.setup(self.negative_pin, io.OUT)

    def clockwise(self, button):
        if self.positive_pin != self.negative_pin:
            io.output(self.positive_pin, True)
            io.output(self.negative_pin, False)

    def counter_clockwise(self, button):
        if self.positive_pin != self.negative_pin:
            io.output(self.positive_pin, False)
            io.output(self.negative_pin, True)

    def stop(self, button):
        if self.positive_pin != self.negative_pin:
            io.output(self.positive_pin, False)
            io.output(self.negative_pin, False)