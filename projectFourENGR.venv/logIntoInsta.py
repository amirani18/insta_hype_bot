""" ###
===============================================================================
ENGR 13000 Fall 2022

Program Description
    This function takes user credentials and logs into their instagram account.

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

def logIn():
    #import library
    from instagrapi import Client

    #create client object
    client = Client()

    #open file with user-inputted username/password
    with open("credentials.txt", "r") as credentials:
        #read in username and password from file
        info = credentials.read().strip('\n').splitlines()

        #open actions file for log and view username and password
        actions = open('InstaHypeOutput.txt', 'w')
        actions.write(f"info: {info}")
        username = info[0]
        password = info[1]
        actions.write(f"\nusername is: {username}",)
        actions.write(f"\npassword is: {password}")

        #set up object and login
        actions.write("\nLogging in...")
        ans = client.login(username, password)

        #validation for whether log in process was successful
        if(not ans):
            actions.write("login failed") 
            return 0
        else:
            actions.write("\nLogged in!\n\n")
    
    return client