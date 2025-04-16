---
title: Navigating Through the Robotic Simulation Landscape
date:
  created: 2025-04-17
  updated:  2025-04-17
draft: true
categories: 
    - robotics
authors:
  - kim
comments: false
links:
  - Best-of-simulation list: https://github.com/knmcguire/best-of-robot-simulators
  - Ekumen blogpost about simulation: https://ekumenlabs.com/blog/posts/accelerate-robotic-dev-sim/
  - Arxiv Survey paper for Aerial Robotics Simulators: https://arxiv.org/abs/2311.02296
  - Best-of list template (to make your own): https://github.com/best-of-lists/best-of
  - Simulation Tools in ROS: https://github.com/ros-simulation
  - Best-of-robot-simulators list: https://github.com/knmcguire/best-of-robot-simulators
---

<script data-goatcounter="https://knmcguire.goatcounter.com/count"
async src="//gc.zgo.at/count.js"></script>

[![image](images/best-of-robot-sim.png){width=100}](simulation_landscape.md)


_In this blogpost I explain how I tried to figure out in which simulator I should invest some of my project development time in. Little did I know of the very deep rabbit hole presented itself for me and I dived right in! Did it help me with my choice? A little, but perhaps I've created something that is perhaps even more useful: a best-of-list of robot simulators._

_Enjoy!_

<!-- more -->
___

It's been less than a week ago that I've announced I'll go freelancing as a robotics engineer. This means freedom, independence, no one telling me what to do! ... yes that might be a problem... because if knowone tells me what to do, how do I know what is important to know, and to learn? One part is ofcourse what I'm interested in, one part is what the client needs, and most imporatntly, of which tools are already available out there. That is something that I'll just need to determine myself by research.

