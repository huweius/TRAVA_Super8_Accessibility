from kivy.uix import *


def camera_control_callback(button):
    button.parent.parent
    print 'Camera Control is pressed'


def movement_control_callback(button):
    print 'Movement Control is pressed'


def setting_callback(button):
    print 'Setting is pressed'