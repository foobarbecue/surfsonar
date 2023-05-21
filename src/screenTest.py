import logging
from numpy import arange
from waveshare_epd import epd2in13_V3
from PIL import Image, ImageDraw, ImageFont
from time import sleep

# Make a display
epd = epd2in13_V3.EPD()
font_big = ImageFont.truetype("/home/aaron/surfsonar/src/ConsolaMonoBold-A9Am.ttf", 35)
font_medium = ImageFont.truetype("/home/aaron/surfsonar/src/ConsolaMonoBold-A9Am.ttf", 20)
font_small = ImageFont.truetype("/home/aaron/surfsonar/src/ConsolaMonoBold-A9Am.ttf", 15)
logging.info("init and Clear")
# partial update
canvas = Image.new("1", (epd.width, epd.height), 255)
canvas.transpose(Image.ROTATE_180)
draw = ImageDraw.Draw(canvas)

epd.init()
epd.Clear(255)
epd.displayPartBaseImage(epd.getbuffer(canvas))

data={'distance':0,'confidence':100}
for x in arange(0, 20, 0.1):
    draw.rectangle((0, 0, epd.width, epd.height), fill=255)

    draw.text((0, -5), "depth", font=font_small)
    draw.text((0, 10), f"{x :4.1f}m", font=font_big, fill=0)

    draw.text((0, 45), "confidence", font=font_small)
    draw.text((0, 60), f"{data['confidence']:4}%", font=font_big, fill=0)

    draw.text((0, 95), "battery", font=font_small)
    draw.text((0, 110), " 33%", font=font_big, fill=0)

    draw.text((0, 145), "gps", font=font_small)

    draw.text((0, 160), "6 fix\n11S 444699\n   3696019", font=font_medium)

    epd.displayPartial(epd.getbuffer(canvas))
    sleep(1)
