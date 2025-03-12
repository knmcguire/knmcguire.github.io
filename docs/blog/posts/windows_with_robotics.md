---
title: "Robotics on Windows, Are You Mad?!"
date:
  created: 2025-03-12
  updated: 2025-03-12
draft: true
categories: 
    - robotics
authors:
  - kim
comments: false
links:
  - Bitcraze blogpost about windows develoment 2021: https://www.bitcraze.io/2021/04/transitioning-back-to-windows-development/
---

*Why the hell do I tortjer myself to get develoment to work on windows.... well I tried to trace back of where this came from. Maybe some of you could relate?*

*Enjoy!*

<!-- more -->

I can't even believe it really myself, that I've spent my entire university studies of my bachelors and masters with a full windows laptop as my computer. Well... I've started with Industrial Design Engineering in 2007 so it that made sense. At that time, windows was just superior with all things Adobe, and even 3D CAD solidworks worked on nothing else than Window. Even MacOS had some catching up to do of being the graphic design powerhouse it is today. But as soon as I did my bridging course to Mechanical engineering and finally my Masters at Bio-Mechanical engineering, it was getting a little bit more difficult. Still I hung on, as we mostly scripted in Matlab, and for some Java and even Prolog still worked okay. I remember that I would roll my eyes when someone was evangalising Ubuntu to me as the superior OS, as you can do everything that windows does, (like Octave instead of Matlab, or Gimp instead of Photoshop). But still I didn't feel the urge to switch... until I had to work with ROS for my final Master's project in 2014. Luckily they had a seperate fixed computer for me to work on, which had Ubuntu 14 with ROS 1 Indigo, such that I can keep my trusty full windows laptop to do the rest. However, I do still have trauma's of the c++ course that I had to do on that, which still resonates with me to this day (why, visual studio, why!)

When I started my PhD in 2015, and after weeks of trying to setup a proper development environment for embedded C with Cygwin, both me and the lab technition broke and went ahead to install a dualboot on my laptop, which is something that I've done on all my university and work laptops ever since. I just couldn't really find really 1 on 1 replacements for the graphic programs like Adobe, gaming was superior on windows (yes I did use my work laptop for that), and even the running of high rendering simulation. Although that I was inflicted by the constant choice of a Nvidea card (since I have the silent hope to do more with deep learning and Cuda at one point), this limited me to having to deal with the dual boot and having to restart my computer if I needed to do any development. Since I had such a pain of c++ development, I didn't want to even try setting that up again and that was my state well far until after my PhD ended: Dual boot of windows and Ubuntu, tightly side to side. Not ideal, but it works for most of my usecases, but the loss of drive space for both OSes and to constantly having to reboot to switch from one side to another. If you are working as PhD, you settle for what works and won't risk diviation to something that potentially loses time... "You don't have time for that!? Now go write your journal papers."

It wasn't until my time at Bitcraze, almost 5 years later, that I gave it another try. For the python development I tested it out on windows just to make sure that the crazyflie python library and cfclient was working before every release, and was supriced that that worked pretty well on Windows. So I found myself on the 'dark side' of the computer (aka windows but depends on who you ask) more and more for at least the python development, but still had to move back to the ubuntu part quite often for C development... until my colleagues told me about the windows sub system for linux. At that time, it was still a development feature on windows 10, and the Gui feature was still quite non-existing other than to hack around quite a bit for subpar result. But it allowed me to compile the C firmware of the Crazyflie, copy it to the windows part and flash the crazyflie with the python cflib.   I had even written a  [blogpost about that state on the bitcraze website](https://www.bitcraze.io/2021/04/transitioning-back-to-windows-development/). Suddenlhy development on Windows wasn't as... painful as it used to be.

But still, the early version of WSL and WSL2/G on Windows 10 was quite buggy. So for some heavy duty development I still had a dual boot Ubuntu available. Since 2022 I started going back to ROS, transitionted to ROS 2 and that was still quite very much only suitable for Ubuntu (although I've tried to [compile Crazyswarm2 for windows ](https://github.com/IMRCLab/crazyswarm2/issues/1)at one point... and half successeded?) This was still very necessary especially in combination with Gazebo. However, once I had a laptop with Windows 11 and tried out WSL2 there which had gui support out of the box, I started to use ROS more and more on WSL2, eventhough it wasn't officially supported. With USBipd to connect the Crazyradio dongle to the subsystem and the remote access from VScode, I actually was on my Ubuntu (and later Pop!OS) less and less. 

There is only one point remaining, and that was the yanky gui support from WSL2. The guis that popped up from WSL2 had a very slow FPS, couldn't recise properly and didn't had propeer mouse intergration support. Moreover, I just couldn't for the life of me, make WSL2 select my super fancy nvidia graphics card on my Lenovo Legon for just RVIZ2 and gazebo alone, only for the full container... And Pop!OS only had double graphiccard support for Intel and Nvidia combos... So guess what kind of laptop I got huh?! An Ryzen with AMD intergrated graphics card with a second Nvidia GPU... I need to pick out my laptops better next time.

After my time at Bitcraze, I wanted to reinstall my computer to have a nice a fresh start, but what to do? I've been bothered by the lack of disk space, not as apalled as much by c and ROS development on windows with the help of WSL2, and hardly was using the dual boot anymore. There were just some graphic card support issues remaining. But, Especially when the ROS team announced that they were changing up their [installation guidance for Windows installation of ROS 2](https://discourse.ros.org/t/upcoming-switch-of-windows-installation-to-pixi-conda/41916), I decided to go back to my roots and go full on Windows again! I am putting a lot of trust in this promised improvement but luckily I don't have anyone relying on me to perform. And if it doesn't work out I'll just get a second laptop for Ubuntu only stuff (or use my Raspberry pi 5, works pretty good with ubuntu 24.04 these days!). No harm done! only my pride on the line.

So once I got a fresh install of Windows 11, the absolute first thing I've tried out was the [new install instructions for ROS 2 on windows](https://github.com/ros2/ros2_documentation/pull/4989). Unfortunately since the binaries/zip files weren't available, I went straight for the hardcore scourse install. They are now recommending using Pixi as environemnt, which before it was only miniconda. Sure, I had to wait a half a day for all the essential ROS 2 packages to build and install, and fix a couple of errors here and there, but my god, what a breeze. Since it is now possible with pixi.toml file to setup the enviroment exactly as it supposed to, I had it working in a day! And check this out... here is a picture of ROS 2 Jazzy on WSL2 as listnerer and ROS 2 Jazzy on Windows 11 natively as talker! I felt just like a proud parent when this happened :blush:


<center>![One terminal in the windows sub system running a ROS 2 listener and ROS 2 natively on Windows running a talker](images/wslwinros
.png)</center>



But how about the GUI issues huh? that was still putting me off. Well look at this! 

TO BO CONTINUED