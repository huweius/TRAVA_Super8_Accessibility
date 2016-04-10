import os

def root_path():
    return os.path.dirname(__file__)

def icon_path(icon):
    return os.path.join(os.path.dirname(__file__), 'Resources', 'Images', 'Icons', icon)

def image_path(image):
    return os.path.join(os.path.dirname(__file__), 'Resources', 'Images', image)