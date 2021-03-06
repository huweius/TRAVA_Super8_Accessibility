import sys
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.camera import Camera
from kivy.uix.image import AsyncImage
from kivy.core.window import Window

from __root__ import *
from custom.widgets.adjustments import BinaryAdjustment
from custom.widgets.picture_button import *
from custom.movements.indicator import *
from custom.callbacks.main_menu import *
from custom.methods.animations import Animator

if sys.platform != 'win32':
    import RPi.GPIO as io
    print 'GPIO loaded'

Window.size = (800, 480)


class RecordingButtonsLayout(GridLayout):
    def __init__(self):
        super(RecordingButtonsLayout, self).__init__(cols=2)
        self.spacing = 10
        self.indicator = Indicator('Record Button', 12)
        self.add_widget(PicturedButton(icon_path('video-camera.png'), self.indicator.set_on, id='StartRecording'))
        self.add_widget(PicturedButton(icon_path('stop2.png'), self.indicator.set_off, id='EndRecording'))


class MainMenuLayout(GridLayout):
    def __init__(self):
        super(MainMenuLayout, self).__init__(rows=4)

        # self.animator = Animator()

        self.padding = 10
        self.spacing = 10

        camera_control_button = Button(text='Lens Controls')
        camera_control_button.bind(on_release=camera_control_callback)
        camera_control_button.font_size = 60
        self.add_widget(camera_control_button)

        movement_control_button = Button(text='Motion Controls')
        movement_control_button.bind(on_release=movement_control_callback)
        movement_control_button.font_size = 60
        self.add_widget(movement_control_button)

        settings_button = Button(text='Settings')
        settings_button.font_size = 60
        settings_button.bind(on_release=setting_callback)
        self.add_widget(settings_button)

        self.add_widget(RecordingButtonsLayout())


class LensControlMenuLayout(GridLayout):
    def __init__(self):
        super(LensControlMenuLayout, self).__init__(rows=4)

        self.padding = 10
        self.spacing = 10

        self.add_widget(BinaryAdjustment('Zooming', -1, -1))
        self.add_widget(BinaryAdjustment('Focusing', -1, -1))
        self.add_widget(PicturedButton(icon_path('undo2.png'), return_button_callback))

        self.add_widget(RecordingButtonsLayout())


class MotionControlMenuLayout(GridLayout):
    def __init__(self):
        super(MotionControlMenuLayout, self).__init__(rows=5)

        # self.animator = Animator()

        self.padding = 10
        self.spacing = 10

        self.add_widget(BinaryAdjustment('Height', 18, 23))
        self.add_widget(BinaryAdjustment('Panning', 16, 20))
        self.add_widget(BinaryAdjustment('Tilting', -1, -1))
        self.add_widget(PicturedButton(icon_path('undo2.png'), return_button_callback))

        self.add_widget(RecordingButtonsLayout())


class MainLayout(GridLayout):
    def __init__(self, handedness='right'):
        super(MainLayout, self).__init__(cols=2, background='white')
        # self.preview_screen = Camera()
        self.preview_screen = AsyncImage(source=image_path('preview.jpg'))
        self.menus = {'main': MainMenuLayout(), 'lens': LensControlMenuLayout(), 'motion': MotionControlMenuLayout()}
        if handedness == 'right':
            self.add_widget(self.preview_screen)
            self.add_widget(self.menus['main'])
            self.menu_index = 2
        else:
            self.add_widget(self.menus['main'])
            self.add_widget(self.preview_screen)
            self.menu_index = 1


class ControlInterface(App):

    def build(self):
        # self.build(super)

        return MainLayout(handedness='left')

    def on_stop(self):
        if sys.platform != 'win32':
            io.cleanup()


if __name__ == '__main__':
    ControlInterface().run()