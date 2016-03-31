from kivy.uix.button import Button
from kivy.uix.button import ButtonBehavior
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from custom.widgets.picture_button import PicturedButton
from __root__ import *


class BinaryAdjustment(GridLayout):
    def __init__(self, title, positive_callback, negative_callback):
        super(BinaryAdjustment, self).__init__(rows=2)
        self.padding = 10
        self.add_widget(Label(text=title))

        buttons = GridLayout(cols=2)
        buttons.padding = 10

        plus_button = PicturedButton(icon_path('plus.png'))
        plus_button.id = title + 'plus button'
        plus_button.bind(on_press = positive_callback)
        buttons.add_widget(plus_button)

        minus_button = PicturedButton(icon_path('minus.png'))
        minus_button.id = title + 'minus button'
        minus_button.bind(on_press = negative_callback)
        buttons.add_widget(minus_button)

        self.add_widget(buttons)

