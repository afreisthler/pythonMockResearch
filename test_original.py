__author__ = 'afreisthler'

from unittest import TestCase

from github import GitHub


class TestOriginal(TestCase):
    def setUp(self):
        self.github = GitHub('afreisthler')

    def test_id(self):
        user_id = self.github.get_id()
        self.assertEqual(user_id, 1740138)

    def test_number_public_repos(self):
        number_public_repos = self.github.get_number_public_repos()
        self.assertTrue(number_public_repos >= 4)

    def test_public_repos(self):
        public_repo_uris = self.github.get_public_repo_uris()
        self.assertTrue(len(public_repo_uris) >= 4)

    def test_all_details(self):
        id, number_public_repos, public_repo_uris = self.github.get_all_details()
        self.assertEqual(id, 1740138)
        self.assertTrue(number_public_repos >= 4)
        self.assertTrue(len(public_repo_uris) >= 4)



