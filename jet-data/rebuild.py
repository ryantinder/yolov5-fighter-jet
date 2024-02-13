import pyautogui
import time
import sys
from PIL import Image, ImageDraw, ImageFont
import random

with Image.open("./output/1707787392_1657_1603_.png") as im:
    print(im.size)
    # draw = ImageDraw.Draw(im)
    # draw.rectangle([1657, 1603, 1757, 1703], outline="red", width=25)
    # im.save("./output/rebuilt/1_1657_1603.png", "PNG")