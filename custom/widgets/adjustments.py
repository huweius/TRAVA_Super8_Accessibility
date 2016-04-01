from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label

from __root__ import *
from custom.movements.motor import Motor
from custom.widgets.picture_button import PicturedButton


class BinaryAdjustment(GridLayout):
    def __init__(self, title, positive_pin, negative_pin, **kwargs):
        super(BinaryAdjustment, self).__init__(rows=2, **kwargs)
        self.padding = 10
        self.add_widget(Label(text=title))

        self.motor = Motor(title, positive_pin, negative_pin)

        buttons = GridLayout(cols=2)
        buttons.padding = 10

        plus_button = PicturedButton(icon_path('plus.png'), self.motor.stop, self.motor.clockwise)
        plus_button.id = title + ' plus button'
        buttons.add_widget(plus_button)

        minus_button = PicturedButton(icon_path('minus.png'), self.motor.stop, self.motor.counter_clockwise)
        minus_button.id = title + ' minus button'
        buttons.add_widget(minus_button)

        self.add_widget(buttons)

