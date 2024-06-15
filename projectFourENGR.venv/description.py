"""
===============================================================================
ENGR 13000 Fall 2022

Program Description
    This user-defined function will take all of the media that was collected from
    the searchPosts function and output the media id, the number of occurrences of 
    the hashtag string, and the type of the media. 

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

def describePosts(medias, hashtag):
    #import library
    import random

    #open file to record interactions
    with open ("MediaDescriptions.txt", "w") as describe:
        #welcome user
        describe.write("Welcome to your media hub! This is where you may see information about the posts we've got for you from Instagram!\n")
        describe.write("******************************************************************************************************************\n\n")

        #initialize loop for series of interactions with the posts
        for i, media in enumerate(medias):

            #write the media identification numbers to the file
            describe.write(f"Post number {i+1} has the id of {media.id}\n\n")

            #count the number of occurrences of the hashtag in the post
            counter = media.caption_text.count(hashtag)
            describe.write(f"\t\tThis post contains the hashtag {hashtag} that is written in the caption {counter} times.\n")

            #return the type of media of the post
            if media.media_type == 1:
                describe.write(f"\t\tThis post has a media type number of {media.media_type}, indicating it is a photo.\n\n")
            elif media.media_type == 2:
                describe.write(f"\t\tThis post has a media type number of {media.media_type}, indicating it is a video, reel, or IGTV.\n\n")
            elif media.media_type == 8:
                describe.write(f"\t\tThis post has a media type number of {media.media_type}, indicating it is an album.\n\n")

        describe.write(f"\nWe've described the media we've collected on the posts with the hashtag {hashtag} for you!! \n\nThank you for using Instagram bot :)")
