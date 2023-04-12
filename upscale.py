#!/usr/bin/python3

import os 
import sys
from PIL import Image
from RealESRGAN import Upscaler4x


upscaler = Upscaler4x()
if len(sys.argv) == 2:
    inf = sys.argv[1]
    outf = os.path.splitext(inf)[0] + "x4.jpg"
elif len(sys.argv) == 3:
    inf = sys.argv[1]
    outf = sys.argv[2]
else:
    print("Usage: python3 upscale.py <src_image> [dst_image]")
    sys.exit(0)

image = Image.open(inf)
upscaler(image).save(outf)
