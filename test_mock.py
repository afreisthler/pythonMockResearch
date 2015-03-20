__author__ = 'afreisthler'

from unittest import TestCase

import mock

from github import GitHub


def urlopen_side_effect(*args, **kwargs):
    if len(args) > 0:
        if args[0] == 'https://api.github.com/users/afreisthler':
            return file('./mock_data/urlopen1')
        elif args[0] == 'https://api.github.com/users/afreisthler/repos':
            return file('./mock_data/urlopen2')
    raise Exception('Unexpected call to urlopen by mock object')


@mock.patch('urllib2.urlopen')
class TestMock(TestCase):
    def setUp(self):
        self.github = GitHub('afreisthler')

    def test_id(self, mock_urlopen):
        mock_urlopen.side_effect = urlopen_side_effect
        user_id = self.github.get_id()
        self.assertEqual(user_id, 1740138)
        self.assertEqual(mock_urlopen.call_count, 1)

    def test_number_public_repos(self, mock_urlopen):
        mock_urlopen.side_effect = urlopen_side_effect
        number_public_repos = self.github.get_number_public_repos()
        self.assertEqual(number_public_repos, 4)
        self.assertEqual(mock_urlopen.call_count, 1)

    def test_public_repos(self, mock_urlopen):
        mock_urlopen.side_effect = urlopen_side_effect
        public_repo_uris = self.github.get_public_repo_uris()
        self.assertTrue(len(public_repo_uris) >= 4)
        self.assertEqual(mock_urlopen.call_count, 1)

    def test_all_details(self, mock_urlopen):
        mock_urlopen.side_effect = urlopen_side_effect
        id, number_public_repos, public_repo_uris = self.github.get_all_details()
        self.assertEqual(id, 1740138)
        self.assertEqual(number_public_repos, 4)
        self.assertTrue(len(public_repo_uris) >= 4)
        self.assertEqual(mock_urlopen.call_count, 3)



