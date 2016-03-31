import kivy

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
#from kivy.uix.camera import Camera
from kivy.uix.image import AsyncImage
from callbacks.main_menu import *
from custom.widgets.picture_button import *
from custom.widgets.adjustments import BinaryAdjustment
from __root__ import *

class MainMenuLayout(GridLayout):
    def __init__(self):
        super(MainMenuLayout, self).__init__(rows=4)

        self.padding = 10
        self.spacing = 10

        camera_control_button = Button(text='Lens Controls')
        camera_control_button.bind(on_release=camera_control_callback)
        self.add_widget(camera_control_button)

        movement_control_button = Button(text='Motion Controls')
        movement_control_button.bind(on_release=movement_control_callback)
        self.add_widget(movement_control_button)

        settings_button = Button(text='Settings')
        settings_button.bind(on_release=setting_callback)
        self.add_widget(settings_button)

        recording_buttons = GridLayout(cols=2)
        recording_buttons.spacing = 10
        recording_buttons.add_widget(Button(text='Start Recording'))
        recording_buttons.add_widget(Button(text='End Recording'))
        self.add_widget(recording_buttons)



class LensControlMenuLayout(GridLayout):
    def __init__(self):
        super(LensControlMenuLayout, self).__init__(rows=4)
        self.add_widget(BinaryAdjustment('Zooming', default_callback, default_callback))
        self.add_widget(BinaryAdjustment('Focusing', default_callback, default_callback))
        self.add_widget(PicturedButton(icon_path('undo2.png')))
        recording_buttons = GridLayout(cols=2)
        recording_buttons.spacing = 10
        recording_buttons.add_widget(Button(text='Start Recording', id='StartRecording'))
        recording_buttons.add_widget(Button(text='End Recording', id='EndRecording'))
        self.add_widget(recording_buttons)








class MainLayout(GridLayout):
    def __init__(self, handedness='right'):
        super(MainLayout, self).__init__(cols=2)
        self.menus = {'main':MainMenuLayout(), 'lens':LensControlMenuLayout()}
        if handedness == 'right':
            self.add_widget(AsyncImage(source='http://www.president.gov.ua/storage/j-image-storage/01/89/38/94033d27b2015f3db8d5afa29ab92bb3_1444821939_large.png'))
            self.add_widget(self.menus['main'])
            self.menu_index = 2
        else:
            self.add_widget(self.menus['main'])
            self.add_widget(AsyncImage(source='http://www.president.gov.ua/storage/j-image-storage/01/89/38/94033d27b2015f3db8d5afa29ab92bb3_1444821939_large.png'))
            self.menu_index = 1





class ControlInterface(App):

    def build(self):
        # self.build(super)


        return MainLayout(handedness='left')

if __name__ == '__main__':
    ControlInterface().run()