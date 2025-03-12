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


I can't even believe it really myself, that I've spent my entire university studies of my bachelors and masters with a full windows laptop as my computer. Well... I've started with Industrial Design Engineering in 2007 so it that made sense. At that time, windows was just superior with all things Adobe, and even 3D CAD solidworks worked on nothing else than Window. Even MacOS had some catching up to do of being the graphic design powerhouse it is today. But as soon as I did my bridging course to Mechanical engineering and finally my Masters at Bio-Mechanical engineering, it was getting a little bit more difficult. Still I hung on, as we mostly scripted in Matlab, and for some Java and even Prolog still worked okay. I remember that I would roll my eyes when someone was evangalising Ubuntu to me as the superior OS, as you can do everything that windows does, (like Octave instead of Matlab, or Gimp instead of Photoshop). But still I didn't feel the urge to switch... until I had to work with ROS for my final Master's project in 2014. Luckily they had a seperate fixed computer for me to work on, which had Ubuntu 14 with ROS 1 Indigo, such that I can keep my trusty full windows laptop to do the rest. However, I do still have trauma's of the c++ course that I had to do on that, which still resonates with me to this day (why, visual studio, why!)

When I started my PhD in 2015, and after weeks of trying to setup a proper development environment for embedded C with Cygwin, both me and the lab technition broke and went ahead to install a dualboot on my laptop, which is something that I've done on all my university and work laptops ever since. I just couldn't really find really 1 on 1 replacements for the graphic programs like Adobe, gaming was superior on windows (yes I did use my work laptop for that), and even the running of high rendering simulation. Although that I was inflicted by the constant choice of a Nvidea card (since I have the silent hope to do more with deep learning and Cuda at one point), this limited me to having to deal with the dual boot and having to restart my computer if I needed to do any development. Since I had such a pain of c++ development, I didn't want to even try setting that up again and that was my state well far until after my PhD ended: Dual boot of windows and Ubuntu, tightly side to side. Not ideal, but it works for most of my usecases, but the loss of drive space for both OSes and to constantly having to reboot to switch from one side to another. If you are working as PhD, you settle for what works and won't risk diviation to something that potentially loses time... "You don't have time for that!? Now go write your journal papers."

It wasn't until my time at Bitcraze, almost 5 years later, that I gave it another try. For the python development I tested it out on windows just to make sure that the crazyflie python library and cfclient was working before every release, and was supriced that that worked pretty well on Windows. So I found myself on the 'dark side' of the computer (aka windows but depends on who you ask) more and more for at least the python development, but still had to move back to the ubuntu part quite often for C development... until my colleagues told me about the windows sub system for linux. At that time, it was still a development feature on windows 10, and the Gui feature was still quite non-existing other than to hack around quite a bit for subpar result. But it allowed me to compile the C firmware of the Crazyflie, copy it to the windows part and flash the crazyflie with the python cflib.  Suddenlhy development on Windows wasn't as... painful as it used to be. I had even written a  [blogpost about that state on the bitcraze website](https://www.bitcraze.io/2021/04/transitioning-back-to-windows-development/).





