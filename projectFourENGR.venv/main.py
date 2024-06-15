""" ###
===============================================================================
ENGR 13000 Fall 2022

Program Description
    This program will run all of the functions for the purpose of running an instagram bot.

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
### """

#import functions from different files
from getLogin import credentials
from logIntoInsta import logIn
from searchPosts import search
from description import describePosts
from interact import interactions

#open text file for recording interactions
with open ("instaBotLog", "w") as log:
    #welcome user
    log.write("Welcome to Instagram Hype Bot! Enter your username and password to get started...\n")

    #get user credentials (username and password)
    credentials()

    #log into instagram using credentials
    client = logIn()
    log.write("\n\nSuccessfully logged in!")

    #search for public posts in the instagram library
    hashtag, medias = search(client)
    log.write("\nWe found some posts for you to interact with!")

    #get information about chosen posts
    describePosts(medias, hashtag)
    log.write("\nWe've described the chosen media for you! \n\nThank you for using Instagram Hype Bot :)")

    #interact with the chosen posts
    interactions(client, hashtag, medias)
    log.write(f"\nWe've interacted on the posts with the hashtag {hashtag} for you!! \n\nThank you for using your very own Instagram bot :)")

