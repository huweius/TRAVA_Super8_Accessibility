from kivy.uix import *

def default_callback(button):
    print button.id + 'is pressed'

def camera_control_callback(button):
    #button.parent.parent
    print 'Camera Control is pressed'
    #return True


def movement_control_callback(button):
    print 'Movement Control is pressed'
    #return True


def setting_callback(button):
    print 'Setting is pressed'
    #return True