import hashlib
import random
import string
import sys
import numpy as np

from PIL import Image, ImageColor

def get_random_hsv(digest):
    hue = digest[0] # Full hue coverage. We are hue-agnostic.
    sat = 40 + (60/255) * digest[1]  # Sat between 40 and 100; this avoids grey colors.
    val = 25 + 15 * sum(digest[2:6])/255  # A steep bell curve around val 62
    return f"hsv({hue}, {sat}%, {val}%)"

def gen_row(foreground, size):
    # Should probably pre-set the array size instead of use a list
    background = ImageColor.getrgb("#0a0f14")  # Following 'gotham' from terminal.sexy for now
    half = np.array([random.choice([background, foreground]) for x in range(size)], np.uint8)
    return np.concatenate((half, half[::-1]))  # There surely is a clever matrix way to do this

def gen_grid(size, digest):
    foreground = ImageColor.getrgb(get_random_hsv(digest))
    return np.array([gen_row(foreground, size) for x in range(size*2)])

def gen_image(size=8, seed=''.join([random.choice(string.ascii_letters) for i in range(16)])):
    # random.seed(seed)  # This is lazy, but it works fine for single thread stuff
    digest = hashlib.sha256(seed.encode('ASCII')).digest()
    im = Image.fromarray(gen_grid(size, digest))
    return im

def main(argv):
    im = gen_image(int(argv[1]), argv[2])
    im.save(f"{argv[2]}_identicon.png", "PNG")
    print("New image saved!")

if __name__ == "__main__":
    main(sys.argv)
