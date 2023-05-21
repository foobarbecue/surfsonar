#!/usr/bin/python3
# -*- coding:utf-8 -*-
# display stuff
import logging
from waveshare_epd import epd2in13_V3
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime

# sonar stuff
from brping import Ping1D

logging.basicConfig(level=logging.DEBUG, filename="/home/aaron/sonarlogs.txt")


# Make a new sonar
logging.info("starting sonar")
myPing = Ping1D()
myPing.connect_serial("/dev/ttyUSB0", 115200)
myPing.initialize()

# Make a display
epd = epd2in13_V3.EPD()
font_big = ImageFont.truetype("/home/aaron/surfsonar/src/ConsolaMonoBold-A9Am.ttf", 35)
font_medium = ImageFont.truetype("/home/aaron/surfsonar/src/ConsolaMonoBold-A9Am.ttf", 20)
font_small = ImageFont.truetype("/home/aaron/surfsonar/src/ConsolaMonoBold-A9Am.ttf", 15)
logging.info("init and Clear")

canvas = Image.new("1", (epd.width, epd.height), 255)
draw = ImageDraw.Draw(canvas)

epd.init()
epd.Clear(0xFF)
epd.displayPartBaseImage(epd.getbuffer(canvas))

with open(f'/home/aaron/data/{datetime.now()}.txt','w') as profiledata:
    while True:
        data = myPing.get_distance()
        profile = myPing.get_profile()
        profile['timestamp'] = datetime.now().isoformat().replace(':','-')
        profiledata.write(str(profile)+'\n')
        draw.rectangle((0, 0, epd.width, epd.height), fill=255)

        draw.text((0, -5), "depth", font=font_small)
        draw.text((0, 10), f"{data['distance'] / 1000 :4.1f}m", font=font_big, fill=0)

        draw.text((0, 45), "confidence", font=font_small)
        draw.text((0, 60), f"{data['confidence']:3}%", font=font_big, fill=0)

        draw.text((0, 95), "battery", font=font_small)
        draw.text((0, 110), " 33%", font=font_big, fill=0)

        draw.text((0, 145), "gps", font=font_small)

        draw.text((0, 160), "6 fix\n11S 444699\n   3696019", font=font_medium)

        epd.displayPartial(epd.getbuffer(canvas))
