---
title: "ROS 2: Across the Windows-Verse"
date:
  created: 2025-06-02
  updated: 2025-06-03
draft: true
categories: 
    - robotics
authors:
  - kim
comments: false
links:
---

<script data-goatcounter="https://knmcguire.goatcounter.com/count"
async src="//gc.zgo.at/count.js"></script>

[![image](images/win_gz_ros2_teleop_wsl2_rqtrviz2.png){width=100}](ros2_across_the_windowverse.md)


_Three months ago that I went head-first in on full on Windows Development. Have I gone screaming mad already? Well... no actually! I managed to establish a handy workflow between the ROS native windows install and WSL2. This blogpost shows that process of what I've set up._

_Enjoy!_
<!-- more -->
___

About 3 months ago I made the 'drastic decision' to go full windows. I only have a half a terrabit onmy laptop, which is not great for gaming (or ROS/simulation) and I just didn't want to switch OSes on my dualboot. I would need to decide what I wanted to do on that day, like core c++ or ROS development or graphics CAD design, to not destrubed to much of my workflow to contsantly switch. Since the situation of WSL2 on windows has drastically improved, I decided that that will be the fall back in case I can't get things to run on windows natively.

In [this last blogpost in March](https://www.mcguirerobotics.com/blog/2025/03/14/robotics-on-windows-are-you-mad/), I have found already that the new install instruction for ROS 2 that used the [Pixi package manager by Previx.dev](https://pixi.sh/latest/) already made things soooo much simpler than it was before (I litterarly use Pixi for everything right now). Back then, I could only install ROS 2 jazzy from source, but when it ran on the command prompt and I was able to make it communicate with the WSL2 Ubuntu 24.04 jazzy with a simple talker and listener. And when I was able to launch an urdf model from WSL2 and actually display it on RVIZ2 on native windows, I remember myself being almost like a proud parent. 

<center>![One terminal in the windows sub system startin up a robot description and ROS 2 natively on Windows running rviz2](images/rviz_wsl_windows.png)</center>

Now that Kilted Kaiju came out about a week ago, I wanted to see how far I can push this further. I love WSL2 and it helps me out at a daily basis, but the Gui handling is just very janky and I have no control over what in WSL2 I want my second Nvidia graphics card to care about. So my goal is: (1)Gazebo Ionic to run natively on Windows 11, (2)run the ROS 2 (kilted Kaijue) - Gz Ionic bridge and other ROS 2  on WSL2 and (3) debug using RVIZ2 and RQT back on native Windows again. Why? Because it's a challenge!

> I've written this blogpost in a tutorial like style, so you can try to follow along. Having said that, it's all super experimental and you WILL encounter bugs. Be prepared to do some code digging and fixing yourself :smile:

## Gazebo Ionic on Windows 11

Since I didn't want to do any core development on Gazebo itself, I went through [the Binary installation instructions](https://gazebosim.org/docs/latest/install_windows/). Here they recommend using the package conda managment system, which I have tried during the gazebo ionic testing tutorial party and that works fine, but this time I wanted to use pixi! Instead of installing the libgz-packages one by one, I could add them to the pixi.toml file as depenencies with right numbering with the right version. I've added the [pixi.toml file as Gist here](https://gist.github.com/knmcguire/c5b14909cf76cc80593c98ddebef51c6).

The cool thing about pixi, is that you can also make use of [multiple environments](https://pixi.sh/latest/tutorials/multi_environment/). So I've added the dependencies of both Gazebo Ionic and Gazebo Harmonic (which is the latest Long term release). And than switching between Gazebo versions is as easy as:

```console
# Harmonic
pixi run -e harmonic gz sim
# Ionic
pixi run -e ionic gz sim
```
Mind that for Windows there is still a bug that requires me to start the server (`gz sim -s`) and gui seperately (`gz sim -g`), but luckily it is all in just one line now to activate both the conda/pixi environment and run gazebo, so it's not that much of an hassle. I have heard through the grapevine that soon (at least for the upcoming Gazebo Jetty), this dual startup procedure will no longer be required. And the nice thing to make it even more simpler, you can put Gazebo Ionic as the default environment, so no `-e ionic` is even requirement if you know which simulator version to 

So I looked at an older simulation model of the [crazyflie made](https://github.com/bitcraze/crazyflie-simulation) for Gazebo harmonic and see if I got it to fly (in command prompt):

```cmd
git clone https://github.com/bitcraze/crazyflie-simulation
set GZ_SIM_RESOURCE_PATH="/FULL/PATH/TO/crazyflie-simulation/simulator_files/gazebo/"
pixi run gz sim -s worlds crazyflie-simulation/simulator_files/gazebo/worlds/crazyflie_world.sdf
```

If you add the Teleop widget (3 dots from top right) and add `/crazyflie/gazebo/twist/command`, you can control its speed in both vertical and linear direction with the [multicopter velocity control plugin](https://gazebosim.org/api/sim/8/classgz_1_1sim_1_1systems_1_1MulticopterVelocityControl.html). I also needed to add pixi's ruby.exe (what runs gazebo) to the windows graphic driver handler (System>Display>Graphics - Custom settings for applications on Win11)


<center>![One terminal in the windows sub system startin up a robot description and ROS 2 natively on Windows running rviz2](images/windows_gz_sim_crazyflie.png)</center>

Unfortunately the controller of the simulated nano quadcopter is not tuned to perfection, so whenever I go forward or rotate, the drone drops in height. I'd like to fix that (for now) with an external ROS 2 controller with the ROS 2 gazebo bridge. 

## ROS 2 Kilted Kaiju on WSL2

Since the ROS 2 distribution for windows doesn't come with the ROS gazebo bridge by standard yet, I decided to work on that on WSL2. I first thought that I'll need to find a way to build the ros-gz-bridge on windows natively, which seems to require an source installed of Gazebo ionic, but I don't want to get into that now. So I've installed [ROS 2 Kilted Kaiju ](https://docs.ros.org/en/kilted/Installation/Ubuntu-Install-Debs.html) with the full desktop version so it comes with Gazebo ionic laready. Technically you could do a barebone-install and only add the Gazebo ROS packages, but as you already noticed, I'm a bit lazy today ;)

Luckily, I found out that gazebo topics can be read out by a Gazebio Ionic installation on WSL2! . With the quadcopter simulator still running on windows and in the air, I could just write 

```
gz topic -t "/crazyflie/gazebo/command/twist" -m gz.msgs.Twist -p "linear: {x:0 y: 0 z: 0.0} angular {z: 0.5}"
```

As before, the quadcopter drops down, so time to add that ROS2 gazebo bridge and simple control node! So in WSL2 with a full-desktop install 


```bash
cd ros_ws #or how you call your ROS build space
mkdir src
cd src
git clone https://github.com/knmcguire/ros_gz_crazyflie src/ros_gz_crazyflie
source /opt/ros/kilted/setup.bash
colcon build --symlink-install
source install/setup.bash
ros2 launch ros_gz_crazyflie_bringup crazyflie_simulation.launch.py gazebo_launch:=False
```

and then in another bash terminal in WSL2 run:
```bash
source /opt/ros/kilted/setup.bash
ros2 run teleop_twist_keyboard teleop_twist_keyboard
```

Now there is a seperate ROS 2 node with a simple take off service that reacts on 't' input in the ROS2 teleop node if still on the ground. Also it is possible to move it around using the I/J/L/M keys on the keyboard. It's set to do an non-holonic movement of the drone, such as a ground vehicle but you can change the control node to your liking as it is mostly experimental.

<center>![One terminal running teleop on WSL2 and Gazebo running on gazebo native with a quadcopter model](images/wsl2_ros2_gz_bridge.png)</center>


So now we have ROS2 on WSL2, controlling the drone gazebo simulation on Windows native which is really cool already! But now I want to check the topic, nodegraph and the Transforms in RVIZ2, which I don't want to do in WSL2 (yanky guis), as there are plenty of things I'd like to update with that. Let's go to the ROS2 installation natively on windows 11!

## ROS 2 Kilted Kaiju back on Windows 11

So now that it is possible to install the ROS 2 Kilted Kaiju binaries in Windows 11 via [these instructions](https://docs.ros.org/en/kilted/Installation/Windows-Install-Binary.html). Currently it needs to be fixed to a directory in C:/pixi_ws/but hopefully we will be able to fix that soon with this [ROS2 github ticket](https://github.com/ros2/ros2/issues/1675). 

Once installed, to the installed ROS2 directory, open up a pixi shell and source the ROS 2 kilted Kaiju distribution:
```bat
cd C:/pixi_ws
pixi shell
call ros2-window/setup.bat
rqt
```

Open up the plotter (rqt>visualisation>plot, might need to install a plot library which you can add with `pixi add`), and you can look at the height topic for instance `/crazyflie/odom/pose/pose/position/z`. Go back to the teleop node on wsl2 (or you start on on Windows native), and see what happends if you control the height with keys `t` and `b`.


In another terminal open up Rviz2 and open up a transform

```
call ros2-window/setup.bat
rqt
```

Since all the gui's are in windows natively, you have more control about their resizing, including the nice 2 x 2 format for a nice overview. Here you see a screenshot where I have the quadcopter in gazebo (windows native), Teleop and contrl (wsl2) and both rqt plotter and rviz2 (windows native) open on the same page. 

<center>![4 window view of a quadcopter model in gazebo (windows), ROS 2 Teleop (wsl2) and both RQT and RVIZ2 (Windows )](images/win_gz_ros2_teleop_wsl2_rqtrviz2.png)</center>


## The Full Monty and conclusion


So if you look at the full rosgraph it looks pretty awesome. And it is quite handy that I can control the gui windows more easily. This will be a improvement to my workflow of developming on ROS2 on windows.

<center>![4 window view of a quadcopter model in gazebo (windows), ROS 2 Teleop (wsl2) and both RQT and RVIZ2 (Windows )](images/rosgraph_win11_wsl2.png)</center>

Having said that, there are still things that can be improved:

- Having ROS 2 running on both natively and WSL2 takes up some resources and is not efficient
- I still have to manually start gazebo from Windows, as that can't be done from a launch file from WSL2
- Gazebo still has some bugs for the windows, but that is to be expected as the maintaince team notes it at 'experimental' (I'll make sure to make GH issues of all of these.)

Nevertheless! I'm still quite excited for other possitilities that can come with this! Let's see if I can also get this to work with other simulators as well like Nvidia Isaac Sim or O3DE engine.

Here is a video compilation of the full run through of my WSL2-Win11 Kilted-Ionic tryout. I will also present a run through at my [Indie Robot Twitch stream of tomorrow](https://www.twitch.tv/indierobot/schedule?seriesID=b4d96240-af58-44ea-9262-76d739c8351b), so make sure to tune in!

TODO: VIDEO yet to come!