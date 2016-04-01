from kivy.uix.button import Button
from kivy.uix.button import ButtonBehavior
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from custom.widgets.picture_button import PicturedButton
from custom.motor import Motor
from __root__ import *


class BinaryAdjustment(GridLayout):
    def __init__(self, title, positive_callback, negative_callback, positive_pin, negative_pin, **kwargs):
        super(BinaryAdjustment, self).__init__(rows=2, **kwargs)
        self.padding = 10
        self.add_widget(Label(text=title))

        self.motor = Motor(positive_pin, negative_pin)

        buttons = GridLayout(cols=2)
        buttons.padding = 10

        plus_button = PicturedButton(icon_path('plus.png'), positive_callback)
        plus_button.id = title + ' plus button'
        plus_button.bind(on_press=self.motor.clockwise())
        buttons.add_widget(plus_button)

        minus_button = PicturedButton(icon_path('minus.png'), negative_callback)
        minus_button.id = title + ' minus button'
        minus_button.bind(on_press=self.motor.counter_clockwise())
        buttons.add_widget(minus_button)

        self.add_widget(buttons)

