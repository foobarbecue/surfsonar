import logging
from numpy import arange
from waveshare_epd import epd2in13_V2
from PIL import Image, ImageDraw, ImageFont


# Make a display
epd = epd2in13_V2.EPD()
font = ImageFont.truetype("/home/pi/surfsonar/src/ConsolaMonoBold-A9Am.ttf", 40)
logging.info("init and Clear")
# partial update
time_image = Image.new("1", (epd.width, epd.height), 255)
time_draw = ImageDraw.Draw(time_image)

epd.init(epd.FULL_UPDATE)
epd.displayPartBaseImage(epd.getbuffer(time_image))
epd.init(epd.PART_UPDATE)

data={'distance':0,'confidence':100}
for x in arange(0, 20, 0.1):
    data_str = f"{x :4.1f}m\n{data['confidence']:4}%"
    time_draw.rectangle((0, 0, epd.width, epd.height), fill=255)
    time_draw.text((0, 0), data_str, font=font, fill=0)
    epd.displayPartial(epd.getbuffer(time_image))