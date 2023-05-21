import logging
from numpy import arange
from waveshare_epd import epd2in13_V3
from PIL import Image, ImageDraw, ImageFont
from time import sleep

# Make a display
epd = epd2in13_V3.EPD()
font = ImageFont.truetype("/home/aaron/surfsonar/src/ConsolaMonoBold-A9Am.ttf", 40)
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
    data_str = f"{x :4.1f}m\n{data['confidence']:4}%"
    draw.rectangle((0, 0, epd.width, epd.height), fill=255)
    draw.text((0, 0), data_str, font=font, fill=0)
    epd.displayPartial(epd.getbuffer(canvas))
    sleep(1)
