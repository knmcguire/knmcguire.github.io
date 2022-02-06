---
layout: post
title: "Starting with my own website on Github Pages"
categories: webdev 
---

  <script data-goatcounter="https://knmcguire.goatcounter.com/count"
  async src="//gc.zgo.at/count.js"></script>

Hi all!

This is my very first post on my very own website! 
Currently there are so many profile pages now on so many social media or professional network websites (linkedin, researchgate, google scholar et cetera) that I felt the need to have a more central place to store all of my professional and personal projects, which I did as you can see!. 

This post describes some important elements that I encountered when starting up development of this website, so hopefully it will also help out others as well.

# Wordpress or Github pages?
I have worked with [wordpress](https://wordpress.com/) before and remembered it be quite an easy to get started with. You just select a existing theme with layout & everything, write your posts select your pages and everything everything is nicely included. However, many times the plugins in the posts if you wanted to show a video or not. Also I would like to have some more control on the layout in the future.

 A tip of a friend [Roland from Pinch of Intelligence](https://www.pinchofintelligence.com/)  convinced me to try out [github pages](https://pages.github.com/). What it does, is generating a static website based on [Jekyll](https://jekyllrb.com/) with markdown files on a Github repository. I kind of like the idea of the full source of the website being available and markdown files I prefer over dealing with the editor on wordpress, eventhoug perhaps the setting up might take a bit longer initially. [This blogpost from Logit](https://www.logitblog.com/moved-away-from-wordpress-to-github-pages/) also explains more about the benefits of Github pages over Wordpress if you are interested.

Long story short, now the source of this website can be found in [my website's repository](https://github.com/knmcguire/knmcguire.github.io), of which anything in the /docs folder is deployed to the eventual website :)

# Hosting locally with Docker

Of-course I would like to try out anything that I write or in terms on layout, and not only when I've pushed my changes to github pages (and all the changes are online for the world to see). I would need to find a way to be able to display the website locally on my own machine. Luckily github pages already provided [instructions to do this](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/testing-your-github-pages-site-locally-with-jekyll), I was a bit against the notion of having to install the whole shabang of Ruby on both the Linux and Windows side of my computer (actually jekyll advises to use the [WSL subsystem ](https://jekyllrb.com/docs/installation/windows/)) instead... 

I decided to go and search if there was any container solution that I can use. With some googling I've found several posts  of people (like this one from [Craig Hunter](https://craighuther.com/2019/05/23/self-hosting-jekyll-with-docker-compose/)), who managed to use a jekyll container with docker to build the website locally. So I did the same and made a [docker-compose.yml](https://github.com/knmcguire/knmcguire.github.io/blob/0be085b8df83c544fa18d5ba44a957ac766c73b5/docs/docker-compose.yml) file with the following content:
```
version: '2.2'

services:
  jekyll:
    image: jekyll/jekyll:latest
    command: jekyll serve --watch --force_polling --verbose
    ports:
      - 4000:4000
    volumes:
      - .:/srv/jekyll
```

Then in a terminal, I will type `docker compose up` in the same directory as the documents sources and then I would be able to reach the website on a browser on Windows with *http://localhost:4000/* and in Linux with *http://0.0.0.0:4000*. The docker container can be stopped easily with `ctrl-c`.



# Layout

Technically you should be able to do (almost) what ever you want with the layout on github pages. For now I just the [jekyll theme minima](https://github.com/jekyll/minima) and, if I wanted, I could clone the minima theme repo into my website repository and change the .CSS files and html files to my liking. It is nice to know that I will have that freedom in the future.

What I've done for now, is that I made some adjustments *on top of the existing theme*. I wanted to make a [special layout html](https://github.com/knmcguire/knmcguire.github.io/blob/main/docs/_layouts/linktree.html) that included a nicely styled referral button (which Minima doesn't have). I copied the [default.html from Jekyll's minima theme](https://github.com/jekyll/minima/blob/master/_layouts/default.html), copied it in a _layout folder in /docs/ and added the following just before  `<body> `:
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

Then I could change the Jekyll header in the markdown file, in the cause your layout is called *my_special_layout.html:
```
---
layout: my_special_layout
title: "My awesome title"
---
```

and now the special button can be added as:
```
<a href="https://knmcguire.github.io/"><button class= "button">My Website</button></a>
```
which looks like this:
<a href="https://knmcguire.github.io/"><button style="background-color: #555555;
        border: none;
        color: white;
        padding: 15px 32px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        width: 100%; 
        cursor: pointer">My Website</button></a>

By the way, While googling on how to make nicely styled buttons, I found that I often came back to [W3 schools' website](https://www.w3schools.com/), which includes many examples of all kinds of HTML and CSS styles for websites. So I'm definitely saving it for future references. 

Anyway, With those buttons I was able to create the buttons on [my link referral page](https://knmcguire.github.io/ln/). This was inspired by [linkt.ee](https://linktr.ee/) structure, except for I felt that that was more for influencers and paid services. I also have wanted to have my own website to display my own projects, next to this link tree, so I decided recreate this for my own. 

<img src="/images/screenshot_linktree.png" height="300"  /> 

# Counting views with Goatcounter

Last but not least, it would be nice to have some kind of measure of how many people are visiting my website and even reading it at all! It does not have to be very detailed, as I would be happy to have some kind of page view count or something similar. 

Jekyll's minima theme also makes it easy to include a Google Analytics tag, which I tested out of-course for a little bit. Currently the version 4 of GA seem to promise no cookie based tracking, however that still seems to be difficult to completely to turn off according to [this article by Kanban maker](https://kambanthemaker.com/using-google-analytics-without-that-annoying-consent-popup-ckdjrnhl10230z2s10qkkavxa). Also the fact that you get a lot of analytics tools 'for free' from GA, is a bit bothersome as well and there must be a catch to it... 

So I decided against using GA and wanted to go for [privacy friendly and open-source tracking alternatives](https://github.com/spekulatius/awesome-privacy-friendly-web-analytics). Since I don't own a server, I decided to go for [Goatcounter](https://www.goatcounter.com/), since they offer free hosting for a non-commercial website. The display of the views are simple but it is more than I need. 

Currently I only have Goattracker on my link referral website and this blogpost, but I will probably extend it to other once I've been able to check out the code a little bit more. But I do like the way the developer [arguments about why he made Goatcounter](https://www.goatcounter.com/why) in the first place. And ofcourse the fact that it's opensource :).

# To Conclude

It is pretty satisfying to work on a website to be honest! And I think it will perhaps also give me the drive to write things down and to document past, present and personal projects. Also, it contains many new elements like working with the jekyll container, building layout in HTML and learn about why we always have to give our consent on all of those websites... Anyway, I hope these tips will be also handy for anybody else starting with their own website with Github Pages!

