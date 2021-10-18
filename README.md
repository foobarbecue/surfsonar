[code is here](https://github.com/foobarbecue/surfsonar)

[writeup best viewed here](https://foobarbecue.github.io/surfsonar/)

[Hacker News thread](https://news.ycombinator.com/item?id=28901214)

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**

- [Putting a sonar depth sensor into a surfboard](#putting-a-sonar-depth-sensor-into-a-surfboard)
- [Why](#why)
- [How](#how)
  - [Tools](#tools)
  - [Ingredients](#ingredients)
  - [Recipe](#recipe)
- [Does this ruin the surfboard?](#does-this-ruin-the-surfboard)
- [Does it work?](#does-it-work)
- [Todo](#todo)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# Putting a sonar depth sensor into a surfboard

<img src="https://user-images.githubusercontent.com/854789/136716532-c8290415-742d-4497-bd39-fff4d4448e42.png" height=350px />  <img src="https://user-images.githubusercontent.com/854789/136716561-d0a32797-1715-4c74-bac9-be51f06f4071.png" height=350px /> <img src="https://user-images.githubusercontent.com/854789/136716695-0046fa21-0816-493a-a275-2234a853a4c8.png" height=350px/>

(yes, I've rotated the text to the correct direction since then)

# Why

Out surfing, I often wonder how deep the water is, and suspect based on wave behavior that I'm over a deep spot or a shallow spot. Waves generally break when they enter shallow water (there are various conflicting formulas for figuring out exactly how shallow). At beach breaks like San Onofre Bluffs, the best place to wait for a good wave is right over a sandbar, and the sandbars can move around from day to day.

One day I decided to stop wondering and find out. I figured I could build a depth sensing sonar into my board and maybe I'd learn a thing or two about the sand underneath me, the dynamics of waves, and maybe even improve my surfing. Along the way I also learned some things about my surfboard, glue, wireless power, etc. It was fun and it works so I figured I'd share all the details here.

# How

## Tools
- Phillips screwdriver
- Drill
- Largeish drill bit
- 1 3/4" Hole saw (or slightly bigger I guess if you can find one)
- Small saw (the one on my Leatherman Wave worked nicely)
- Dremel (I used the Dremel Lite. It's pretty lame. I miss my plug-in Dremel which I gave away.)

## Ingredients

**Item**|**Manufacturer**|**Model**|**Source**|**Price**|**Comment**
:------|:------|:------|:------|:------|:------
Computer|Raspberry Pi |Zero W| | |I started with the Pi Pico, but upgraded when I realized: a) The python libraries for the sonar would need significant rework b) It'd be quite nice to have wifi
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
Silicone sealant|| | | |

## Recipe

Note: I switch back and forth bewtween imperative tense (Cut the hole) to first person (I cut the hole) in the below. Imperative is when I'm strongly recommending doing it my way. First person is when I feel like there's a good chance you could improve on my methods!

1. **Set up the RPi.** Burn Raspberry Pi OS / Debian Buster to an sd card. Mount it and create a wpa_supplicant.conf for your wifi a blank ssh.txt on the boot partition. Solder male headers onto the top of the board if you didn't buy the pi with headers. Screw the PiSugar onto the bottom of the board (so the pogo pins contact solder joints on the bottom of the board). Press the display onto the headers on the top of the board. At this point you probably want to ssh into the board and play with the display a bit using the [python libraries and included examples](https://github.com/waveshare/e-Paper/tree/master/RaspberryPi_JetsonNano/python).
   
1. **Wire it up**. Connect the Ping Sonar to the BLUART board with the included pins, and the BLUART board to the RPi with the male to male usb micro cable. At this point you probably want to ssh into the board and try out the sonar using the [python libraries and included examples](https://github.com/waveshare/e-Paper/tree/master/RaspberryPi_JetsonNano/python).

    <img src="https://user-images.githubusercontent.com/854789/136716861-bd218e27-a287-49b1-b143-293cdc687cec.JPG" height="200" /> <img src="https://user-images.githubusercontent.com/854789/136716894-9207b048-299c-404e-b344-036c9de8c334.jpg" height="200" />

1. **Set up the code**. I basically mashed together one of the e-ink examples with one of the sonar examples. Code is [here](https://github.com/foobarbecue/surfsonar). You probably want the code to run on boot. There are lots of ways to do this, but I used the quick-and-dirty one: add an @reboot line to crontab. Run `crontab -e` and add a line that goes something like `@reboot /home/pi/surfsonar/src/sonarDisp.py > /tmp/sonarOutput.txt 2>&1`. 

1. **Box it up**. Drill a hole in the side of the opaque section of the Polycase box for the sensor cable passthrough. Careful not to drill too close to the bottom of the box, because you need to leave enough space to screw on the inside part of the cable passthrough. (I made this mistake and had to hack away one of the mounting points on the inside bottom of the box in order to make it fit). Stick the display to the transparent front of the case using the mounting tape. Stick the wireless power receiver coil there too. You may need to cut it out of its foil packaging first (see ingredients section). I used glue stick to try to glue it to the Polycase but I don't think that actually did anything -- there was remnant adhesive on the coil PCB and that did the job. It's a moderately tight fit so just think about where everything goes and play around with it a bit. Especially the USB cable coming out of the RPi -- I had to cut away some of the plastic on the connector to make that fit. Close it all up and test it.

1. **Operate**.
 Before you start butchering, learn the anatomy of your board. In particular, how many stringers do you have, and where are they? Since you can't seen them on a foamie, I walked into the Catch Surf store and asked. They told me I have three stringers, all pretty close to the middle. I tried a stud finder and to my surprise it was able to see them. <br /><br /> Cut a hole in the top of the board just big enough for the Polycase box. Drill a hole in the bottom of your board with the hole saw to put the sonar in. When you flip the board, remember that the sides switch! This sounds obvious, but... turns out it's an easy mistake to make (embarrased face). If you used a 1 3/4" hole saw you'll find it's a little small and needs enlarging -- I hacked away some foam and carved away some of the plastic to enlarge the circle. I cut a channel in the bottom of the board for the cable, but didn't go all the way to the sensor hole. For cutting through the plastic on the bottom of the board I used a dremel at first and then used my Leatherman Wave saw, cutting at about a 45 deg angle to remove a triangular prism of foam with a rectangle of slick plastic on top (the "channel lid"). Then I used a drill with big drill bit to make the connections between the sensor hole, the channel, and the Polycase. I cut away enough in the "channel" to fit the excess cable, and glued the "channel lid" back on. I sealed around the edges of the sensor with silicone sealant. 

    <img src="https://user-images.githubusercontent.com/854789/136716834-6a5c9945-1a30-4f0e-b6d1-1cc34bdb4883.jpg" height="200"/> <img src="https://user-images.githubusercontent.com/854789/136716840-26b05243-dd3a-4486-a1de-0783d4b40a2b.jpg" height="200"/>


1. **Power** Add velcro strips to the charging pad and the top of the Polycase. Now you can keep your board vertical in a board rack and slap the charger on it. <br/><br/> I didn't add an external power switch of any kind. The PiSugar S has a feature where it switches off when the battery gets down to 3V, and switches back on when the battery is charged to 3.6V. It seems to run for 5h or so on a charge (careful test pending). So, my system is generally to attach the charger to it the night before and let it run all day until the low-voltage disconnect turns it off. The PiSugar also has a feature where attaching power should turn on the Pi even if it was shutdown normally with high battery voltage. To enable both of these auto-turn-on behaviors, there's a confusingly labelled switch, labelled AUTO on one side and ON on the other. The switch should be set on the ON side to enable the automatic behaviors.

    <img src="https://user-images.githubusercontent.com/854789/136716242-d8008624-e3d6-4af2-ab13-26b752df327a.JPG" height="200" > <img src="https://user-images.githubusercontent.com/854789/136716248-e706d4dc-2ca8-4af2-b104-d08a6375e307.JPG" height="200" >


# Does this ruin the surfboard?
I was concerned about compromising the watertightness of my board. Somewhere on the internet I read a heretic view that foamies don't get waterlogged, which sure would be nice, wouldn't it? I figured I'd try a test. I weighed the foam cylinder I cut on scale that measures to the gram (unfortunately I don't have anything better hand) and got 3g. I soaked it in water under a weight for a couple of days and it still weighed 3g. Note that this is fresh water, not salt water, and I suspect the repeated compression of surfing on it is what actually drives water into the foam, and I didn't test that.

<img src="https://user-images.githubusercontent.com/854789/136716757-5b8c0db4-a713-429d-80d4-24cacff93642.jpg" height="200" /> <img src="https://user-images.githubusercontent.com/854789/136716776-aa332835-18a8-4226-a3ea-e9d427427208.png" height="200" />


# Does it work?
I've taken it out for one test surf and the numbers were very reasonable once I got well past the break. I paddled out to see and watched the depth tick up about 2.4m to 3.2m, reading 100% confidence most of the time. However, closer to shore, near the breaking waves, I was getting nonsense readings and low confidence. I suspect this is due to bubbles (thanks to mannykannot and orforforof on HN for this insight). I need to look at the full waveform data to figure out if I can get good numbers in the surf zone. In the interactive plot below, you can see the two periods where I sat waiting outside. The surf was too good to collect more data than that!

{% include sonar_test_trail5_2021-01-17.html %}


# Todo
 - [ ] Parallize display update and sonar recording so it doesn't block
 - [ ] Add GPS & RTC
 - [ ] Add battery voltage and current monitoring
 - [ ] Put time and plot on display
