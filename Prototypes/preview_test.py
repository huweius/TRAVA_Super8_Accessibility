import io
import thread
import picamera as p
import time

from kivy.core.image import Image as CoreImage
from kivy.core.image import ImageData as CoreImageData
from kivy.graphics.texture import Texture
from kivy.graphics import Rectangle
from kivy.uix.image import Image
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

class testApp(App):

    def build(self):
        self.b= BoxLayout()
        self.image_composition = Image()
        self.cam = p.PiCamera()
        self.cam.resolution = 400,480

        self.cam.capture('temp.jpg')
        self.image_composition = Image(source='temp.jpg')
        self.stream = io.BytesIO()
        # self.stream=io.BytesIO()
        # self.cam.capture(self.stream, 'rgb')
        # self.cam.close()
        # self.stream.seek(0)
        # self.tex = Texture.create(size=(1600,896), colorfmt='rgb')
        # self.tex.blit_buffer(self.stream.getvalue(), colorfmt='rgb', bufferfmt='ubyte')
        # with self.image_composition.canvas:
        #     Rectangle(texture = self.tex, size = (1600,896))
        print 'final'
        self.b.add_widget(self.image_composition)

        return self.b

    def on_start(self):
        super(testApp, self).on_start()
        thread.start_new_thread(self.preview_loop, ())

    def preview_loop(self):
        frame = 1
        # for image in self.cam.capture_continuous('temp.jpg'):
        #     self.image_composition.source = 'temp.jpg'
        #     # self.image_composition.reload()
        #     print 'Image reloaded'
        #     frame += 1
        #     time.sleep(1)

        while True:
            self.cam.capture(self.stream, format='png')
            self.stream.seek(0)
            self.image_composition = CoreImage(self.stream, ext='png')
            self.image_composition.reload()
            self.stream.truncate()
            print 'Image reloaded'



        # for image in self.cam.capture_continuous(self.stream, format='rgb'):
        #     print 'Frame %d' % (frame)
        #     self.stream.truncate()
        #     self.stream.seek(0)
        #     print 'Finished seeking'
        #     self.tex.blit_buffer(self.stream.getvalue(), colorfmt='rgb', bufferfmt='ubyte')
        #     print 'Finished blitting buffer'
        #     self.image_composition.canvas.clear()
        #     print 'Finished clearing canvas'
        #     self.image_composition.canvas.add(Rectangle(texture=self.tex, size=(800, 480)))
        #     print 'Finished adding rectangle'
        #     self.image_composition.canvas.draw()
        #     # self.image_composition.r
        #     print 'Finished drawing'
        #     frame += 1


testApp().run()

