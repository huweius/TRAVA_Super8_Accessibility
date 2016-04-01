from kivy.uix.image import Image
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import thread

# TODO: Integrate Camera Preview to Kivy Screen Interface


class PreviewScreen(Image):
    def __init__(self, **kwargs):
        super(Image, self).__init__(**kwargs)
        self.camera = PiCamera()
        self.camera.resolution = (400, 300)
        self.camera.framerate = 30
        self.rawCapture = PiRGBArray(self.camera, size=(400, 300))

        time.sleep(0.5)

        self.thread = thread.start_new_thread(self.thread_callback, self)

    def thread_callback(self):
        for frame in self.camera.capture_continuous(self.rawCapture, format='bgr', use_video_port=True):
            if self.parent:
                self.canvas = frame.array

