#!/usr/bin/env python3

"""
unittests for client.py
"""
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from client import GithubOrgClient
from typing import List, Dict, Any


class TestGithubOrgClient(unittest.TestCase):
    """
    Test case with parameterized tests and patch
    """
    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        mock_get_json.return_value = {"name": org_name}
        client = GithubOrgClient(org_name)
        self.assertEqual(client.org(), {"name": org_name})

    @patch('client.GithubOrgClient.org')
    def test_public_repos_url(self, mock_org: Mock) -> None:
        mock_org.return_value = {"repos_url":
                                 "https://api.github.com/orgs/google/repos"}
        client = GithubOrgClient("google")
        expected_url = "https://api.github.com/orgs/google/repos"
        self.assertEqual(client._public_repos_url, expected_url)

    if __name__ == '__main__':
        unittest.main()
