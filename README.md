Out surfing, I often wonder how deep the water is, and suspect based on wave behavior that I'm over a deep spot or a shallow spot. Waves generally break when they enter shallow water (there are various conflicting formulas for figuring out exactly how shallow). At beach breaks like San Onofre Bluffs, the best place to wait for a good wave is right over a sandbar, and the sandbars can move around from day to day.

One day I decided to stop wondering and find out. I figured I could build a depth sensing sonar into my board and maybe I'd learn a thing or two about the sand underneath me, the dynamics of waves, and maybe even improve my surfing. Along the way I also learned some things about my surfboard, glue, wireless power, etc. It was fun and it works so I figured I'd share all the details here.

## Ingredients

**Item**|**Manufacturer**|**Model**|**Source**|**Price**|**Comment**
:------|:------|:------|:------|:------|:------
Computer|Raspberry Pi |4b| | |I started with the Pi Pico, but upgraded when I realized: a) The python libraries for the sonar would need significant rework b) It'd be quite nice to have wifi
Battery|PiSugar |S| | |
Sensor|Blue Robotics|Ping Sonar (Ping2D)|[Blue Robotics](https://web.archive.org/web/20201201211944/https://bluerobotics.com/store/sensors-sonars-cameras/sonar/ping-sonar-r2-rp/)|$279|The version of this I bought had potted connectors on both ends, which was a bit of a pain to install in a board. With mine, I had to cut a trench in the board to put the cable in there, and it was much longer than needed. I figured that was easier than cutting, soldering and worrying about waterproofing the joint. Since then they've upgraded the sensor-side connector to a WetLink Pentrator -- looks way more convenient. The price has gone up a bit, presumably to account for the connector.|Blue Robotics|BLUART| |$42|
Enclosure|Polycase|WC-21| |$12.51|
Glue|Gorilla|Original| | |You want original, not clear, for repairing boards. The difference is original expands (foams up) when setting and fills available space. This is good when you want to "grow into" the foam.
Surfboard|Catch Surf|Odysea Log 6'0|Catch surf store here in SC| |
Wireless power receiver|HOMEFUNTIME|Fast QI Receiver|[amazon](https://www.amazon.com/gp/product/B07Z28DY9L)|15|Sold in packs of two but you only need one. However, I cut off the outer foil layer to make it fit better and it took two tries to get that right, so I was glad that I got forced into buying two!
Wireless power transmitter|TOZO|W1|[amazon](https://www.amazon.com/gp/product/B07FM8R7J1)|$20| |
USB cable | CableCreation | Micro USB to Micro USB OTG |[amazon](https://www.amazon.com/gp/product/B0744BW2B2)| $8| |
Dessicant| | | | |
Grease| | | | |
Velcro| | | | |
Mounting tape| | | | |

## Recipe

1. Set up the RPi
   
   I installed 
   
1. Wire it up
1. Put it in a box
1. Butcher your surfboard

## Is the board watertight?

## How well does it work?