import requests

class MyGithubMessenger(object):
    def __init__(self, user_name):
        self.user_name = user_name
        self.url_ = 'https://raw.githubusercontent.com/{}/'.format(self.user_name)
        
    def pull_github_file(self, file_location, file_name):
        resp = requests.get(self.url_ +  str(file_location) + "/" + "master" + '/' + str(file_name))
        
        if resp.status_code != 200:
            return "Unable to connect to your github...try again"
        my_file = resp.text
        if resp.text == 400:
            return "Invalid file location or file name...try again"
        return my_file
