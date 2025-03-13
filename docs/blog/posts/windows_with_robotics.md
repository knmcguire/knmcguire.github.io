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
  - ROS Discourse on Windows User Survey: https://discourse.ros.org/t/windows-survey-results/39502
  - New Installation instructions for ROS 2 Rolling: https://docs.ros.org/en/rolling/Installation/Windows-Install-Binary.html
---

<script data-goatcounter="https://knmcguire.goatcounter.com/count"
async src="//gc.zgo.at/count.js"></script>

<p><img alt="windows WSL2 terminals" src="https://knmcguire.github.io/blog/images/wslwinros.png" width="100" /></p>


*Yes, I am a little bit mad. Why the hell do I torture myself to get development to work on Windows... well, I tried to trace back the journey for robotics development, where I desperately tried to hang on to Windows, but had to settle for a dual boot, only to slowly return to give development on Windows hope again.*

*Enjoy! (I hope :wink:)*

<!-- more -->

## During my studies and PhD: Drawn into Ubuntu

I can't even believe it myself, that I've spent my entire university studies of my bachelor's and master's with a full Windows laptop as my computer. Well... I started with Industrial Design Engineering in 2007, so that made sense. At that time, Windows was just superior with all things Adobe, and even 3D CAD SolidWorks worked on nothing else than Windows. Even MacOS had some catching up to do to become the graphic design powerhouse it is today. But as soon as I did my bridging course to Mechanical Engineering and finally my Master's in Bio-Mechanical Engineering, it was getting a little bit more difficult. Still, I hung on, as we mostly scripted in Matlab, and some Java and even Prolog still worked okay on Window. I remember that I would roll my eyes when someone was evangelizing Ubuntu to me as the superior OS, saying you can do everything that Windows does (like Octave instead of Matlab, or Gimp instead of Photoshop). But still, I didn't feel the urge to switch... until I had to work with ROS for my final Master's project in 2014. Luckily, they had a separate fixed computer for me to work on, which had Ubuntu 14 with ROS 1 Indigo, so I could keep my trusty full Windows laptop to do the rest. However, I still have traumas from the C++ course that I had to do on that, which still resonates with me to this day (why, Visual Studio, why!).

When I started my PhD in 2015, and after weeks of trying to set up a proper development environment for embedded C with Cygwin, both me and the lab technician broke and went ahead to install a dual boot on my laptop, which is something that I've done on all my university and work laptops ever since. I just couldn't really find one-on-one replacements for the graphic programs like Adobe, gaming was superior on Windows (yes, I did use my work laptop for that), and even the running of high rendering simulation. Although I was inflicted by the constant choice of a Nvidia card (since I have the silent hope to do more with deep learning and CUDA at one point), this limited me to having to deal with the dual boot and having to restart my computer if I needed to do any development. Since I had such a pain with C++ development, I didn't want to even try setting that up again, and that was my state well until after my PhD ended: Dual boot of Windows and Ubuntu, tightly side by side. Not ideal, but it works for most of my use cases, but the loss of drive space for both OSes and constantly having to reboot to switch from one side to another. If you are working as a PhD, you settle for what works and won't risk deviation to something that potentially loses time... "You don't have time for that!? Now go write your journal papers."

## A glimmer of hope for Windows

It wasn't until my time at Bitcraze, almost 5 years later, that I gave it another try. For the Python development, I tested it out on Windows just to make sure that the Crazyflie Python library and cfclient were working before every release, and was surprised that it worked pretty well on Windows. So I found myself on the 'dark side' of the computer (aka Windows, but depends on who you ask) more and more for at least the Python development, but still had to move back to the Ubuntu part quite often for C development... until my colleagues told me about the Windows Subsystem for Linux. At that time, it was still a development feature on Windows 10, and the GUI feature was still quite non-existent other than to hack around quite a bit for subpar results. But it allowed me to compile the C firmware of the Crazyflie, copy it to the Windows part, and flash the Crazyflie with the Python cflib. I had even written [blogpost about that state on the bitcraze website](https://www.bitcraze.io/2021/04/transitioning-back-to-windows-development/). Suddenly, development on Windows wasn't as... painful as it used to be.

