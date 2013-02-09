#!/usr/bin/env python

import colour
import webcolors

from PIL import Image, ImageDraw

def make_rainbow(colours, width, height):

    count = len(colours)
    slice = 100

    width = slice * count
    height = 200

    im = Image.new("RGBA", (width, height))
    canvas = ImageDraw.Draw(im)

    dx = width / float(len(colours)) 
    x = 0
    y = height / 2.0

    for hex in colours:

        rgb = webcolors.hex_to_rgb(hex)

        canvas.line((x, y, x + dx, y), width=height, fill=rgb)
        canvas.text((x + 10, 10), hex, fill=(255,255,255))

        x += dx

    return im

if __name__ == '__main__':

    import sys

    palette = sys.argv[1]
    palette = colour.palette(palette)

    colours = palette.sort_colours()

    im = make_rainbow(colours, 1024, 400)

    if len(sys.argv) == 3:
        im.save(sys.argv[2])
    else:
        im.show()

