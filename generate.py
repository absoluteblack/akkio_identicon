import random
import string
import numpy as np

from PIL import Image, ImageColor

def get_color():
    colors = [
        "#e31a1c",
        "#31a354",
        "#dca060",
        "#3182bd",
        "#756bb1",
        "#80b1d3",
        "#fcfdfe"
    ]
    return random.choice(colors)

def get_random_hsv():
    hue = 255 * random.random()  # Full hue coverage. We are hue-agnostic.
    sat = 40 + 60 * random.random()  # Sat between 40 and 100; this avoids grey colors.
    val = 20 * sum([random.random() for x in range(5)])  # A steep bell curve around val 50
    return f"hsv({hue}, {sat}%, {val}%)"


def gen_row(foreground):
    # Should probably pre-set the array size instead of use a list
    background = ImageColor.getrgb("#0a0f14")  # Following 'gotham' from terminal.sexy for now
    half = np.array([random.choice([background, foreground]) for x in range(4)], np.uint8)
    return np.concatenate((half, half[::-1]))  # There surely is a clever matrix way to do this

def gen_grid():
    # foreground = ImageColor.getrgb(get_color())
    foreground = ImageColor.getrgb(get_random_hsv())
    return np.array([gen_row(foreground) for x in range(8)])

def gen_image(seed=''.join([random.choice(string.ascii_letters) for i in range(16)])):
    random.seed(seed)  # This is lazy, but it works fine for single thread stuff
    im = Image.fromarray(gen_grid())
    return im
