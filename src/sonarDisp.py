#!/usr/bin/python3
# -*- coding:utf-8 -*-
# display stuff
import logging
from waveshare_epd import epd2in13_V2
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
from time import sleep

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
font = ImageFont.truetype("/home/pi/surfsonar/src/ConsolaMonoBold-A9Am.ttf", 40)
logging.info("init and Clear")

outp_image = Image.new("1", (epd.width, epd.height), 255)
outp_draw = ImageDraw.Draw(outp_image)

epd.init(epd.FULL_UPDATE)
epd.displayPartBaseImage(epd.getbuffer(outp_image))
epd.init(epd.PART_UPDATE)

#Color top half, where ghosting is, black
outp_draw.rectangle((0, 0, epd.width, epd.height / 2), fill=0)

with open(f'/home/pi/data/{datetime.now()}.txt','w') as profiledata:
    while True:
        data = myPing.get_distance()
        profile = myPing.get_profile()
        profile['timestamp'] = datetime.now().isoformat().replace(':','-')
        profiledata.write(str(profile)+'\n')
        data_str = f"{data['distance'] / 1000 :4.1f}m\n{data['confidence']:3}%"
        logging.info(data_str)
        outp_draw.rectangle((0, 0, epd.width, epd.height), fill=255)
        outp_draw.text((0, epd.height / 2), data_str, font=font, fill=0)
        epd.displayPartial(epd.getbuffer(outp_image))
        sleep(1)
