# Welcome to Instagram Hype Bot! 👾
Here is the repo for a personal project developed in December of 2022!

**Introduction**
	
 Social media platforms are a great tool for today’s era of mass networking and extensive connections. These platforms provide prolific doors of opportunity for those who build a presence on any type of media. Individuals can change the world by gaining support for a cause and creating an action for followers to act upon to advance the cause. As another avenue, users may build their presence for their own fame. In essence, both uses of social media provide massive networking opportunities that enhance the user’s presence in the global sphere. By gaining enough attention on social media, users may gain connections to influential individuals who help users advance in their professional, social, or individual careers. College students of today’s generation are a population who use social media very often. However, busy college students have little time to worry about building and maintaining a substantial presence on social media. Maintaining a presence on social media cannot get in the way of their academic and extracurricular priorities. What could be a solution to managing an active social media platform while also excelling in college?
	
   Creating an Instagram bot best solves this problem. An Instagram bot will be active for students on their account(s). It will find medias for their account to interact with. It will describe each of these media so users have a clear idea of what posts the bot finds for them. An Instagram bot will even like and comment on posts, and follow users based on a chosen hashtag to get media from. This saves a ton of energy and time for students who will instead use these resources to figure out homework problems or finish a report for a major project. 

 
**Inputs and Outputs**

  The Instagram bot program that automates interactions on Instagram will take in the inputs of a username and password. The program will prompt the user to enter their username and password. If nothing is entered, the program will ask the user to enter a username or password. In addition, if the wrong password is entered for an account, the program will tell the user that the wrong password was entered. 
	
  The program provides several sources of output in the form of files. The first output file will display the user credentials that the user inputted. These credentials will be the username and password to the user’s Instagram account. The second output file will display the process of logging in. Once the username and password are imported from the credentials file, the program will tell the user that they are in the process of logging in, then display a message for when they have been successfully logged in. The third output file will display a record of actions that the program has completed for the user. These include the process of logging in, finding posts, and describing the posts. The fourth output file will be an information file of what types of media the bot found for the user based on the hashtag it was using. The fifth output file will provide a record of interactions where the likes, comments, and follows will be displayed. The program will add a comment to every fifth post and tell the user which specific comment was added to the post based on a list of comments. The program will end by thanking the user for their use of the Instagram Hype Bot. 


**User-defined Functions** 

  The first user-defined function asks for the user to enter their username and password. If the user enters nothing for either field, the program will ask them to enter something until the user types in a valid username and/or password. If the account doesn’t exist, the program will complain. If the password doesn’t match up with the account, then the program will say that the wrong password was entered. The user will need to run the program again and enter a valid password so the log in process becomes successful. These user credentials will be stored in a file. 
The second user-defined function will take the contents of the file and use the client.login function from the library instagrapi to log into Instagram. Due to the communication of the functions, the log-in process will take a little while. The completion of this function will be stored in the log file. 
	
 The third user-defined function is the search function. This function peruses the Instagram library for posts that contain the hardcoded hashtag. In this program’s case, the hashtag is “love.” The program will choose five posts for the sake of efficiency in this prototype. These five posts will then be returned to use elsewhere in the program, along with the hashtag.
	
 The fourth user-defined function is the description function. This function will describe each of the collected medias for the user. The first thing that will be described is the media id. Based on this media id, the number of times that the hashtag is found within the caption of that media will be indicated. Next, the media type will be described. The media may either be a photo, a video/IGTV/reel, or an album. The results of this function will be outputted to the MediaDescription.txt file. 
	
 The final user-defined function is the interact function. This function works occasionally due to the nature of the instagrapi library. The error of sending private requests is more likely to be seen. In this function, the program will first write to a file that records each of the actions that this function performs. The function will like each post with the hashtag “love” that is brought in from the search for media function. If the post number has a remainder of five, the creator of this post will be followed, and a comment will be added in the comments section of this post. While these actions are occurring, statements indicating the completion of each action will be written to a file. All print statements will be displayed in the final clean output file called InstaHypeBotLog.txt. 

 
**User Manual**


  To use this program, we will need to have the pip and instagrapi libraries installed. First, install pip onto your device. 
```
python get-pip.py
``` 
  Next, create a virtual environment in visual studio. You may do this by going to the extensions tab and installing the python environment manager
Once you’ve gotten this extension installed, you may go to the tab that pops up called “extensions”. Expand the “venv” section and click the plus button to create a virtual environment for this program. Then press the box with the arrow to open the terminal for this virtual environment. Type in “pip install instagrapi” to add this library to the virtual environment. 
```
pip install instagrapi
```
  Once you’ve completed the initial installation processes, you are ready to start copying code. Create files with the following names found in the box. The code to be put in these files can be found in the files above. Copy the appropriate code into each of these files from the appendix. Then run the main.py function. Here, enter your desired username and password. Then wait as the program processes your credentials, finds posts to interact with, describes these medias and interacts with the chosen media. Once the program finishes, you will see a series of text files. To view the credentials you’ve entered, open credentials.txt. To see all the functions that were completed, open instaBotLog. To view the media descriptions, open MediaDescriptions.txt. 
	
   Run this program to your desired number of iterations. But be careful: Instagram may find out that you’re spamming your bot and thus lock you out of Instagram. Some tweaks you could add to this program are changing the word in the hashtag string. The program will find media with these hashtags accordingly. You can change the number of media that the program collects. Given that the program has no issue in liking, commenting, and following users, you may also change the strings in the comments list. Find the places to do these by referencing the images below. Finally, have fun! 

Appendix
Main Function
"""
===============================================================================

Description
    This program will run all of the functions for the purpose of running an instagram bot.

Get User Credentials
"""
===============================================================================

Description
    This user-defined function will prompt the user to enter a username and 
    password to their instagram account. The program will then store
    the credentials in a file and use these to log the user in. 

Log Into Instagram
"""
===============================================================================

Description
    This function takes user credentials and logs into their instagram account.

Search for Media
"""
===============================================================================

Description
    This function will search through the instagram library of recent posts with the 
    hashtag "love" on the posts. It will return five of these posts in a list called 
    "medias". 

Describe the Media
"""
===============================================================================

Description
    This user-defined function will take all of the media that was collected from
    the searchPosts function and output the media id, the number of occurrences of 
    the hashtag string, and the type of the media. 


Interact with the Media (works occasionally)
"""
===============================================================================

Description
    This function will take the number of posts from the search function and interact 
    with them in a variety of ways involving liking, commenting, and following the 
    instagram account. This function will only work occasionally due to the bugs 
    that occur with the functions in the instagrapi library. 

![3](https://github.com/amirani18/insta_hype_bot/assets/112004077/84767cbc-8e6a-48e2-a81e-618cc1d18cff)

![image](https://github.com/amirani18/insta_hype_bot/assets/112004077/83289c9d-2577-4388-a9c7-acdbd9b92f2e)
