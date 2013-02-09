#!/usr/bin/env python

import colour
import sys
import json
import webcolors

import PIL.Image as Image
import PIL.ImageDraw as ImageDraw

def snap_to_grid(src, ref):

    fh = open(src, 'r')
    data = json.load(fh)

    utils = colour.utils(ref)

    results = {}

    for hex, details in data['colours'].items():

        closest = utils.closest_colour(hex)
        results[hex] = closest

    return results

def draw(results):

    count = len(results.keys())    

    slice = 100 
    width = count * slice
    height = 500

    dx = slice
    dy = height / 2

    x = 0
    y = 0

    im = Image.new("RGBA", (width, height))
    canvas = ImageDraw.Draw(im)
    
    for hex, closest in results.items():

        rainbow = map(webcolors.hex_to_rgb, (hex, closest[0]))

        for rgb in rainbow:

            h = webcolors.rgb_to_hex(rgb)

            canvas.rectangle((x, y, (x + dx), (y + dy)), fill=rgb)
            canvas.text((x + 10, y + 10), h, fill=(255,255,255))

            y += dy

        x += dx
        y = 0

    return im

if __name__ == '__main__':

    src = sys.argv[1]
    ref = sys.argv[2]

    res = snap_to_grid(src, ref)
    im = draw(res)

    im.show()


