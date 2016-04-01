from kivy.uix.button import ButtonBehavior
from kivy.uix.image import Image

class PicturedButton(ButtonBehavior, Image):
    def __init__(self, source, callback, **kwargs):
        Image.__init__(self, source=source, **kwargs)
        ButtonBehavior.__init__(self)
        self.bind(on_release=callback)

    def on_press(self):
        ButtonBehavior.on_press(self)
        self.opacity = 0.5

    def on_release(self):
        ButtonBehavior.on_release(self)
        print self.id + " is pressed. "
        self.opacity = 1

