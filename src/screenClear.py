#!/usr/bin/env python3
import logging
from waveshare_epd import epd2in13_V3

epd = epd2in13_V3.EPD()
logging.info("init and Clear")
epd.init()
epd.Clear(0xFF)
