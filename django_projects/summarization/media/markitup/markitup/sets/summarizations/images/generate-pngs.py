#!/usr/bin/env python

import os

def textToPng(names):
    for name in names:
        os.system("convert -size 16x16 xc:transparent -pointsize 10 -draw \"text 0,10 '%(name)s'\" -channel Gray %(name)s.png" % locals())

names = ["TX", "NM", "YN", "CL", "DT", "MD"]

textToPng(names)

