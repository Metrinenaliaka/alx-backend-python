#!/usr/bin/env python3

"""
unittests for client.py
"""
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from client import GithubOrgClient
from typing import List, Dict, Any
import unittest
from unittest.mock import patch
from parameterized import parameterized_class
from fixtures import org_payload, repos_payload, expected_repos, apache2_repos
from client import GithubOrgClient


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
        """
        Test that GithubOrgClient.org returns the expected result
        """
        mock_get_json.return_value = {"name": org_name}
        client = GithubOrgClient(org_name)
        self.assertEqual(client.org(), {"name": org_name})

    @patch('client.GithubOrgClient.org')
    def test_public_repos_url(self, mock_org: Mock) -> None:
        """
        Test that the result of GithubOrgClient._public_repos_url
        """
        mock_org.return_value = {"repos_url":
                                 "https://api.github.com/orgs/google/repos"}
        client = GithubOrgClient("google")
        expected_url = "https://api.github.com/orgs/google/repos"
        self.assertEqual(client._public_repos_url, expected_url)

    @patch('client.get_json')
    @patch('client.GithubOrgClient._public_repos_url')
    def test_public_repos(self, mock_public_repos_url:
                          Mock, mock_get_json: Mock) -> None:
        """
        Test that GithubOrgClient.public_repos
        returns the expected list of repos
        and that the mocked property and get_json were called once.
        """
        # Define the mocked payload
        mocked_payload = [
            {"name": "repo1", "license": {"key": "MIT"}},
            {"name": "repo2", "license": {"key": "Apache"}},
            {"name": "repo3", "license": {"key": "GPL"}},
        ]

        # Configure the mock objects
        url = "https://api.github.com/orgs/google/repos"
        mock_public_repos_url.return_value = url
        mock_get_json.return_value = mocked_payload

        # Create an instance of GithubOrgClient
        client = GithubOrgClient("google")

        # Call the public_repos method
        repos = client.public_repos(license="MIT")

        # Assert that the returned list of repos is what we expect
        expected_repos = ["repo1"]
        self.assertEqual(repos, expected_repos)

        # Assert that the mocked property and get_json were called once
        mock_public_repos_url.assert_called_once()
        mock_get_json.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected_result):
        """
        Test that GithubOrgClient.has_license returns the expected result
        """
        client = GithubOrgClient("google")
        result = client.has_license(repo, license_key)
        self.assertEqual(result, expected_result)

        @parameterized_class([
            {"org_payload": org_payload,
             "repos_payload": repos_payload,
             "expected_repos": expected_repos,
             "apache2_repos": apache2_repos}
        ])
        class TestIntegrationGithubOrgClient(unittest.TestCase):
            """
            Integration test case for GithubOrgClient
            """
            @classmethod
            def setUpClass(cls):
                """
                Set up the test class
                """
                cls.get_patcher = patch('requests.get')
                cls.mock_get = cls.get_patcher.start()
                cls.mock_get.side_effect = [
                    cls.org_payload,
                    cls.repos_payload,
                    cls.apache2_repos
                ]

            @classmethod
            def tearDownClass(cls):
                """
                Tear down the test class
                """
                cls.get_patcher.stop()

            def test_public_repos(self):
                """
                Test the public_repos method
                """
                client = GithubOrgClient("google")
                repos = client.public_repos()
                self.assertEqual(repos, self.expected_repos)


if __name__ == '__main__':
    unittest.main()
