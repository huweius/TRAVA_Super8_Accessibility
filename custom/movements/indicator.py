import RPi.GPIO as io


class Indicator(object):
    def __init__(self, indicator_id, indicator_pin):
        super(Indicator, self).__init__()
        self.id = indicator_id
        self.pin = indicator_pin

        io.setmode(io.BCM)

        io.setup(self.pin, io.OUT)

    def set_on(self, button):
        io.output(self.pin, True)

    def set_off(self):
        io.output(self.pin, False)