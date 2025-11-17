---
title: "Robot arm!"
date:
  created: 2025-11-17
  updated: 2025-11-18
draft: true
categories: 
    - robotics
authors:
  - kim
comments: false
---

<script data-goatcounter="https://knmcguire.goatcounter.com/count"
async src="//gc.zgo.at/count.js"></script>

[![](images/robot_arm_puzzle.png){width=100}](freelancing_6months.md)

_It is always good to be reminded on how hard robotics can be! I got a taste of that again when I worked with the S0-100 this summer and the last months. Still! It's interesting and fun to come accross new projects to try out!_

<!-- more -->

This summer I tried something new! I've done a lot of simulation, swarm robotics and aerial vehicles in my career, with mostly vision in the mix. I just have never worked with robot arms, aka manipulators before! Time to change that, and this summer after receiving my shiny new 3D printer I thought, let's try out that fancy S0-100 arm that everyone is raving about! I'm sure it is fully intergrated into ROS 2 so I could started right away!

## Building the arm!

The [build of the SO-100](https://github.com/TheRobotStudio/SO-ARM100) was suprisingly easy! Sure, I had to wait a few weeks to get the Feetech motors in, and my Bambu A1 mini had to do all nighters for a while, but once I had those in I was all ready to go! I only was a bit late to notice that I wasn't printing out the new fancy S0-101 version, but luckily it used exactly the same motors. The other things like the adapter, usb cables and woodclamps were all locally sourcable at the local hobbystores here.

It took me a couple of afternoons to assemble the SO-100 arm, and it was a lot of fun doing so. There were a couple of pieces of the arm that definitely were a very tight fit. luckily that was something that I could fix with an very profesional heatgun (aka my hairdryer). It was only unfortunate that I found out at the very end, that I had accidently mixed up the carefully ID programmed motors in order!

Luckily I was able to still access those motors and were able to change the ID's programatically still, so no harm done and I was able to calibrate the motors at the end as well.

I've made an compilation video of the streams of the build. This was all build in a LoFi-build video I've been experimenting with so might be nice to play in the background after a day of work!

<iframe width="560" height="315" src="https://www.youtube.com/embed/To5IaJ_1NLs?si=QeYRp5nnuAs2UMEt" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

And for those that don't have the patience, there is a sped up version of the same build process:

<iframe width="560" height="315" src="https://www.youtube.com/embed/8lhbWUhtOF0?si=_gr7t8pJwMcs667d" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## Controlling the arm?

Alright, I'll be straight upfront about this, I might have been a little less successfull with this part. Once I finished building the arm, I had a couple of conference to go to, and afterwards I wanted to get straight into it. I decided skip the next SO-100 control instructions and went straight into ROS. I didn't additionally build the teleopperation arm but since I saw that there was a [SO-100](https://index.ros.org/r/so_arm_100_hardware/#jazzy). How hard can it be!

At [ROSCon UK](https://roscon.org.uk/2025/) I've even followed an half day workshop that included [Moveit2](https://moveit.picknik.ai/main/index.html). The pervious ROS package was build so that it could serve this [this SO arm 100 arm project](https://github.com/brukg/so_arm_100_hardware) so hence I jumped right in, excited for a full out of the box experience.

There you go, Mistake one... assume you know it all and take shortcuts. 