But still, the early version of WSL and WSL2/G on Windows 10 was quite buggy. So for some heavy-duty development, I still had a dual boot Ubuntu available. Since 2022, I started going back to ROS, transitioned to ROS 2, and that was still quite very much only suitable for Ubuntu (although I've tried to [compile Crazyswarm2 for Windows ](https://github.com/IMRCLab/crazyswarm2/issues/1) at one point... and half succeeded?). This was still very necessary, especially in combination with Gazebo. However, once I had a laptop with Windows 11 and tried out WSL2 there, which had GUI support out of the box, I started to use ROS more and more on WSL2, even though it wasn't officially supported. With USBipd to connect the Crazyradio dongle to the subsystem and the remote access from VSCode, I actually was on my Ubuntu (and later Pop!OS) less and less.

There is only one point remaining, and that was the janky GUI support from WSL2. The GUIs that popped up from WSL2 had a very slow FPS, couldn't resize properly, and didn't have proper mouse integration support. Moreover, I just couldn't, for the life of me, make WSL2 select my super fancy Nvidia graphics card on my Lenovo Legion Laptop for just RVIZ2 and Gazebo alone, only for the full container... And Pop!OS only had double graphic card support for Intel and Nvidia combos... So guess what kind of laptop I got huh?! A Ryzen with AMD integrated graphics card with a second Nvidia GPU... Just the one that is unsupported for Pop!OS multi GPU support... I need to pick out my laptops better next time.

## Now: Biting the bullet, full back into Windows

After my time at Bitcraze, I wanted to reinstall my computer to have a nice fresh start, but what to do? I've been bothered by the lack of disk space, not as appalled as much by C and ROS development on Windows with the help of WSL2, and hardly was using the Ubuntu of the dual boot anymore. There were just some graphic card support issues remaining. But, especially when the ROS team announced that they were changing up their [installation guidance for Windows installation of ROS 2](https://discourse.ros.org/t/upcoming-switch-of-windows-installation-to-pixi-conda/41916), I decided to go back to my roots and go full on Windows again! I am putting a lot of trust in this promised improvement, but luckily I don't have anyone relying on me to perform. And if it doesn't work out, I'll just get a second laptop for Ubuntu-only stuff (or use my Raspberry Pi 5, works pretty good with Ubuntu 24.04 these days!). No harm done! Only my pride on the line.

So once I got a fresh install of Windows 11, the absolute first thing I've tried out was the [new install instructions for ROS 2 on windows](https://github.com/ros2/ros2_documentation/pull/4989). Unfortunately, since the binaries/zip files weren't available, I went straight for the hardcore source install. They are now recommending using Pixi as the environment, which before it was only Miniconda. Sure, I had to wait half a day for all the essential ROS 2 packages to build and install, and fix a couple of errors here and there, but my god, what a breeze. Since it is now possible with the pixi.toml file to set up the environment exactly as it is supposed to, I had it working in a day! And check this out... here is a picture of ROS 2 Jazzy on WSL2 as listener and ROS 2 Jazzy on Windows 11 natively as talker! I felt just like a proud parent when this happened :blush:

<center>![One terminal in the windows sub system running a ROS 2 listener and ROS 2 natively on Windows running a talker](images/wslwinros
.png)</center>

But how about the GUI issues huh? That was still putting me off. Not only the GPU access issues and the low FPS of the browser refresh rate, but also the fact that sometimes, the WSL GUI just disappears and I can't retrieve it, and the only way to access it is to restart WSL2... Well, not anymore! Here a robot description ROS launched from WSL Ubuntu 24.04 and RVIZ2 from Windows with none of that issue. The only issue, of course, is the model will need to be fully described from the robot description, so if there is a model (STL or Collada) referred to in the robot description, you'll get an error, of course, since the native Windows RVIZ2 can't find it.

<center>![One terminal in the windows sub system startin up a robot description and ROS 2 natively on Windows running rviz2](images/rviz_wsl_windows.png)</center>

## What's next?

I see many possibilities here to make ROS running on Windows not as painful as it used to be, and maybe even better? Here I showed RVIZ2, but how about running Gazebo from Windows while running SLAM packages from WSL2? Or maybe a package that handles the USB support so I no longer have to use USBIPD? One thing is for sure, I'll like to use Pixi for everything now since it was an eye opener after I tried out the new ROS2 draft installation instructions for Windows. I'm glad that the ROS2 dev team decided to not fully give up on windows, since there seem to be many that actually rely on this (104 people answered [the survey ](https://discourse.ros.org/t/windows-survey-results/39502) they sent out). Now the [rolling ROS 2 documentation are out for Windows 10](https://docs.ros.org/en/rolling/Installation/Windows-Install-Binary.html) with the new instructions, but this works on windows 11 as well, and Jazzy with just a couple of bug fixes here and there. It's such an improvement for those who struggled with it before.




