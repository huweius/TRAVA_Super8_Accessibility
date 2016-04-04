from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label

from __root__ import *
from custom.movements.motor import Motor
from custom.widgets.picture_button import PicturedButton


class BinaryAdjustment(GridLayout):
    def __init__(self, title, positive_pin, negative_pin, **kwargs):
        super(BinaryAdjustment, self).__init__(rows=2, **kwargs)
        self.add_widget(Label(text=title))

        self.motor = Motor(title, positive_pin, negative_pin)

        buttons = GridLayout(cols=2)
        # buttons.padding = 10

        plus_button = PicturedButton(icon_path('plus.png'), self.motor.stop, self.motor.clockwise, size_hint=(1,1))
        plus_button.id = title + ' plus button'
        buttons.add_widget(plus_button)
        print 'Size of the plus button is %d x %d' % (plus_button.width, plus_button.height)

        minus_button = PicturedButton(icon_path('minus.png'), self.motor.stop, self.motor.counter_clockwise, size_hint=(1,1))
        minus_button.id = title + ' minus button'
        buttons.add_widget(minus_button)

        self.add_widget(buttons)

