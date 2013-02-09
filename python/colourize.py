#!/usr/bin/env python

import colour
import sys
import json
import webcolors

import PIL.Image as Image
import PIL.ImageDraw as ImageDraw

def draw(palette, image):

    palette = colour.palette(palette)
    utils = colour.utils(palette)

    results = {}

    im = Image.open(image)

    for y in range(im.size[1]):
        for x in range(im.size[0]):

            old = im.getpixel((x, y))

            hex = webcolors.rgb_to_hex(old)
            closest = utils.closest_colour(hex)

            new = webcolors.hex_to_rgb(closest[0])
            im.putpixel((x, y), new)

    return im

if __name__ == '__main__':

    import colour

    palette = sys.argv[1]
    image = sys.argv[2]

    im = draw(palette, image)

    im.save("test.png")
    im.show()


