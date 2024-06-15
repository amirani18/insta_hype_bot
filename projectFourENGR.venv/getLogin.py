"""
===============================================================================
ENGR 13000 Fall 2022

Program Description
    This user-defined function will prompt the user to enter a username and 
    password to their instagram account. The program will then store
    the credentials in a file and use these to log the user in. 

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

def credentials(): 
    #open file to record credentials
    with open("credentials.txt", "w") as info:

        #prompt user for username
        username = info.write(input('Enter your username: '))

        #ensure a username is entered
        while username < 1:
            print("Please enter your username: ")
            username = info.write(input('Enter your username: '))
            if username >= 1:
                continue
        info.write('\n')

        #prompt user for password
        password = info.write(input('Enter your password: '))

        #ensure a username is entered
        while password < 1:
            print("Please enter your password.")
            password = info.write(input('Enter your password: '))
            if password >= 1:
                continue