So why focus on simulation? I've already worked on robotic simulation for the Crazyflie back at Bitcraze ([blogpost 1](https://www.bitcraze.io/2021/12/simulation-possibilities/), [blogpost 2](https://www.bitcraze.io/2022/03/updates-on-simulation-work/)) where I worked mostly with [Cyberbotics' Webots](https://cyberbotics.com/) and [Open Robotics' Gazebo](https://gazebosim.org/home), which are both awesome and big staples in robotics, however have some limitations in rendering capabilities and physics for fluid and airdynamics. Ofcourse this can be solved by making a plugin for better rendering  and physics engines, but which options are available for those?

## What is a robotic simulator?

That is what my husband asked me, and you know what, it is suprisingly difficult to explain. He comes from the physics and material science and their definition of the word 'simulation' is very different of how we view simulation, so the meaning or implementation is very different depended of which field you are from. Basically [the wikipedia page definition of a simulator](https://en.wikipedia.org/wiki/Simulation) is:

> A simulation is an imitative representation of a process or system that could exist in the real world

This is an extremely broad term and can stand for anything, from a pseudo random dice roll program to a finite element analysis of a steal beam, to a high fedelity rendering of a camera footages of a virtual drone. This is just to illustrate of how big the terms actually is!

And how about a simulator for robotic systems? For that I actually had a little bit of help by Gemini for this:

> A robotic simulator is a software framework that provides a virtual environment, often leveraging different physics/rendering engines and sensor models, to model the robot's behavior, its interaction and perception with the simulated world for design, evaluative or data-generative purposes.

That seems more like the definition that I'm the most familiar with robotic simulation.  There are some key words in there that will be probably important:

- **virtual environment** - To provide the scenario for the simulated robot to act in depended on the application, like a indoor building, forest, or lunar landscape
- **behavior, its interaction and perception** - The simulated entity should be able to interact and act upon that virtual environment or world, through it's simulated sensors and actuators
- **physics/rendering engines and sensor models** - To be able to simulate those interactions and perceptions, caused by the robots behavior, to model how an object will slip wile being grasped or the noise of the lidar ranges.
- **design, evaluative or data-generative** - To use this as a development tool, as part of continious intergration and assure quality or to collect data that can be used for AI training purposes.


For a more indepth explanation on the definition of robotic simulation and it's purposes I would very much recommend you to read the [Ekumen blogpost on robotic simulators ](https://ekumenlabs.com/blog/posts/accelerate-robotic-dev-sim/) and [watch their presentation at FOSDEM 2025](https://fosdem.org/2025/schedule/event/fosdem-2025-6252-accelerating-robotics-development-through-simulation/). This also helped me get some clarity in the definitions and I've learned a lot from it as well.

## Starting with simulators for aerial robotics

At ICRA 2023 when I still was part of Bitcraze, I've helped organizing the Workshop [the Role of Robotic Simulators](https://imrclab.github.io/workshop-uav-sims-icra2023/) with co-organizers Giuseppe Silano (CVUT), Chiara Gabelleri (TU Twente) and Wolfgang Hönig (TU Berlin). The original purpose of the workshop was to settle on an simulator for all aerial robotic application. What we got, where 16 papers of all different aerial robotics simulators build or assembled for different purposes. Instead, we choose to write a survey paper instead, which got published last year at Robotics and Automation Magazine.

> C. A. Dimmig et al., "Survey of Simulators for Aerial Robots: An Overview and In-Depth Systematic Comparisons," in IEEE Robotics & Automation Magazine, doi: 10.1109/MRA.2024.3433171 [:fontawesome-solid-file-lines:](https://arxiv.org/abs/2311.02296)

By the way, Guiseppe has presented this work at on of our Aerial ROS meetings in September last year so check out [the recording here](https://arxiv.org/abs/2311.02296). Moreover, if you happened to be at [ICRA 2025 in Atlanta](https://2025.ieee-icra.org/), on of the co-authors Joseph Moore (Johns Hopkins University) will present the paper at the Aerial Robots 1 session on Tuesday 20th of May at 10:20 local time.  

This survey paper, we collected 50+ simulators for Aerial Robotics alone, of which a subselection of about 10 where more properly evaluated. With that subselection I started my investigation of seeing which projects or underlying simulation I should try to learn more about, which helped me a lot as a starting ground.

But as I went through I saw that many of these projects are are not regurally maintained. Just an example, that Airsim (build on Unreal-Engine) is planned to be archieved and there will not be [continuing with the promised project airsim](https://www.businessinsider.com/microsoft-shutters-project-airsim-ai-strategy-openai-2023-10). Also some of these use the Unity game engine as well, but then I found out that the [Unity Robotics hub github](https://github.com/Unity-Technologies/Unity-Robotics-Hub/tree/main) seems very barren at this moment (seems like the robotics team got [laid off last year with the last mass firing](https://techcrunch.com/2024/01/09/unity-to-lay-off-another-1800-employees-representing-25-of-its-workforce/#:~:text=Just%20a%20few%20weeks%20after%20its%20most%20recent,improve%20its%20financial%20performance%20after%20a%20difficult%20year.)).

So... that doesn't really help me does it? I do want to go into a framework that healthy, well maintained and has .. well a development future in robotics. But I don't want to constantly do the same investigation again and again as it is very time consuming, and mentally draining.

## Generating a Best-of list

It all started when I updated [my website last February](first_blogpost.md/#how-did-i-make-the-website-and-blog) and for [my freelancing adventure](going_solo.md/#my-new-portfolio). I'm using [mkdocs](https://www.mkdocs.org/) for generating my website (and I think I've already expressed my love for it plenty of times), but I was amazed by their [plugin catelog](https://github.com/mkdocs/catalog). Anyone can make their own plugin for the framework and get listed here in this best-of-list. And the cool thing is, that it grabs the meta data from the github resposity in terms of stars, downloads, forks and activity, and makes a ranking of how well these projects are doing, fully automatic. So you can see immediately which are the most relevant and healthy projects to go for.

Fully inspired, I decided to make my own best-of list... of Robotic Simulators! And here is where the rabbit hole presents itself, since I dove in face first, not knowing how deep it was. But I'm just to curious and I'm a little bit of completionist. Ofcourse I have my limits with this, or else I would have still been playin Red Ded Redemption 2 full time to this day. But at least I wanted to go and research this to a point that I will be able to make my decision and that it might be useful for others as well.

So there you go, a [Best-of-list for robot simulators ](https://github.com/knmcguire/best-of-robot-simulators)

[![best-of-robot-sim](images/best-of-robot-sim.png)](https://github.com/knmcguire/best-of-robot-simulators)

This consists of more than 80 projects, which can be combinations of eachother and are both open and closes source (although the latter won't be correctly ranked obciously). Currently I selected 9 categories:

* **Generic Open-Source Robotic Simulators**: Generic simulators, tools or SDKs made for robotics which are open-source
* **Robotics Simulators that are closed source**: Generic simulators or tools made for robotics that are closed source
* **Physics Engines**: Physics Engines that simulate multi-joint dynamics, gravity etc
* **Rendering Engines**: Simulator frameworks made especially for aerial robotics
* **Game Engines**: Robotic simulators build for other domains like automotive or maritime
* **Aerial Robotics Simulators**: 3D engines made for games but can be interfaced with robotic frameworks
* **Domain Specific Simulators**: Simulations made for training for AI-agents like reinforcement learning
* **AI-Training Simulators**: Simulations made for training for AI-agents like reinforcement learning
* **End of Life**: Simulators that are announced EOL, are obviously no longer maintained (longer than 5 years) or have been deprecated

So ofcourse these categories are maybe not incapsulating all the intricacies of what a robotic simulators, and I'm very much aware that perhaps aerial robotics is over represented, but that is why I've made this blogpost. If anyone has suggestions on improvement, a new simulator or moving a simulator somewhere else, please let me now as [a github issue](https://github.com/knmcguire/best-of-robot-simulators/issues). Also it is not possible to add simulators in 2 categories except for renaming them, like I've done for the O3DE game engine, so I might be able to do with some of these as well. 


## So, did the list served it's purpose?

Did this list help me to make a decision to select on which robotics simulator to focus on next? Yes. Was I able to make this decision with a bit less effort then diving full blown research? Definitely. But that is okay, because this best-of-robot-simulators is perhaps something that can help others like me as well. 

So for me, I decided that I'll dive in further into [O3DE the Open 3D engine](https://o3de.org/) for it's high fedility features. Since the city that I currently live in, Malmö Sweden, is quite big in Game development, it made sense for me to go into a project made from a game development perspective... and is open source. However, I'm also very aware on the possibilities of  Nvidia Isaac Sim, and keeping a close eye on the release of the [Open-source Physics Engine by Nvidia called Newton](https://developer.nvidia.com/blog/announcing-newton-an-open-source-physics-engine-for-robotics-simulation/). Although I'm a bit warry about the commitment of bigger companies on supporting robotics (because Unity Robotics hub and Airsim), Nvidia has made a right step in the direction with the start of open-sourcing their PhysX engine with version 5 and working together with Open Robotics' Gazebo and Robotec's O3DE, to standarize simulation interfaces, so there is hope!

Robotec has given a [FOSDem talk](https://fosdem.org/2025/schedule/event/fosdem-2025-6035-o3de-creating-realistic-simulations-with-open-source-game-engine/) about O3DE back in February, which I'll now go and watch again to get started (next to updating my c++ skills). Wish me luck!