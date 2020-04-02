# Good-Minecraft-Seed-Generator
A program to create good Minecraft seeds.

___

## Update #1 (Taken From My Reddit Post)


### Intro
Hey everyone and welcome to my first update post for my "good-seed-generator".  In this update, I created a super simple program that generates a list of 100 seeds. 


### Research
The research for this project includes:
* A review for writing to files from Corey Schafer:  [https://www.youtube.com/watch?v=Uh2ebFW8OYM](https://www.youtube.com/watch?v=Uh2ebFW8OYM) 
* A post I made on the range of numbers for Minecraft seeds:  [https://www.reddit.com/r/Minecraft/comments/fn1xob/what\_is\_the\_range\_for\_minecraft\_seeds/](https://www.reddit.com/r/Minecraft/comments/fn1xob/what_is_the_range_for_minecraft_seeds/) 
* And, although I already had an environment that I liked, I decided to switch to Sublime for this project and used this video from Corey Schafer to set it up:  [https://www.youtube.com/watch?v=xFciV6Ew5r4](https://www.youtube.com/watch?v=xFciV6Ew5r4) 


### Code
All of the code for this project can be found on this Github Page:  [https://github.com/CodeForeverAndEver/Good-Minecraft-Seed-Generator](https://github.com/CodeForeverAndEver/Good-Minecraft-Seed-Generator)  


### Coming Up Next
The next thing I am going to work on is (all automatically) putting the seeds into [Chunkbase Biome Finder](https://www.chunkbase.com/apps/biome-finder) with Selenium, zooming out all the way to make sure the entire generated map is viewable, and then taking a screenshot with Selenium, and then cropping the image to just the map with Pillow. After that, I am going to work on creating an algorithm to check if the seed has all of the attributes that would define it as "good".


### Release Date Prediction
Currently, I think that the full thing will be released two weeks from now!


### Stay Up To Date
To stay up to date, keep checking the [original post](https://www.reddit.com/r/Minecraft/comments/fmjh19/thinking_about_making_a_goodseedgenerator/) where I will keep posting the links to each update!

___
## Update #2 (Taken From My Reddit Post)


# Intro
Hey everyone and welcome back to another devlog update post for my "good-seed-generator". In this update, I built off of the last thing I built: a list-of-seeds generator. 


# Research
The research for this update includes:
* A video on threading from Corey Schafer: https://youtu.be/IEEhzQoKtQU  This video helped because it showed me that I needed multiprocessing **not** threading
* A video on multiprocessing from Corey Schafer: https://youtu.be/fKl2JW_qrso This video helped me to run multiple automated browsers at once
* This question from StackOverflow which helped me to get the image of the seed (I used the second answer): https://stackoverflow.com/questions/15018372/how-to-take-partial-screenshot-with-selenium-webdriver-in-python
* This StackOverflow question which helped lead me in the right direction for changing the zoom slider on the [ChunkBase Biome-Finder](https://www.chunkbase.com/apps/biome-finder): (https://stackoverflow.com/questions/17911980/selenium-with-python-how-to-modify-an-element-css-style/17912095 
* This post from Karlo Abapo which helped me to update the slider after I had moved it to the left (I could move the square on the slider but the image wouldn't zoom out, by moving the slider a little to the left even if it couldn't go anymore in that direction it updated the zoom): https://karloabapo.wordpress.com/2018/03/18/how-to-move-a-slider-element-with-selenium-python/
* This StackOverflow post which helped teach me how to scroll to an element on a webpage so that it was in view, I needed this because the zoom wouldn't update unless I had the slider always in view. I also used it to get the seed back in view: https://stackoverflow.com/questions/3401343/scroll-element-into-view-with-selenium
* This video about the Pillow library from Corey Schafer: https://www.youtube.com/watch?v=6Qs3wObeWwc
* I also used the knowledge I had from the Corey Schafer video I posted in the last update about file manipulation


# Code + Stopping Progress Updates on GitHub
All of the code for this project can be found on my Github Page for it: https://github.com/CodeForeverAndEver/Good-Minecraft-Seed-Generator. In the last update, I also mentioned that I would be giving more frequent mini-updates on the Github page but have decided otherwise as it only slows my progress down.


# Coming Up Next
The next thing I am going to work on is creating an algorithm to check if the seed is "good". In this development process, I am only going to classify something as good if it has certain biomes near spawn. For example, I want to start by checking if it has a Mooshroom Biome, Mesa Biome, and Jungle Biome by spawn. If you want to influence this development process leave what you think is a good seed in the comments of [this post](https://www.reddit.com/r/Minecraft/comments/fmjh19/thinking_about_making_a_goodseedgenerator/). After that, I am going to take a while and learn PyQT and make a GUI to interface with the project. I also want to include different options for what you want in the seed. For example, if you want a jungle biome and mooshroom biome, there should be checkboxes in the program for whether you want them or not. But that is a much later update.


# Release Date Prediction
I think that the very first version of this should be out 1-2 weeks from now. However, this will most likely be an exe file that just looks for mooshroom, mesa, and jungle seeds with you choosing any options. The first version with a GUI I expect will take much longer and I may decide to do mini-updates for that instead of these large ones,


# Stay Up To Date
To stay up to date, keep checking the [original post](https://www.reddit.com/r/Minecraft/comments/fmjh19/thinking_about_making_a_goodseedgenerator/) where I will keep posting the links to each update! Note: This is also the same link where I am asking for what you consider to be a good seed.


# Leave Any Thoughts In The Comments
If you have any suggestions or want to show some encouragement, anything, just leave them in the comments. :D

- Beast
