from kivy.uix import *

def default_callback(button):
    pass


def camera_control_callback(button):
    main = button.parent.parent
    main.remove_widget(main.menus['main'])
    main.add_widget(main.menus['lens'], main.menu_index)
    print 'Camera Control is pressed'
    # return True


def movement_control_callback(button):
    main = button.parent.parent
    main.remove_widget(main.menus['main'])
    main.add_widget(main.menus['motion'], main.menu_index)
    print 'Movement Control is pressed'
    # return True


def setting_callback(button):
    print 'Setting is pressed'
    # return True


def return_button_callback(button):
    print 'Return button is pressed'
    main = button.parent.parent
    main.remove_widget(button.parent)
    main.add_widget(main.menus['main'], main.menu_index)