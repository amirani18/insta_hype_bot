"""
===============================================================================
ENGR 13000 Fall 2022

Program Description
    This function will search through the instagram library of recent posts with the 
    hashtag "love" on the posts. It will return five of these posts in a list called 
    "medias". 

Assignment Information
    Assignment:     Project 4
    Author:         Areej Mirani, amirani@purdue.edu
    Team ID:        Team Number #22 (e.g. Team 24)

Contributor:    Name, login@purdue [repeat for each]
    My contributor(s) helped me:
    [ ] understand the assignment expectations without
        telling me how they will approach it.
    [ ] understand different ways to think about a solution
        without helping me plan my solution.
    [ ] think through the meaning of a specific error or
        bug present in my code without looking at my code.
    Note that if you helped somebody else with their code, you
    have to list that person as a contributor here as well.
    
ACADEMIC INTEGRITY STATEMENT
I have not used source code obtained from any other unauthorized
source, either modified or unmodified. Neither have I provided
access to my code to another. The project I am submitting
is my own original work.
===============================================================================
"""

def search(client):
    #enter hashtag 
    hashtag = "love"

    #get the list of posts from the public web using functions from the instagrapi library
    medias = client.hashtag_medias_recent(hashtag, 5)

    return hashtag, medias