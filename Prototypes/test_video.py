from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics.texture import Texture
from kivy.graphics import Rectangle
from numpy import reshape
from array import array

from picamera.array import PiRGBArray
from picamera import PiCamera
import time


class CameraTestWidget(Widget):
    def __init__(self, **kwargs):
        super(CameraTestWidget, self).__init__(**kwargs)

        camera = PiCamera()
        camera.resolution = (400, 480)

        output = PiRGBArray(camera)

        camera.capture(output, 'rgb')

        texture = Texture.create(size=(400, 480))

        texture_buffer = []


        size = 400 * 480 * 3
        # texture_buffer = [int(x * 255) / size for x in range(size)]

        print 'Captured Photo %dx%d' % (output.array.shape[1], output.array.shape[0])

        for row in range(output.array.shape[1]):
            for column in range(output.array.shape[0]):
                for color in range(3):
                    # print 'Index is %d. ' % (row*output.array.shape[0]*3+column*3+color)
                    # texture_buffer[row*output.array.shape[0]*3+column*3+color] = output.array[column, row, color]
                    texture_buffer.append(output.array[column, row, color])
                # print 'Pixel [%d, %d] is color %d, %d, %d' % (row, column, output.array[column, row, 0], output.array[column, row, 1], output.array[column, row, 2])

        texture_buffer = 'b'.join(map(chr, texture_buffer))

        # texture_array = array('B', reshape(output, 1).tolist())

        # texture_array = array('B', [int(value) for value in reshape(output, 1).tolist()])

        # for color in texture_buffer:
        #     print color

        texture.blit_buffer(texture_buffer, colorfmt='rgb', bufferfmt='ubyte')

        with self.canvas:
            Rectangle(texture=texture, pos=self.pos, size=(400, 480))


class CameraTestApp(App):
    def build(self):
        return CameraTestWidget()


if __name__ == '__main__':
    CameraTestApp().run()



