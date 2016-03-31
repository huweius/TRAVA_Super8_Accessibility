from kivy.uix.button import ButtonBehavior
from kivy.uix.image import Image

class PicturedButton(ButtonBehavior, Image):
    def __init__(self, source):
        Image.__init__(self, source=source)
        ButtonBehavior.__init__(self)

