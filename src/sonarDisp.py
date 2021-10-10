#!/usr/bin/python3
# -*- coding:utf-8 -*-
# display stuff
import logging
from waveshare_epd import epd2in13_V2
from PIL import Image, ImageDraw, ImageFont

# sonar stuff
from brping import Ping1D

logging.basicConfig(level=logging.DEBUG, filename="/home/pi/sonarlogs.txt")


# Make a new sonar
logging.info("starting sonar")
myPing = Ping1D()
myPing.connect_serial("/dev/ttyUSB0", 115200)
myPing.initialize()

# Make a display
epd = epd2in13_V2.EPD()
font = ImageFont.truetype("/home/pi/surfsonar/src/ConsolaMonoBold-A9Am.ttf", 45)
logging.info("init and Clear")
# partial update
time_image = Image.new("1", (epd.height, epd.width), 255)
time_draw = ImageDraw.Draw(time_image)

epd.init(epd.FULL_UPDATE)
epd.displayPartBaseImage(epd.getbuffer(time_image))

epd.init(epd.PART_UPDATE)
num = 0

while True:
    data = myPing.get_distance()
    data_str = f"{data['distance'] / 1000 :4.1f}m{data['confidence']:3}%"
    logging.info(data_str)
    if data:
        time_draw.rectangle((0, 0, 255, 104), fill=255)
        time_draw.text((0, 0), data_str, font=font, fill=0)
        epd.displayPartial(epd.getbuffer(time_image))