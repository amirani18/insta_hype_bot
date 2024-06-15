"""
===============================================================================
ENGR 13000 Fall 2022

Program Description
    This function will take the number of posts from the search function and interact 
    with them in a variety of ways involving liking, commenting, and following the 
    instagram account. This function will only work occasionally due to the bugs 
    that occur with the functions in the instagrapi library. 

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

def interactions(client, hashtag, medias):
    #import library
    import random

    #open file to record interactions
    with open ("instaHypeBotLog.txt", "w") as log:

        #welcome user
        log.write("Welcome to your interactions hub! This is where you may see a record for all the \ninteractions we have completed with the collection of Instagram media!\n")
        log.write("******************************************************************************************************************\n\n")


        #initialize loop for series of interactions with the posts
        for i, media in enumerate(medias):
        
            #like posts
            client.media_like(media.id)
            log.write(f"Liked post number {i+1} of hashtag {hashtag}\n")

            #every fifth post, follow and comment on the post
            if i % 5 == 0:
                #follow the user of the post
                client.user_follow(media.user.pk)
                log.write(f"\n\nFollowed user {media.user.username}")

                #comment on the post
                client.media_comment(media.id, "DM @areej.mirare")

                #initialize comments
                comments = ["DM @areej.mirare", "You're awesome", "Reach out the global for more outreach!"]
                comment = random.choice(comments)
                log.write(f"\nCommented {comment} under post number {i+1}\n\n")