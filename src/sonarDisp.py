#!/usr/bin/python3
# -*- coding:utf-8 -*-
# display stuff
import logging
from waveshare_epd import epd2in13_V3
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
import socket
import re
import board
import adafruit_gps
from brping import Ping1D

logging.basicConfig(level=logging.INFO, filename=f"/home/aaron/sonarlogs/{datetime.now().isoformat()}.txt")


# Make a new sonar
myPing = Ping1D()
myPing.connect_serial("/dev/ttyUSB0", 115200)
myPing.initialize()

# Set up a socket to talk to the pisugar3 battery module
batt_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
batt_socket.connect(('0.0.0.0', 8423))

# Set up the GPS
i2c = board.I2C()
gps = adafruit_gps.GPS_GtopI2C(i2c, debug=False)
gps.send_command(b"PMTK314,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0")
gps.send_command(b"PMTK220,1000")

# Make a display
epd = epd2in13_V3.EPD()
font_big = ImageFont.truetype("/home/aaron/surfsonar/src/ConsolaMonoBold-A9Am.ttf", 35)
font_medium = ImageFont.truetype("/home/aaron/surfsonar/src/ConsolaMonoBold-A9Am.ttf", 20)
font_small = ImageFont.truetype("/home/aaron/surfsonar/src/ConsolaMonoBold-A9Am.ttf", 15)
logging.info("gps_time,depth,confidence,batt_soc,gps_nmea")

canvas = Image.new("1", (epd.width, epd.height), 255)
draw = ImageDraw.Draw(canvas)

epd.init()
epd.Clear(0xFF)
epd.displayPartBaseImage(epd.getbuffer(canvas))

with open(f'/home/aaron/data/{datetime.now()}.txt','w') as profiledata:
    while True:
        #query battery module
        batt_socket.send(b'get battery')
        batt_soc_str = batt_socket.recv(20).decode()
        batt_soc_str = re.match('battery: (\d\d.\d\d).*', batt_soc_str)
        if batt_soc_str:
            batt_soc_pct = float(batt_soc_str[1])
        else:
            batt_soc_pct = float('nan')

        #query sonar
        data = myPing.get_distance()
        profile = myPing.get_profile()
        profile['timestamp'] = datetime.now().isoformat().replace(':','-')
        profiledata.write(str(profile)+'\n')
        draw.rectangle((0, 0, epd.width, epd.height), fill=255)

        #query GPS
        gps.update()

        draw.text((0, -5), "depth", font=font_small)
        draw.text((0, 10), f"{data['distance'] / 1000 :4.1f}m", font=font_big, fill=0)

        draw.text((0, 45), "confidence", font=font_small)
        draw.text((0, 60), f"{data['confidence']:3}%", font=font_big, fill=0)

        draw.text((0, 95), "battery", font=font_small)
        draw.text((0, 110), f"{batt_soc_pct:3.1f}%", font=font_big, fill=0)

        draw.text((0, 145), "gps", font=font_small)

        draw.text((0, 160), f"s:{gps.satellites} f:{gps.fix_quality}\n"
                            f"{gps.latitude}\n{gps.longitude}", font=font_medium)

        epd.displayPartial(epd.getbuffer(canvas.transpose(Image.ROTATE_180)))

        #store data
        try:
            iso_gps_time = datetime(*gps.datetime[:6]).isoformat()
        except:
            iso_gps_time = None
        logging.info(f",{iso_gps_time},{data['distance']/1000},{data['confidence']},{batt_soc_pct},{gps.nmea_sentence}")
