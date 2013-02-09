#!/usr/bin/env python

import colour
import sys
import json
import webcolors

import PIL.Image as Image
import PIL.ImageDraw as ImageDraw

def draw(ref, path):

    utils = colour.utils(ref)

    results = {}

    im = Image.open(path)

    for y in range(im.size[1]):
        for x in range(im.size[0]):

            old = im.getpixel((x, y))

            hex = webcolors.rgb_to_hex(old)
            closest = utils.closest_colour(hex)

            new = webcolors.hex_to_rgb(closest[0])
            im.putpixel((x, y), new)

    return im

if __name__ == '__main__':

    ref = sys.argv[1]
    old = sys.argv[2]
    # new = sys.argv[3]

    im = draw(ref, old)

    im.show()


