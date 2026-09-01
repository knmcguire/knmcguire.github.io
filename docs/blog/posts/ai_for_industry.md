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

So my very first assignment officially with my setup company McGuire Robotics AB, was joining team B-robotized at the AI for Industry challenge. This was an open challenge, organized by Intrinsic (now part of Google), where anyone could participate in. It was all about automating electgronics assembly, in this case a simulated server slot assembly, where the robot arm had to manipulate and handle flexible cables and insert plugs,  Mostly tailored towards roboticists, but in practise also data scientist, AI engineers or embedded developers could have their first go at robotics in this challenge. 

## Preparing for the qualifying round

So we allready started working on the challenge since early this year, around February, where would look at existing tools that could prepare us already so to get fully into the challenge. We already figured that most likely the UR5e arm was going to be used for the challenge, so we managed to get a gazebo simulater started up with a standard gripper (the robotiq one). We managed to get 3 cameras on that arm and experimented with a taskboard that is already more familiar, which is bascially just a basic peg in hole type of taskboard from the NIST standard models.

We had no idea what would be provided during the challenge, so we also connected the arm with Moveit and made sure it can be controlled with impedenace control and that we were able to control it with a cartisian target. This was also important for the first ground work of implementing HIL-SERL which was human in the loop reinforicement learning. This was our main trumph card for the final insertion, arguably the most difficult part of the challenge.

My main goal was to setup the simulation for learning, and potentially look into Nvida Isaac or Mujoco. Also, simulating the flexible cables is an entire different thing entirely so that would also take quite some time to ijmplemnt.

So once the toolkit came out, we realized that many things already were available that we tried to implement before. The toolkit already came with a fully working and controlable UR5E plus gripper (albeit a much simpler one), together with the entire frame work and taskboard already simulated in Gazebo. We eventually decided to not go the Nvidia Isaac route, mostly due to the difficulty of running that on everyones machine, but also because we found out that the evaluation of the qualifying round was mainly done in Gazebo.

This meant that my role as chef simulation kind of got diminished as the full platform was already there. However, I do have an lot of perception experience from back in my Master's and Early Phd projects. Perhaps to some of the developers no-a-days my computer vision knowledge is perhaps considered 'old school', but I must say it was very satisfying to jump back into OpenCV and use those old musscles, and can very powerfull as well. 

## Taskboard detecting 

So initially I focussed on the first part of the task, which was detecting the pose of the taskboard and orienting itself above the location the ports. The idea was that if we are able to detect the full pose of the taskboard, we will be able to do the logic later of where the actual components were. This was all to retrieve the actual 3D pose of the port that we needed to have the gripper to move towards and get as close as possible so that the reinforcement learning policy would take over.

First thing I thought about is to make a binary image of the taskboard by tresholding it's gray scale image related to it's much lighter background. Then with some clean up of the artifiacts (like the light lines on the back) by erroding and dillating the binary image with morphological filters. Then to retrieve the edges, and fit lines on those edges with houghlines and ransac filtering. These lines, when they intersect they will 4 corners, even if those corners could not be seen by the camera because it is too nearby. Then, the flatsquare was projected using the camera info information using the SolvePnP algorithm, to retrieve those points in 3D space and hence getting the 3D pose of the taskboard. Ofcourse you'd have rotation ambiquity as well, so luckily there was also a nice mageneta logo that gave some clarity on that too. 

On a clean, empty taskboard, this usually works pretty well on a single camera, however on a more cluttered taskbaord with nicc ards you'd find more squares then only the taskboard. So the projection would be validated it by the multiple cameras (because there were 3), if all 3 cameras were able to detect the taskboard at the same place within a certain tolarance, it will at least confirm that it's detecting it propeperly. Perhaps a kalman filter would have been sufficient, but from all the detection it has done there was maybe only 1 out of an 100 that it saw a different square somewhere else, and if it did detect it was usually on to an acuracy of milimeters which was definitely good enough!

The port detections itself was done in quite a different technique, namely the use of yolo lfor the prot detection. This was the task of my team mate Yara, which handled all of the training franework. Basically she setup the the simulator to generate all possible positions of the taskboard and retrieved the ports location in those images by using the available ground truth transforms and sementic fill in clustering. You should defintiely ask her for the specifs But ofcourse, these detection where only done in 2D on a single camera. However that the pose of the taskboard is known, we can project the taskboard zones. And if you can imagine a ray beaming from the camera through the component, and intersect that beam with the projected zones, then viola, you have a 3D pose! 

## The pre-insertion method

So the taskboard and component detection solved about 95 % of the total movement, namely positioning the arm directly above the port for the trained hilserl policy to take over. In order for the robot to determine the full taskboard pose, it was necessary for it to rotate the camera into the direction where it is sheeing that binary image (or blob). And that took extra time and also an risk for the cable to get tangled and stuck. 

