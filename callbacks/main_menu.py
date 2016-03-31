from kivy.uix import *

def default_callback(button):
    print button.id + 'is pressed'

def camera_control_callback(button):
    main = button.parent.parent
    main.add_widget(main.menus['lens'], main.menu_index)
    print 'Camera Control is pressed'
    #return True


def movement_control_callback(button):
    print 'Movement Control is pressed'
    #return True


def setting_callback(button):
    print 'Setting is pressed'
    #return True

def return_button_callback(button):
    print 'Return button is pressed'