# Lab 3
    These are tasks for the day 3 of the boot camp

    
## This repository contains the following files
### min_max.py
    This file contains a function that takes in a list.
    The function return a list with that contains the minimum and the
    largest of the elements in a list.
    ie if a the input is l = [1, 2, 3, 4, 55]
    The output is [1, 55] 
        
### talk_to_git.py
    This file uses the GitHub API to return a file from Github
    This is a file has a class MyGithubMessenger that takes in a user
    name.
    The user name has to be a user name for a GitHub account.
    This class also has a method pull_github_file that takes in a
    repository and the file that you want to get with its extension
    The pull_github_file returns the contents of the file at the
    specified repository
    
### user_bot.py
    This file imports the talk_to_git.py module.
    It makes use of the pull_github_file method from the
    MyGithubMessenger to print the file specified by the user.
    
### words.py
    This script has a words function that takes in a string and returns
    how many times a word appears in a string.
