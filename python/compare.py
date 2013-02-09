#!/usr/bin/env python

import webcolors
import colour
import sys

import PIL.Image as Image
import PIL.ImageDraw as ImageDraw

def side_by_side(hex1, hex2, **kwargs):

    width = kwargs.get('width', 500)
    height = kwargs.get('height', (width / 2))

    dx = width / 2
    dy = height

    x = 0
    y = 0

    img = Image.new("RGBA", (width, height))
    canvas = ImageDraw.Draw(img)

    for hex in (hex1, hex2):

        rgb = webcolors.hex_to_rgb(hex)

        canvas.rectangle((x, y, (x + dx), (y + dy)), fill=rgb)
        canvas.text((x + 10, y + 10), hex, fill=(255,255,255))

        x += dx

    return img

if __name__ == '__main__':
    
    palette = sys.argv[1]
    hex = sys.argv[2]

    p = colour.palette(palette)
    u = colour.utils(p)

    c_hex, c_name = u.closest_colour(hex)

    im = side_by_side(hex, c_hex)
    im.show()
