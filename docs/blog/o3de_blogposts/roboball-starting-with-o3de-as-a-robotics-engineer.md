**This is a placeholder for the original blogpost to be found here: [https://o3de.org/roboball-starting-with-o3de-as-a-robotics-engineer/](https://o3de.org/roboball-starting-with-o3de-as-a-robotics-engineer/)**

Hi! Let me start by saying I’m not a game developer, I’m a robotics engineer. But, I’ve spent most of my career working with robotics-specific simulators like Gazebo and Webots and during COVID, I had the chance to take courses in Unity and Godot and experiment with VR on my Oculus Quest. That is where I did find out that there are so many similarities between robotics and game development. 

You can see a simulator as a game for robots, but both fields use modular frameworks where different components connect together to make everything work. That is basically one of the building blocks of the Robotic Operating System (ROS), which can be seen as an actual robotics engine. 

The Best-Of-Robot-Simulators list
With so many robot simulators to consider, I’ve started going into the rabbit hole earlier this year and made a “best-of robot simulators” list that ranked them by maintenance and community activity. That’s when I saw a familiar name at the top: O3DE. I’d actually heard about it at FOSDEM 2024, where Robotec presented in the Robotics and Simulation Devroom (you can watch it here). Seeing it ranked so highly on the list, I decided to take the leap and learn the engine.

In April, I started playing around with O3DE using their Ping Pong example. But being me, I couldn’t just follow the tutorial the easy way… I decided to try it on a beta version of O3DE that was still in testing (version 25.05 at the time). Looking back, maybe not the smartest move for a complete beginner! It made it really hard to tell the difference between actual bugs and my own incompetence. But I figured experienced developers probably wouldn’t test the beta this way, so at least I could catch some real bugs? I was inspired by the yearly Gazebo tutorial parties where developers of all levels go through tutorials together to make sure they still work. Hopefully I didn’t annoy too many core maintainers in the process! 

After finishing the Ping Pong tutorials, I decided to try live-streaming my learning process on Twitch. How hard can it be? Turns out… pretty hard! I’m definitely not a natural at it. People on Twitch somehow manage to constantly narrate what they’re doing, but when I focus on a problem, I get completely absorbed and go silent. Not exactly exciting content for a stream! It was honestly pretty stressful, so over the summer I decided to take a different approach and work more project-style instead.

Making a Ball Bounce!
That’s when I started the RoboBall project. It might sound similar to another RoboBall project, but it was actually inspired by something closer to home: an autonomous bouncing ball toy for my cats ! The idea was that it would keep bouncing and keep them entertained. Unfortunately… my cats were not impressed. But it gave me an idea: I couldn’t hack the actual robot ball, but I could definitely simulate it in O3DE!

To make the streaming work better for me, I decided to prepare everything tutorial-style. This gave me structure and something concrete to work through, which made the whole process less stressful.

So with the Roboball project, I was able to show the project in different phases:

I began with just making a ball entity in the default level, showing how to add meshes and create a custom bouncy material. 
Next came Lua scripting and keyboard inputs to make the ball controllable, plus a camera rig that follows it around as it moves. Here is where I learned more about O3DE’s scripting capabilities.
Then I played around with collision detection and implemented collision-based impulses. Instead of relying on unrealistic bouncy materials, I wanted actuators that felt more like how a real robot ball would bounce around.
Finally, with walls and a goal in the environment, I showed how to implement goal-seeking behavior and obstacle avoidance. The result? A fully autonomous robot ball that jumps around hitting targets… or maybe running from my virtual cats!
This project was an incredibly effective way to understand the intricacies of O3DE. It touched on asset creation, physics, and scripting all at once, and I definitely feel I’m in a much better place to implement more complex things now. Check out this gif of the end result:

Video Player

00:00
00:10


I also got a chance to really work with Lua. While I did enjoy Script Canvas for visual programming, I found that for simple if-statements and state machines, Lua was easier and required fewer “lines” compared to “nodes” to make the robot ball autonomous. Both have their place, but Lua felt more natural for this kind of logic.

Once the project was done, I published it online and asked Claude.ai to help me polish it into proper tutorials. I’ve also edited the streams to be viewed on my IndieRobot youtube channel to rewatch the project for anyone interested. I’ve written the tutorial to specifically aid me in the streams, but I do think you should be able to follow along as well. And perhaps I could rewrite this as a more fleshed out tutorial for the O3DE website if more people would be interested in it (and if you do, please let me know).

Meeting the community at Open Source Summit
Last august I had the privilege to be invited to give a keynote speech at the Open Source Summit in Amsterdam this year, which is an event organized by the Linux Foundation. I shared the stage with my good friend Ramon Roche from the Dronecode Foundation and we told the story about Mary, an intern at a robotics company. The story was how she was able to develop an autonomous warehouse inspecting an aerial robot, and how she used all kinds of open source projects from PX4, to ROS and OpenCV, all the way to O3DE for simulation! Watch the keynote.[/vc_column_text][/vc_column][/vc_row]


1
2
3
Previous
Next
To Conclude
From the Open Source Summit and my experience learning O3DE, what really stood out to me throughout this whole process was the community. O3DE’s Discord is incredibly active and genuinely helpful to beginners like me, even when I was probably asking obvious questions. Everyone was respectful and genuinely interested in whatever projects beginners shared. This is yet another reminder of how great it can be to work together on open-source projects.

So far, my experience with O3DE for developing games and simulations has been quite positive, and the program has been very stable. As a tool, I would already recommend it quite a bit. But if anything will bring me back to O3DE for more projects, it’s this aspect—a helpful, well-organized community that makes you feel welcome. I now feel confident enough to tackle my next challenge: trying out the ROS2 gem. Hopefully I’ll find the time to do so soon!