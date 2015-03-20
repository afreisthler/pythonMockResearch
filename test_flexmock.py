__author__ = 'afreisthler'

from unittest import TestCase
import urllib2

from flexmock import flexmock

from github import GitHub


def urlopen_side_effect(*args, **kwargs):
    if len(args) > 0:
        if args[0] == 'https://api.github.com/users/afreisthler':
            return file('./mock_data/urlopen1')
        elif args[0] == 'https://api.github.com/users/afreisthler/repos':
            return file('./mock_data/urlopen2')
    raise Exception('Unexpected call to urlopen by mock object')


class TestFlexmock(TestCase):
    def setUp(self):
        self.github = GitHub('afreisthler')

    def test_id(self):
        flexmock(urllib2).should_receive("urlopen").times(1).with_args(
            "https://api.github.com/users/afreisthler").and_return(file('./mock_data/urlopen1'))
        user_id = self.github.get_id()
        self.assertEqual(user_id, 1740138)

    def test_number_public_repos(self):
        flexmock(urllib2).should_receive("urlopen").times(1).with_args(
            "https://api.github.com/users/afreisthler").and_return(file('./mock_data/urlopen1'))
        number_public_repos = self.github.get_number_public_repos()
        self.assertEqual(number_public_repos, 4)

    def test_public_repos(self):
        flexmock(urllib2).should_receive("urlopen").times(1).with_args(
            "https://api.github.com/users/afreisthler/repos").and_return(file('./mock_data/urlopen2'))
        public_repo_uris = self.github.get_public_repo_uris()
        self.assertTrue(len(public_repo_uris) >= 4)

    def test_all_details(self):
        flexmock(urllib2)
        urllib2.should_receive("urlopen").times(3).replace_with(urlopen_side_effect)
        id, number_public_repos, public_repo_uris = self.github.get_all_details()
        self.assertEqual(id, 1740138)
        self.assertEqual(number_public_repos, 4)
        self.assertTrue(len(public_repo_uris) >= 4)



