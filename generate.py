import random
import numpy as np

from PIL import Image, ImageColor

background = ImageColor.getrgb("#0a0f14")  # Following 'gotham' from terminal.sexy for now
foreground = ImageColor.getrgb("#98d1ce")

def gen_row():
    half = np.array([random.choice([background, foreground]) for x in range(4)], np.uint8)  # Should probably pre-set the array size instead of use a list
    return np.concatenate((half, half[::-1]))  # There surely is a clever identity matrix way to do this

def gen_grid():
    return np.array([gen_row() for x in range(8)])

def gen_image():
    im=Image.fromarray(gen_grid())
    im.save("identicon.png", "PNG")
