from kivy.animation import Animation


class Animator(Animation):
    def __init__(self, **kw):
        super(Animator, self).__init__(**kw)
        self.original_size = (0, 0)
        self._duration = 0.5

    def fade_out (self, widget):
        self.original_size = (widget.width, widget.height)
        self.animated_properties['opacity'] = 0
        self.animated_properties['size'] = (10, 10)

    def fade_in (self, widget):
        self.animated_properties['size'] = self.original_size
        self.animated_properties['opacity'] = 1.0