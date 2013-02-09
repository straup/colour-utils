#!/usr/bin/env python

import colour
import sys

first = sys.argv[1]
rest = sys.argv[2:]

p1 = colour.palette(first)
p2 = None

for next in rest:

    p2 = colour.palette(next)
    p1.merge(p2)

p1.dump()

