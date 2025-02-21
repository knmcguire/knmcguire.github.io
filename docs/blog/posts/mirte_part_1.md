---
title: Building MIRTE, Open Source Robot from TU Delft
date:
  created: 2025-02-17
  updated: 2025-02-17
draft: true
categories: 
    - builds
authors:
  - kim
#comments: true
links:
  - MIRTE Website: https://mirte.org/
---

<script data-goatcounter="https://knmcguire.goatcounter.com/count"
async src="//gc.zgo.at/count.js"></script>

<p><img alt="mirte part 1 tumbnail" src="https://knmcguire.github.io/blog/images/mirte_done.jpg" width="100" /></p>

_I've spent some days building the low-cost open-source educational robot developed by TU Delft! Here is a short blog post describing that experience and some ideas and plans for projects I could possibly do with it. It's an awesome platform._

<!-- more -->

So when I decided to take a little career break before starting anything new, I had a whole list of things and projects that I'd like to do. 
Eventhough I've done quite some creative projects... at one point I'd like to make something physical, with sensors that move... a robot perhaps?
I'm very glad that on a previous trip to my old university town, Martin Klomp lent me building materials to build the MIRTE, a fully open-source robot that TU Delft has developed for educational purposes.
I knew Martin from my time on the organizing committee of the Robocup Junior (NL) competition in the Netherlands, so this is a project that has come from all that shared experience of needing a good standard mobile robot for kids and students alike.
This platform is and will be used in their university classes in robotics as well, so I'm excited to see what it is all about.

## Building  MIRTE

<center>![MIRTE robot overview](images/mirte_overview.png){ width="300" }</center>

So I got the building materials for the MIRTE Pioneer, but there are other versions as well, that have fewer capabilities but are more suitable for kids or students who are just getting started.
I've made a picture of everything that came in the box, which are all off the shelf.
The version I had did have the 'MIRTE PCB,' of which the KiCad files are available under the CERN open hardware license, but the [MIRTE website](https://mirte.org/) also provides instructions to connect all the sensors through wires and a breadboard. Also, I've gotten a whole bunch of sensors like sonar, camera, infrared sensors, and some screens. How will it all fit!

<center>![MIRTE robot done](images/mirte_expansion.jpg){ width="300" }</center>

So once I've covered all the materials, I followed the building instructions on the [MIRTE website](https://mirte.org/).
It had visual instructions that made it quite easy to put things together. But I was more impressed with the clever design of the base itself.
The Orange board and the MIRTE PCB were attached with screws along with some sensors, but the base itself could be assembled without the use of even one screw.
Even the motors for the wheels could be easily clicked into place.
Also, in the front part of the base, there were modules for the sensors that could be clicked in facing forward and changed to other sensors depending on the application of the project.
This is a very handy feature.

<center>![MIRTE robot done](images/mirte_done.jpg){ width="300" }</center>

Here is a video of the full build:

<center><iframe width="560" height="315" src="https://www.youtube.com/embed/JcqcggjcqF8?si=GLnWwj4mbfMycYdx" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe></center>

## Connecting and driving MIRTE

So once I've put in the flashed SD card, I was able to connect with MIRTE since it initializes like a WiFi access point. The web UI is where I could put in the SSID and password of the access point that I'd like the MIRTE to connect to instead. Since I am currently running Windows (yeah yeah I know the torture I put myself through), I'll skip it for now because I know what kind of network issues I'll be getting with that, and I want to get driving right away!

<center>![MIRTE robot web GUI](images/mirte_gui.png){ width="400" }</center>

So here in this web UI, I can also test the sensors. I've put on 2 distance sensors on the sides and one camera. The camera isn't shown on the GUI yet, but I can already test out the right and left distance cameras. Also, it contains a simple control panel so that I can remote control the MIRTE and chase my cats!

I was about to quit here and leave the MIRTE on a shelf while I think about the next project... but then late at night I woke up in cold sweat where my unconscious robotist side of mine said: NO WAY! I can't leave just leave it hanging as a remote-controlled car... let's at least connect those sensors to something! 

Since there are 2 distance sensors on the side, this is the perfect opportunity to make a Braitenburg robot, which is literally 2 lines of logic (or 2 blocks for Blockly).
MIRTE has an API for Blockly, Python, and ROS1, but I'll stick with Python for now and wait for the ROS 2 version to come out (this will be somewhere in 2025).
But it was possible to edit this all in MIRTE's WebGUI.

```python
max_speed = 50 # percentage speed
while True:
  left_dist = mirte.getDistance('left')
  right_dist = mirte.getDistance('right')
  right_motor_speed = round(min(max(left_dist, 1), max_speed))
  left_motor_speed = round(min(max(right_dist, 1), max_speed))
  mirte.setMotorSpeed('right', right_motor_speed)
  mirte.setMotorSpeed('left', left_motor_speed)
```

And that is what a Braitenburg robot is, where the sensors are directly connected to the actuators. This is as simple of a robot that can be. But with this, it can already avoid most of the obstacles (and cats) in the room!
 The distance sensors don't have a very large field of view so there is a dead spot right in front of it (like the chair leg). But as long as it goes with a slow speed... there is usually no harm to MIRTE. That is how easy robotics can be.

See here the full video of testing the distance sensors and wheels, and making the MIRTE drive autonomously based on a Braitenburg vehicle.

<center><iframe width="560" height="315" src="https://www.youtube.com/embed/CBb7-vnnBmc?si=iLKSgSTNvPmbG5Hd" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe></center>

## Conclusion and what is next?
So I'll leave the MIRTE alone after that (tiny) crash, since I need to figure out how to access the camera and think about what other sensors I can add.
For instance, I do have an AOK-D Lite camera and a small lidar I can put on top.
And how about a small arm or gripper? So many possibilities, but I'll wait until my unconscious robotist wakes me up in the middle of the night with a good plan. 
But all in all, the MIRTE is a really nice platform, and the base is quite sturdy as well. 
And the web UI to control it and define the sensors is very well thought out as well. 
The project is still in development and I'll make sure to share my notes for improvement with the developers (or contribute). 
But I can't wait for the ROS 2 packages to come out for this robot so that I can connect it with NAV 2, Gazebo harmonic, or have a Crazyflie land on it perhaps?

If you want to check it out, all of the build plans are open sourced and can be found on [mirte.org](https://mirte.org/).
The full base can be laser-cut out of 4 mm MDF and configured to accommodate other sensors as well[^1]. 
But in any way, thanks again to Martin Klomp from [RoboHouse](https://robohouse.nl/) at [TU Delft](https://www.tudelft.nl/) for lending me the [MIRTE](https://mirte.org/). It was fun!

[^1]: 
  I kind of really want to buy a laser cutter for myself now in fact... anyone know of a good model for home/hobby use by any chance? 