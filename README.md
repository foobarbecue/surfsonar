Out surfing, I often wonder how deep the water is, and suspect based on wave behavior that I'm over a deep spot or a shallow spot. Waves generally break when they enter shallow water (there are various conflicting formulas for figuring out exactly how shallow). At beach breaks like San Onofre Bluffs, the best place to wait for a good wave is right over a sandbar, and the sandbars can move around from day to day.

One day I decided to stop wondering and find out. I figured I could build a depth sensing sonar into my board and maybe I'd learn a thing or two about the sand underneath me, the dynamics of waves, and maybe even improve my surfing. Along the way I also learned some things about my surfboard, glue, wireless power, etc. It was fun and it works so I figured I'd share all the details here.

## Ingredients

**Item**|**Manufacturer**|**Model**|**Source**|**Price**|**Comment**
:------|:------|:------|:------|:------|:------
Computer|Raspberry Pi |4b| | |I started with the Pi Pico, but upgraded when I realized: a) The python libraries for the sonar would need significant rework b) It'd be quite nice to have wifi
Battery system|PiSugar |S|[amazon](https://www.amazon.com/gp/product/B099RB7G78)|$29||
Display|Waveshare|2.13inch_e-Paper_HAT|[amazon](https://www.amazon.com/gp/product/B071S8HT76)|$25|Looks great outdoors in the sun. Quite slow to refresh.|
Sensor|Blue Robotics|Ping Sonar (Ping2D)|[Blue Robotics](https://web.archive.org/web/20201201211944/https://bluerobotics.com/store/sensors-sonars-cameras/sonar/ping-sonar-r2-rp/)|$279|The version of this I bought had potted connectors on both ends, which was a bit of a pain to install in a board. With mine, I had to cut a trench in the board to put the cable in there, and it was much longer than needed. I figured that was easier than cutting, soldering and worrying about waterproofing the joint. Since then they've upgraded the sensor-side connector to a WetLink Pentrator -- looks way more convenient. The price has gone up a bit, presumably to account for the connector.
Serial to USB adapter (FTDI)|Blue Robotics|BLUART|[Blue Robotics](https://bluerobotics.com/store/comm-control-power/tether-interface/bluart-r1-rp/) |$42|You could probably skip this and use a UART on the RPi|
Enclosure|Polycase|WC-21|[Polycase](https://www.polycase.com/wc-21)|$12.51|
Glue|Gorilla|Original| | |You want original, not clear, for repairing boards. The difference is original expands (foams up) when setting and fills available space. This is good when you want to "grow into" the foam.
Surfboard|Catch Surf|Odysea Log 6'0|Catch surf store here in SC| |I agonized over which of my boards to use and in the end decided on the foamie because 1) It's what I ride when the conditions are really bad and that's when I might have time to pay attention to a gadget. 2) Bad conditions are when I can most use the extra help from a magic sandbar-spotter.|
Wireless power receiver|HOMEFUNTIME|Fast QI Receiver|[amazon](https://www.amazon.com/gp/product/B07Z28DY9L)|15|Sold in packs of two but you only need one. However, I cut off the outer foil layer to make it fit better and it took two tries to get that right, so I was glad that I got forced into buying two!
Wireless power transmitter|TOZO|W1|[amazon](https://www.amazon.com/gp/product/B07FM8R7J1)|$20| |
USB cable | CableCreation | Micro USB to Micro USB OTG |[amazon](https://www.amazon.com/gp/product/B0744BW2B2)| $8|I created something like this by chopping and soldering two micro USB cables together (with impeccable heatshrink of course) and it worked at first, but then only intermittently. I switched to combining a male micro to female USB-A cable with a normal USB-A to micro usb cable. I went through several combinations of such cables that seemed like they should work with no luck before finding one that did. In the end I tried buying this little cable which has been reliable.
Grease| | | | |Might not be needed, but there was a little water inside the enclosure after I tested it overnight in a bathtub so I added it to the gaskets. No evidence of any leaking since then. I used a "single serving" packet of bike chain grease that came with my Aventon ebike.
Dessicant|Aquapapa|2 gram silica gel|[amazon](https://www.amazon.com/gp/product/B01MZ4ZQ3Z)|$8.53 / 100 | |
Velcro|3M| | | |Any velcro would work fine probably
Mounting tape|Scotch|108-SML|[amazon](https://www.amazon.com/dp/B01MZ2RVCQ)|$16.53 for an infinite supply|

## Tools
 - Phillips screwdriver
 - Drill 
 - Largeish drill bit
 - 1 3/4" Hole saw
 - Small saw (the one on my Leatherman Wave worked nicely)
 - Dremel

## Recipe

1. **Set up the RPi.** Burn Raspberry Pi OS / Debian Buster to an sd card. Mount it and create a wpa_supplicant.conf for your wifi a blank ssh.txt on the boot partition. Solder male headers onto the top of the board if you didn't buy the pi with headers. Screw the PiSugar onto the bottom of the board (so the pogo pins contact solder joints on the bottom of the board). Press the display onto the headers on the top of the board. At this point you probably want to ssh into the board and play with the display a bit using the [python libraries and included examples](https://github.com/waveshare/e-Paper/tree/master/RaspberryPi_JetsonNano/python).
   
1. **Wire it up**. Connect the Ping Sonar to the BLUART board with the included pins, and the BLUART board to the RPi with the male to male usb micro cable. At this point you probably want to ssh into the board and try out the sonar using the [python libraries and included examples](https://github.com/waveshare/e-Paper/tree/master/RaspberryPi_JetsonNano/python).
   
1. **Set up the code**. I basically mashed together one of the e-ink examples with one of the sonar examples. Code is in this repo.
1. **Put it in a box**. Drill a hole in the side of the opaque section of the Polycase box for the sensor cable passthrough. Careful not to drill too close to the bottom of the box, because you need to leave enough space to screw on the inside part of the cable passthrough. (I made this mistake and had to hack away one of the mounting points on the inside bottom of the box in order to make it fit).
1. Butcher your surfboard
When you flip the board, remember that the right side of the board is now the left side. This sounds obvious, but let's just say... turns out it's an easy mistake to make (embarrased face) 
## Is the surfboard watertight?

## How well does it work?

## Todo
 [ ] Get auto turn-on working properly
 [ ] Rotate display to correct orientation
 [ ] Record the full waveform
 [ ] Add GPS & RTC
 [ ] Add battery voltage and current monitoring