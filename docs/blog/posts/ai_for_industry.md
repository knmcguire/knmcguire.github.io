---
title: "Going through the AI for industry challenge"
date:
  created: 2026-09-01
  updated: 2026-09-01
draft: true
categories: 
    - robotics
authors:
  - kim
comments: true
links:
  - The AI for industry challenge official website: https://www.intrinsic.ai/events/ai-for-industry-challenge
---

<script data-goatcounter="https://knmcguire.goatcounter.com/count"
async src="//gc.zgo.at/count.js"></script>

[![](images/kim_aichallenge.png){width=100}](freelancing_1year.md)


_something something something._


<!-- more -->
![image](images/kim_aichallenge.png){width=500 .center}
*<p style="text-align: center;">Working on the AI for industry challenge in my new office and setup.</p>*

So my very first assignment officially as McGuire Robotics AB, was joining team B-robotized at the AI for Industry challenge. This was an open challenge, organized by Intrinsic (now part of Google), where anyone could participate in. It was all about automating electgronics assembly, in this case a simulated server slot assembly, where the robot arm had to manipulate and handle flexible cables and insert plugs,  Mostly tailored towards roboticists, but in practise also data scientist, AI engineers or embedded developers could have their first go at robotics in this challenge. 

## Before the qualifying round

So we allready started working on the challenge since early this year, around February, where would look at existing tools that could prepare us already so to get fully into the challenge. We already figured that most likely the UR5e arm was going to be used for the challenge, so we managed to get a gazebo simulater started up with a standard gripper (the robotiq one). We managed to get 3 cameras on that arm and experimented with a taskboard that is already more familiar, which is bascially just a basic peg in hole type of taskboard from the NIST standard models.

We had no idea what would be provided during the challenge, so we also connected the arm with Moveit and made sure it can be controlled with impedenace control and that we were able to control it with a cartisian target. This was also important for the first ground work of implementing HIL-SERL which was human in the loop reinforicement learning. This was our main trumph card for the final insertion, arguably the most difficult part of the challenge.

My main goal was to setup the simulation for learning, and potentially look into Nvida Isaac or Mujoco. Also, simulating the flexible cables is an entire different thing entirely so that would also take quite some time to ijmplemnt.

## During the qualifying round

So once the toolkit came out, we realized that many things already were available that we tried to implement before. The toolkit already came with a fully working and controlable UR5E plus gripper (albeit a much simpler one), together with the entire frame work and taskboard already simulated in Gazebo. We eventually decided to not go the Nvidia Isaac route, mostly due to the difficulty of running that on everyones machine, but also because we found out that the evaluation of the qualifying round was mainly done in Gazebo.

This meant that my role as chef simulation kind of got diminished as the full platform was already there. However, I do have an lot of perception experience from back in my Master's and Early Phd projects. Perhaps to some of the developers no-a-days my computer vision knowledge is perhaps considered 'old school', but I must say it was very satisfying to jump back into OpenCV and use those old musscles, and can very powerfull as well. 

## Taskboard detecting 

So initially I focussed on the first part of the task, which was detecting the pose of the taskboard and orienting itself above the location the ports. The idea was that if we are able to detect the full pose of the taskboard, we will be able to do the logic later of where the actual components were. This was all to retrieve the actual 3D pose of the port that we needed to have the gripper to move towards and get as close as possible so that the reinforcement learning policy would take over.

First thing I thought about is to make a binary image of the taskboard by tresholding it's gray scale image related to it's much lighter background. Then with some clean up of the artifiacts (like the light lines on the back) by erroding and dillating the binary image with morphological filters. Then to retrieve the edges, and fit lines on those edges with houghlines and ransac filtering. These lines, when they intersect they will 4 corners, even if those corners could not be seen by the camera because it is too nearby. Then, the flatsquare was projected using the camera info information using the SolvePnP algorithm, to retrieve those points in 3D space and hence getting the 3D pose of the taskboard. Ofcourse you'd have rotation ambiquity as well, so luckily there was also a nice mageneta logo that gave some clarity on that too. 

On a clean, empty taskboard, this usually works pretty well on a single camera, however on a more cluttered taskbaord with nicc ards you'd find more squares then only the taskboard. So the projection would be validated it by the multiple cameras (because there were 3), if all 3 cameras were able to detect the taskboard at the same place within a certain tolarance, it will at least confirm that it's detecting it propeperly. Perhaps a kalman filter would have been sufficient, but from all the detection it has done there was maybe only 1 out of an 100 that it saw a different square somewhere else, and if it did detect it was usually on to an acuracy of milimeters which was definitely good enough!

The port detections itself was done in quite a different technique, namely the use of yolo lfor the prot detection. This was the task of my team mate Yara, which handled all of the training