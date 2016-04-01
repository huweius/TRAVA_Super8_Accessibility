from kivy.uix.button import ButtonBehavior
from kivy.uix.image import Image

from custom.callbacks.main_menu import default_callback


class PicturedButton(ButtonBehavior, Image):
    def __init__(self, source, on_release, on_press=default_callback, **kwargs):
        Image.__init__(self, source=source, **kwargs)
        ButtonBehavior.__init__(self)
        self.bind(on_press=on_press)
        self.bind(on_release=on_release)

    def on_press(self):
        ButtonBehavior.on_press(self)
        self.opacity = 0.5

    def on_release(self):
        ButtonBehavior.on_release(self)
        print self.id.__str__() + " is pressed. "
        self.opacity = 1

