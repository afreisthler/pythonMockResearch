__author__ = 'afreisth'

import urllib2
import json

# Class using github api put together as an example for mock library evaluation
class GitHub(object):
    def __init__(self, username):
        self.username = username

    def get_id(self):
        result = urllib2.urlopen('https://api.github.com/users/{0}'.format(self.username))
        return json.load(result).get('id', None)

    def get_number_public_repos(self):
        result = urllib2.urlopen('https://api.github.com/users/{0}'.format(self.username))
        return json.load(result).get('public_repos', None)

    def get_public_repo_uris(self):
        result = urllib2.urlopen('https://api.github.com/users/{0}/repos'.format(self.username))
        repos = json.load(result)
        return [repo['html_url'] for repo in repos if not repo['private']]

    def get_all_details(self):
        id = self.get_id()
        number_public_repos = self.get_number_public_repos()
        public_repo_uris = self.get_public_repo_uris()
        return id, number_public_repos, public_repo_uris

