---
layout: post
title: "Starting with Github Pages"
categories: webdev 
---

Hi all!

This is my very first post on my very own website! Currently there are so many profile pages now on so many social media or proffessional network websites (linkedin, researchgate, google scholar etc etc) that I felt the need to have a more central place to store all of my professional and personal projects. 

# Choosing the host
I have worked with [wordpress](https://wordpress.com/) before and it is quite easy to get started. You just select a existing theme with layout & everything, write your posts select your pages and everything everything is nicely included. However, many times the plugins in the posts if you wanted to show a video or not. Moreover I kind of like the idea of the full source of the website being available on a github repository. Which is kind of the idea of [github pages](https://pages.github.com/) does, as it is generating a static website based on the [Jekyll generator](https://jekyllrb.com/).  [This blogpost from Logit](https://www.logitblog.com/moved-away-from-wordpress-to-github-pages/) and a tip of my friend [Roland from Pinch of Intelligence](https://www.pinchofintelligence.com/) also convinced me to try out github pages. Eventhough there more websites hosting services out there, I thought to start out with this first.

# Layout

Technically you should be able to do (almost) what ever you want with the layout on github pages. For now I just the [jekyll theme minima](https://github.com/jekyll/minima), if I wanted I could clone the minima theme repo into my website repository and change the .CSS files and html files to my liking. It is nice to know that I will have that freedom in the future.

What I've done for now, is that I made some adjustments. I wanted to make a [special layout html](https://github.com/knmcguire/knmcguire.github.io/blob/main/docs/_layouts/linktree.html) that included a nicely styled referral button. I copied the [default.html from Jekyll's minima theme](https://github.com/jekyll/minima/blob/master/_layouts/default.html) and added the following before  `<body> `:
```
    <head>
        <style>
            .button {
            background-color: #555555;
            border: none;
            color: white;
            padding: 15px 32px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            width: 100%; 
            cursor: pointer
            }
        </style>  
    </head>
```

How to make nicely styled buttons, I obviously googled how to do this, but I found that I often came to [W3 schools' website](https://www.w3schools.com/), which is a really nice referral if you want to add anything special to your website. I'm definietly saving it for future references. 

With those buttons I was able to create the buttons on [my link referral page](https://knmcguire.github.io/ln/). This was slightly expired by [linkt.ee](https://linktr.ee/) structure, except for I felt that that was more for influencers and paid services. I also have wanted to have my own website to display my own projects, next to this link tree, so I decided to kind of make my own link referal pages. 

![link referral](/images/screenshot_linktree.png)

# Analytics

Second of all, I would like to have some kind of measure of how many people are visiting my website. It does not have to be very detailed, as I would be happy to have some kind of page view count and unique users. Jekyll's minima theme also enables to include a Google Analytics tag, which I tested out of-course for a little bit. Currently the version 4 of GA seem to promise no cookie based tracking, however that still seems to be difficult to completely to turn off according to [this article by Kanban maker](https://kambanthemaker.com/using-google-analytics-without-that-annoying-consent-popup-ckdjrnhl10230z2s10qkkavxa). Also the fact that you get a lot of analytics tools 'for free' from GA, is a bit bothersome as well and there must be a catch to it...

This is only a personal website so I think in general it wouldn't really bother anyone if I used GA or not, but I decided against using GA and wanted to go for [privacy friendly and open-source tracking alternatives](https://github.com/spekulatius/awesome-privacy-friendly-web-analytics). Since I don't own a server, I decided to go for [Goatcounter](https://www.goatcounter.com/), since they offer free hosting for a non-commercial website. The display of the views are simple but it is more than I need. 

