---
title: "ROS2 on windows updated version"
date:
  created: 2026-05-07
  updated: 2026-05-07
draft: true
categories: 
    - personal
authors:
  - kim
comments: true
links:
  - Six Months Down The Freelancing Road: https://www.mcguirerobotics.com/blog/2025/10/12/six-months-down-the-freelancing-road/
  - Flying Solo - the Start of my Robotics Freelancing career: https://www.mcguirerobotics.com/blog/2025/04/10/flying-solo/
---


## WSL2

### Install a WSL2 distro

```
wsl --list --verbose 

Wsl --list –online 

wsl --install -d Ubuntu-26.04 --name wsl-u2604-ros2 
```

```

wsl --unregister wsl-u2604-ros2
```

Then fill in your own user name (I use Kim) and choose a password (helloros)


Then follow https://docs.ros.org/en/lyrical/Installation.html to intall full dekstop ros

THen [install the ros gazebo bridge](https://gazebosim.org/docs/latest/ros_installation/)

```

sudo apt-get install ros-lyrical-ros-gz
```

Then try out controlling a simple robot with [gazebo ros2 bridge example](https://gazebosim.org/docs/jetty/ros2_integration/#visualize-in-rviz)


Terminal 1
```

ros2 launch ros_gz_sim_demos sdf_parser.launch.py rviz:=True
```
Terminal 2
```
ros2 topic pub /model/vehicle/cmd_vel geometry_msgs/msg/Twist "{linear: {x: 5.0, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: -0.1}}
```

You might see some errors depended on your system. For instance I saw:

 
```

[gazebo-1] libEGL warning: failed to get driver name for fd -1 

[gazebo-1] 

[gazebo-1] libEGL warning: MESA-LOADER: failed to retrieve device information 

[gazebo-1] 

[gazebo-1] libEGL warning: failed to get driver name for fd -1 

[gazebo-1] 

[gazebo-1] MESA: error: ZINK: failed to choose pdev 

[gazebo-1] libEGL warning: egl: failed to create dri2 screen 
```


Then you will need to install in wsl2
```

sudo apt install -y mesa-utils libgl1-mesa-dri
```

and add the following to your bash

```
export QT_QPA_PLATFORM=xcb 
export GZ_RENDER_ENGINE=ogre 
```