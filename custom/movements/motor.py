import sys
if sys.platform != 'win32':
    import RPi.GPIO as io


class Motor(object):
    def __init__(self, motor_id, positive_pin, negative_pin):
        super(Motor, self).__init__()

        if sys.platform != 'win32':
            io.setmode(io.BCM)
            self.id = motor_id
            self.positive_pin = positive_pin
            self.negative_pin = negative_pin

            if self.positive_pin != self.negative_pin:
                io.setup(self.positive_pin, io.OUT)
                io.setup(self.negative_pin, io.OUT)

    def clockwise(self, button):
        if sys.platform != 'win32':
            if self.positive_pin != self.negative_pin:
                print 'Turning clockwise'
                io.output(self.positive_pin, True)
                io.output(self.negative_pin, False)

    def counter_clockwise(self, button):
        if sys.platform != 'win32':
            if self.positive_pin != self.negative_pin:
                print 'Turning counterclockwise'
                io.output(self.positive_pin, False)
                io.output(self.negative_pin, True)

    def stop(self, button):
        if sys.platform != 'win32':
            if self.positive_pin != self.negative_pin:
                io.output(self.positive_pin, False)
                io.output(self.negative_pin, False)