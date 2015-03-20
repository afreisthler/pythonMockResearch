__author__ = 'afreisthler'

from unittest import TestCase
import urllib2

import mox

from github import GitHub


class TestMox(TestCase):
    def setUp(self):
        self.github = GitHub('afreisthler')
        self.urllib_mocker = mox.Mox()

    def test_id(self):
        self.urllib_mocker.StubOutWithMock(urllib2, 'urlopen')
        urllib2.urlopen("https://api.github.com/users/afreisthler").AndReturn(file('./mock_data/urlopen1'))
        self.urllib_mocker.ReplayAll()

        user_id = self.github.get_id()
        self.assertEqual(user_id, 1740138)

        self.urllib_mocker.UnsetStubs()
        self.urllib_mocker.VerifyAll()

    def test_number_public_repos(self):
        self.urllib_mocker.StubOutWithMock(urllib2, 'urlopen')
        urllib2.urlopen("https://api.github.com/users/afreisthler").AndReturn(file('./mock_data/urlopen1'))
        self.urllib_mocker.ReplayAll()

        number_public_repos = self.github.get_number_public_repos()
        self.assertEqual(number_public_repos, 4)

        self.urllib_mocker.UnsetStubs()
        self.urllib_mocker.VerifyAll()

    def test_public_repos(self):
        self.urllib_mocker.StubOutWithMock(urllib2, 'urlopen')
        urllib2.urlopen("https://api.github.com/users/afreisthler/repos").AndReturn(file('./mock_data/urlopen2'))
        self.urllib_mocker.ReplayAll()

        public_repo_uris = self.github.get_public_repo_uris()
        self.assertTrue(len(public_repo_uris) >= 4)

        self.urllib_mocker.UnsetStubs()
        self.urllib_mocker.VerifyAll()

    def test_all_details(self):
        self.urllib_mocker.StubOutWithMock(urllib2, 'urlopen')
        urllib2.urlopen("https://api.github.com/users/afreisthler").AndReturn(file('./mock_data/urlopen1'))
        urllib2.urlopen("https://api.github.com/users/afreisthler").AndReturn(file('./mock_data/urlopen1'))
        urllib2.urlopen("https://api.github.com/users/afreisthler/repos").AndReturn(file('./mock_data/urlopen2'))
        self.urllib_mocker.ReplayAll()

        id, number_public_repos, public_repo_uris = self.github.get_all_details()
        self.assertEqual(id, 1740138)
        self.assertEqual(number_public_repos, 4)
        self.assertTrue(len(public_repo_uris) >= 4)

        self.urllib_mocker.UnsetStubs()
        self.urllib_mocker.VerifyAll()