Eventhough I really like the solution we had, in the end we at one point to a shot to go for a more simpler approach, namely getting the 3D pose of the components by simply intersecting with a plane offset from the table plane. Since it was posible to also infer the orientation of these components, that should be possible GIVEN that there were only a few ports to see. But with those restrictions, it would be possible to have a oneshot component detection that was 

The rules for the qualifying round indicated that the target components were visible in at least one of the cameras attached to the robot arm. So after we tried the more elaborate taskboard detection in the preinsertion strategy, we then tried an hybrid approach. If there where more ports than a certain threshold, it will use the default, rotating but full pose taskboard detection. If it wouldnt see as many ports in its view, it would use the simplied, taskboard detecting skipping and straight from yolo to 3D detector right away.  

Ofcourse, we were not able to see an video or logs from the online submission, but from purely the time the arm took from completing the task we could already tell, that it was always seeing fewer ports and therefore selecting the easy 3D compoenent approach. That's when we fully skipped the default taskboard pose search approach (nooo my darling!) and took the full risk of onloy the lightning fast, one  shot component detection that we could fully optimize for speed to get the plug as close as possible for hilserl to take over. And that paid off, as we ended up on the 10th spot out of the 160 teams participating for the qualifying round

For the phase-1 round (the round after the qualifying round), we decided to go for a different approach for the pre-insertion approach. We were allowed to use Flowstate, the development envirnoment made by intrinsic, which had a lot of skills available for us to take over the initial taskboard and component detection already. So then we decided to focus on the one element that stayed consistent trhough the entire compition, the plugin insertion policy with HILSerl.

## HIL-SERL for preinsertion

So anyone that has worked with reinforcement learning knows that ... it ... takes ... a ... really ... long ... time! So that would mean that we either had to wait for weeks for policies to appear, or had a similator that was able to run a lot of simulations in parallel. Luckily, our team mate Jennifer Beuhler proposed that we used HIL-SERL, Human in the loop Sample-Efficient reinforcement learning. Setting up the very intergrate framework and learning environment was all from her hardefforts, and the initial policies were completely trained by her. I was glad I was able to take some of it over at the end of it all.

So for reinforcement learning, it's all about the developing a policy that is able to determine the 'next right moves' based on the current state. This policy is trained in en envirnoment which has an indcated reward function. In our case, the reward function was only given when the plug is fully inserted. Ofcourse, to come here completely by chance will take a long time , Maybe even never because that is how chance works, and if it never hits the reward it will just not learn. So you can either engineer the reward function (closer it gets to the port the higher reward), or have a human show the arm how to do it to get to that reward quicker. 

So the approach is as follows, you would record a set of 20-50 demostrations teleoperating the robot arm to insert the plug successfully. After that the training starts, where you would have both the learner and actor active. It will use in part the demostrations you have recorded before, but also it will take into account any intervening, where you would control the gripper to directions and orientations where it would more likely succeed and get that juicy reward. You might first want to even try to get the gripper to do the initial insertion already, just to increase the changes of it 'accidently' moving it allthe way (or at least the base line policy trained on the demostration data). And you can let the robot 'ride without wheels' for alonger duration of time as you go along. Mostly, here I found that choosingthe teleoperation device is extremely important.


Training the robot arm in gazebo for inserting both plugs took a good 2-3 hours of intense training and intervening, before the robot arm was starting to do full insertions on their own. After that it was a matter of tampering off, even be 'distrubtive' with the interventions, or increasing the scene randomization in the scene. So if the policy seem to be successfful for a good duration of time without any intervening, that is the time to start selecting the policy to try out in the 'real world' and with real world we still mean simulation.



## In the end, everything really matters

So for the second phase we sadly didn't qualify for anymore. Unfortunately it is hard to say what was the actual cause, and where we divirted from a potential winning path, as both the new preinsertion as extra trained policy didn't make the cut. The phase 1 challenge was signficantly harder as we had to plugin in 5 cables (so 10 insertions) instead of just one plug at a time. However, HIL-serl is a technique meant for real arms and meant to be trained in live. However, as the competition went along, it did became clear that we probably wouldn't be able to receive that special treatment with 9 other teams competing. So perhaps we should have more focussed on the immediate transferablilty of the simulated policy to real life, and that is perhaps not something that has been done with HIL serl (yet)! But these are all just assumptions. 

None-the-less, this definitely didn't mean that we didn't leave this competition empty handed. For me personally, this was the first time that I ever worked with a manipulator, even in simulation. Sure I've learned about the theory, and embedance control during my masters, but never applied. Also this was the first time that I have worked with applied, 3D reinforcement learning, other than the simple flat 2d grid exercises we had to do during my Masters. But it was also a way to get back into touch with my old friend OpenCV that I used to use so much back in the day and now definitely will get back into it.

Moreover, working together as a team as of equals together to solve a difficult robotics issue like this, has been the most satisfying experience of all. Working together with Yara and Jennifer has been truely a pleasure, even through the stress and hardships of the many deadlines, we did deliver something that we all did together as team b-robotized. I hope that I'll be able to be part of many of these teams in the future in my consulting days to come.