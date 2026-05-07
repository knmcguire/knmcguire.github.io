---
title: "One year of freelancing: I guess we're doing this for real now!"
date:
  created: 2026-05-07
  updated: 2026-05-07
draft: false
categories: 
    - personal
authors:
  - kim
comments: true
links:
  - Six Months Down The Freelancing Road: https://www.mcguirerobotics.com/blog/2025/10/12/six-months-down-the-freelancing-road/
  - Flying Solo - the Start of my Robotics Freelancing career: https://www.mcguirerobotics.com/blog/2025/04/10/flying-solo/
---

<script data-goatcounter="https://knmcguire.goatcounter.com/count"
async src="//gc.zgo.at/count.js"></script>

[![](images/kim_aichallenge.png){width=100}](freelancing_1year.md)


_A full year into freelancing, and yep, we're officially doing this for real now. In this post, I'm sharing what changed after setting up my company, what projects and open-source things are currently on my plate, and what I'm still learning the hard way about balancing contracts, content, travel, and my sanity._


<!-- more -->
![image](images/kim_aichallenge.png){width=500 .center}
*<p style="text-align: center;">Working on the AI for industry challenge in my new office and setup.</p>*

## Officially started McGuire Robotics

In my [six-month blog post](freelancing_6months.md), I mentioned I might take the next official step. Back then I was freelancing through an intermediary company, which was great for trying things out without immediately diving into all the legal/admin setup needed in Sweden.  

Now that I'm much more sure I want to stay independent and self-employed (and after taking a business course in Swedish, no less... don't ask how much I actually understood), it was time for phase two: officially starting **McGuire Robotics AB**.

One question I got a lot was why I chose an **aktiebolag (AB, similar to a Ltd)** instead of an **enskild firma (sole proprietorship)**. I had a couple of reasons for that.  

First, I like having separation between me and the business, both mentally and legally. In robotics consulting, there is real risk if something goes wrong in software integration, and I didn't want to be personally exposed to all that liability. Yes, insurance and contracts help, but I still wanted that extra layer of protection. I've also heard from both Swedish and international clients that they generally prefer working with limited companies for the same reason.

Second, if I ever want to grow and hire people, I want the structure in place already. If I decide to build products, develop games, or apply for certain grants (which are often limited-company only here), I can do that. The sole proprietorship route felt a bit too restrictive for my longer-term plans.

That said, I won't lie: setting up a limited company required **a lot** more paperwork and admin. I hired an accountant and a lawyer for support, so I definitely wasn't doing it entirely solo, but I still had moments of "is this really worth it for a one-person company?"  

Now that this part is mostly behind me and the future options are still open, my answer is: yes, absolutely worth it.

## Projects so far?

I've done a mix of assignments so far, ranging from R&D to implementation work. I can't share everything publicly, but I can share a few:

