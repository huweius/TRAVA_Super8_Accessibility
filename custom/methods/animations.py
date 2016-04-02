from kivy.animation import Animation


class Animator(Animation):
    def __init__(self, **kw):
        super(Animator, self).__init__(**kw)
        self.original_size = (0, 0)
        self._duration = 2

    def fade_out (self, widget):
        print "Executing Fade Out"
        self.original_size = (widget.width, widget.height)
        self.animated_properties['opacity'] = 0
        self.animated_properties['size'] = (10, 10)
        self.start(widget)

    def fade_in (self, widget):
        print "Executing Fade In"
        self.animated_properties['size'] = self.original_size
        self.animated_properties['opacity'] = 1.0
        self.start(widget)
