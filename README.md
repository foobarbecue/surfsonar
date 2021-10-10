Out surfing, I often wonder how deep the water is, and suspect based on wave behavior that I'm over a deep spot or a shallow spot. Waves generally break when they enter shallow water (there are various conflicting formulas for figuring out exactly how shallow). At beach breaks like San Onofre Bluffs, the best place to wait for a good wave is right over a sandbar, and the sandbars can move around from day to day.

One day I decided to stop wondering and find out. I figured I could build a depth sensing sonar into my board and maybe I'd learn a thing or two about the sand underneath me, the dynamics of waves, and maybe even improve my surfing. Along the way I also learned some things about my surfboard, glue, wireless power, etc. It was fun and it works so I figured I'd share all the details here.

## Ingredients

**Item**|**Manufacturer**|**Model**|**Source**|**Price**|**Comment**
:-----:|:-----:|:-----:|:-----:|:-----:|:-----:
Computer|Raspberry Pi |4b| | |I started with the Pi Pico, but upgraded when I realized: a) The python libraries for the sonar would need significant rework b) It'd be quite nice to have wifi
Battery|PiSugar |S| | |
Sensor|Blue Robotics|Ping2D| |$341|
Serial to USB board (FTDI)|Blue Robotics|BLUART| |$42|
Enclosure|Polycase|WC-21| |12.51|
Glue|Gorilla|Original| | |You want original, not clear, for repairing boards. The difference is original expands (foams up) when setting and fills available space. This is good when you want to "grow into" the foam.
Surfboard|Catch Surf|Odysea Log 6'0| | |
Wireless power receiver|HOMEFUNTIME|Fast QI Receiver|https://www.amazon.com/gp/product/B07Z28DY9L|14.99|Sold in packs of two but you only need one. However, I cut off the outer foil layer to make it fit better and it took two tries to get that right, so I was glad that I got forced into buying two!
Wireless power transmitter| | | | |
Dessicant| | | | |
Grease| | | | |
Velcro| | | | |

## Recipe