I completed an investigation for the [Dronecode Foundation](https://dronecode.org/) about the PX4 simulation ecosystem. The goal was to understand who uses the stack, for what applications, and what users feel is currently missing. That turned into a full report with survey results and recommendations for future development priorities. You can read it [here](https://www.mcguirerobotics.com/px4_sim_research_report/), and I also gave a presentation at the [PX4 Developer Summit 2025 in Atlanta](https://youtu.be/zGxuXFUkEnk).

Early this year, I also joined [b-robotized](https://en.b-robotized.com/) as an external contractor for the [AI for Industry Challenge](https://intrinsic.ai/events/ai-for-industry-challenge). This is consuming most of my days right now, with the submission deadline around the corner. Honestly, the only reason this blog post got written today is because I had a few hours of forced low-internet-quality time on the train. Otherwise, I'm usually staring at logs and praying for the robot arm to detect the task board and plug in the cables correctly. The competition is hardcore, but also a huge learning opportunity since I hadn't worked with manipulators before. Would I take on manipulator assignments after this? Ask me again once the challenge is over :sweat_smile:.

## Managing my project workload

One of the biggest lessons from this year, and something I'm definitely still learning, is workload balance. When I started, I had quite a lot of time for personal projects and occasional blog posts. Once client assignments started coming in, all of that space disappeared quickly. Even though I'd set a clear goal to keep room for creativity and learning, that plan collapsed as soon as pressure and deadlines entered the scene.

This is a very real freelancer problem, and I've heard many burnout stories from independent colleagues. Most of it comes down to having too much on your plate, and I'm definitely guilty of that too. Last year I traveled too much, tried to keep regular content going, and juggled 2-3 assignments in parallel. That's simply too much, and I'm not built for aggressive context switching (not exactly breaking news, but now there's confirmation). What I enjoy most, both in client work and personal projects, is dedicated deep-focus time: getting fully absorbed in something mentally challenging (or just really fun to nerd out on). I can happily obsess over one topic for weeks. That's also when good blog posts happen, and those often lead to future assignments, so yes, this needs to be planned in on purpose.

## What happened to the content!?

Yes... see the section above. Last year I tried to keep doing Twitch programming streams around O3DE and robotics builds. Doing that consistently while under pressure from multiple projects is rough, and for me it drained both creativity and motivation. So the short answer is: I just didn't have the energy to stream, write posts, make videos, and deep dive all at once.

Of course, I'm self-employed now, so I need to be realistic. If I could spend 100% of my time on open source and personal projects, I absolutely would. But... I also like getting paid. Even if I choose assignments I enjoy, there's still a difference between what you personally want to build, what helps the community, and what the client needs right now. Finding that balance is difficult, but important. The content that performs best for me usually comes from dedicated focus blocks. My [ROS 2 on Windows post](windows_with_robotics.md) got a lot of traction, and the [best-of robot simulators list](https://github.com/knmcguire/best-of-robot-simulators) passed 1,000 stars and even generated leads and assignments.

A wise, bearded, bald man from an [certain robotic newletter](https://www.weeklyrobotics.com/) told me once:  

> "As a freelancer, your main job is not your contracts, but the content creation that generates the leads."


## Going deeper into open source

My ROS 2 on Windows work also led to something very cool. Since the topic got traction, I was asked by the [Open Robotics infrastructure team](https://docs.ros.org/en/rolling/Governance.html) if I wanted to join. I went through the mentorship process and I'm now an official committer in infrastructure. My main focus is improving ROS 2 on Windows 11, but over time I hope to contribute more broadly across infrastructure topics too.

I'll also be co-mentoring two Google Summer of Code students: one on improving the [colcon mixin repository](https://github.com/colcon/colcon-mixin-repository) together with Scott Logan, and one on [performance test CI integration](https://github.com/ros2/performance_test_fixture) together with Skyler Miedema. Both are very infrastructure-heavy projects, which makes this a great way to get deeper into the mechanics of the ecosystem. Luckily, the ROS 2 summer release cycle will be active then, so maybe people will forgive me if I break things :stuck_out_tongue:. Oh, and did I mention I am also co-lead on the [ROSCon Global 2026](https://roscon.ros.org/) program committee in Toronto this year? 

One thing I noticed here too: it's very easy to overcommit when you want to be helpful. I wanted to spend one day a week on open source/infra, and in practice I kept saying yes to too many things. I should schedule this work on purpose, not squeeze it between tasks. Ideally not in parallel, but in dedicated project blocks, for both open source projects and my freelancing commitments.

## Traveling worth it for networking?

In the last half year, I definitely traveled a lot: [Open Source Summit Europe](https://events.linuxfoundation.org/archive/2025/open-source-summit-europe/) in Amsterdam in August, [ROSCon UK 2025](https://roscon.org.uk/2025/) in Edinburgh in September, [ROSCon 2025](http://roscon.ros.org/2025) in Singapore in October, the [PX4 Developer Summit](https://events.linuxfoundation.org/px4-developer-summit/) in November, and [FOSDEM](https://www.fosdem.org/2026/) in Brussels in January.  

At each of those, I had either organization work or one (or more) talks. They were all super valuable, and I'm happy I did them, but in hindsight I also shouldn't be too hard on myself that other things slipped, like content creation. Networking is important, and these events strengthened existing relationships a lot. But the travel load may simply have been too high. I now have many leads and collaboration ideas, but there are also opportunities I just can't act on because of schedule limits. It also made me understand why companies grow teams: one person can only execute so much.

For now, I'm still happy as a one-person company and likely will stay that way for the foreseeable future. But if that's the plan, I need to be stricter with travel. I've already made the sad decision not to go to [ICRA 2026](https://ieee-icra.org/), even though it's in Europe... please don't fuel my FOMO :cry:.


## Working at the Game Habitat

Becoming self-employed comes with lots of freedom, but also loneliness. No immediate colleagues to bounce ideas off, no random coffee chats, no spontaneous nerd sessions. That was something I really missed from my Bitcraze and PhD days, so early in my freelance journey I started looking for coworking places. I wanted a developer community around me, but there aren't that many robotics-focused spaces here, and eventually I found the [Game Habitat DevHub](https://devhub.gamehabitat.se/) in Malmö.

Southern Sweden has a strong game-dev ecosystem, with major studios in Malmö such as Massive Entertainment (Assassin's Creed should ring a bell, right?). DevHub is part of [Game Habitat](https://www.gamehabitat.se/) and supports smaller studios and indie developers. As a robotics engineer, I use quite a lot of tooling that originated in game development (especially for simulation), so joining actually made a lot of sense. I started with a flex desk, and once it became clear I needed a full workstation setup, I moved into a shared office with other game developers. One fun side effect is getting pulled into playtests now and then, which is a great break from deep technical work. There's also a small game project on the side now, mostly so I can better understand the hurdles the others face, so maybe that will become a future blog post too.

There are a lot of similarities between robotics and game development, and I really hope to both learn from and contribute to the people around me. The game industry is going through a tough period right now, but one thing I keep seeing at events is that all of the AI/LLM monsters need data, and much of that data can come from simulation. So maybe there's interesting overlap to build on there.


## Great independence comes with great responsibility

So what is next?  

I feel the administrative burden of setting up a company is slowly becoming more manageable now that systems are in place and I trust them more. But managing client projects, content creation, and open-source contributions still needs deliberate balancing.

My plan is to schedule work in clearer sequential blocks across all three areas, so I can focus on one thing at a time. And yes, that means being more conservative with travel too (although I will definitely be at ROSCon 2026 in September, tickets are already booked :wink: ).

Let's see how I am able to manage this enterprise called, myself!
