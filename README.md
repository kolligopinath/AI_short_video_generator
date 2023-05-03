# AI_short_video_generator
Automated short video generated using Artificial intelligence tools.

This can be used to Generate instagram reels, Tiktok videos, Youtube shorts in wide range of topics like Travel, lifestyle, fashion, Short stories for kids, etc,.

This can generate lengthy videos as well in those areas.

How it has been built?

    Topic selection: This project asks chatGPT to create a topic based on users input
    
    Content /Script Generation: Based on the topic, chatGPT generates a video script, title, and description for the video.
    
    Voiceover Generation: It uses Eleven Labs API to generate voiceovers for each line of text.
    
    Image Generation: It generates relevant images for each line of the script, based on the topic using DALLE.
    
    Video generation: Now the Voice over audio & images are pieced together to generate video.


## A sample output file is attached - Mother and Childs Colorful Tale.mp4

# Steps to be followed for using this project:

You need two account to make use of this project.

    1. ChatGPT 4
    
    2. Eleven labs
    
In the file AI_short_video_generator/AI_short_video_generator.py Give your API keys for openai & elevenlabs

You need a Python instance insalled on your system with the following packages

    openai, requests, nltk, urllib.request, datetime, moviepy, flask, re(pip install these packages)
    
Now run the app.py file from your teminal, this will generate a link with local server to launch the application. Launch the application using that link.

http://127.0.0.1:5000

Now you can see the UI as below screenshot.

![image](https://user-images.githubusercontent.com/21278131/235863659-b171323d-ae18-4455-a528-7deeed78b595.png)

Type in the topic in detail on which you want to generate your video and then click on Generate.

It will take its time to do the magic and once the process is complete, it will automatcally opens a popup to download that video.

   ## That's it!!!
