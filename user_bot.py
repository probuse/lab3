from talk_to_git import MyGithubMessenger

print "\
Talk to your github app.\
To continue please input your github user name\
"
user_name = raw_input("Your github user name: \n> ")

my_bot = MyGithubMessenger(user_name)

print "\
the application can help you get a file from your github repository\
Provide the name of your repository and the file name to get the file\
"
user_feedback = raw_input("Do you want to get a file from your github?  \nAnswer yes or no\n >")

if user_feedback == 'yes':
    repo_name = raw_input("PLease input your repository name: \n> ")
    file_name = raw_input("PLease input your file name with its extension: \n> ")
    print my_bot.pull_github_file(repo_name, file_name)    
else:
    print 'Our bot does not know how to do that yet.'

