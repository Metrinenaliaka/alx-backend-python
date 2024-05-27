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

    if __name__ == '__main__':
        unittest.main()
