import webcolors
import json
import PIL.Image as Image
import PIL.ImageDraw as ImageDraw

class utils:

    def __init__(self, palette):

        fh = open(palette, 'r')
        data = json.load(fh)

        self.hex = data['colours']
        self.rgb = {}

    def name_to_hex(self, name):

        for colour_hex, colour_details in self.hex.items():

            if colour_details['name'] == name:
                return colour_hex

        return None

    # http://stackoverflow.com/questions/9694165/convert-rgb-color-to-english-color-name-like-green

    def closest_colour(self, hex):

        r, g, b = webcolors.hex_to_rgb(hex)

        min_colours = {}

        for key, name in self.hex.items():
            r_c, g_c, b_c = webcolors.hex_to_rgb(key)
            rd = (r_c - r) ** 2
            gd = (g_c - g) ** 2
            bd = (b_c - b) ** 2
            min_colours[(rd + gd + bd)] = name

        idx = min(min_colours.keys())

        details = min_colours[idx]
        name = details['name']

        hex = self.name_to_hex(name)
        return hex, name

    def side_by_side(self, hex1, hex2, **kwargs):

        width = kwargs.get('width', 500)
        height = kwargs.get('height', (width / 2))

        dx = width / 2
        dy = height

        x = 0
        y = 0

        img = Image.new("RGBA", (width, height))
        canvas = ImageDraw.Draw(img)

        for hex in (hex1, hex2):

            # sigh...

            if not hex.startswith("#"):
                hex = "#" + hex

            rgb = webcolors.hex_to_rgb(hex)

            canvas.rectangle((x, y, (x + dx), (y + dy)), fill=rgb)
            canvas.text((x + 10, y + 10), hex, fill=(255,255,255))

            x += dx

        return img

if __name__ == '__main__':

    import sys

    palette = sys.argv[1]
    hex = sys.argv[2]

    u = utils(palette)
    c_hex, c_name = u.closest_colour(hex)

    im = u.side_by_side(hex, c_hex)
    im.show()    
