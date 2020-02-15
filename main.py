import numpy as np
import pyglet
from PIL import Image
import time

# Create a 1024x1024x3 array of 8 bit unsigned integers
data = np.zeros( (1024,1024,3), dtype=np.uint8 )

data[512:,512:] = [254,0,0]       # Makes the middle pixel red
data[512,513] = [0,0,255]       # Makes the next pixel blue

img = Image.fromarray(data).tobytes()       # Create a PIL image

window = pyglet.window.Window()
image = pyglet.image.ImageData(1024, 1024, 'RGB', img, pitch=-1024*3)



def update(dt):
    print(int(dt * 1932) % 1023)
    data[int(dt * 1932) % 1023, 300] = [0, 254, 0]
    img = Image.fromarray(data).tobytes()       # Create a PIL image
    image = pyglet.image.ImageData(1024, 1024, 'RGB', img, pitch=-1024*3)


pyglet.clock.schedule_interval(update, 1/120.0)
pyglet.app.run()


@window.event
def on_draw():
    window.clear()
    image.blit(0, 0)

class Pos:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Environment:
    def __init__(self):
        self.field = np.array((1000, 1000))

    def add_pheromones(self, pos):
        self.field[pos] = self.field[pos.x, pos.y] + 1

class Ant:
    def __init__(self, env):
        self.position = Pos(0, 0)
        self.env = env
        pass
    def update(self):
        pass

    def leave_pheromones(self):
        self.env.add_pheromones(self.position)





