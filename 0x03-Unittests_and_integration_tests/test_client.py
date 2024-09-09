#!/usr/bin/env python3
"""Unit and integration tests for client module."""

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import org_payload, repos_payload, expected_repos, apache2_repos


class TestGithubOrgClient(unittest.TestCase):
    """Unit tests for GithubOrgClient class."""

    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch('client.get_json')
    def test_org(self, org_name: str, mock_get_json: Mock) -> None:
        """
        Test GithubOrgClient.org method with mocked get_json.
        """
        client = GithubOrgClient(org_name)
        client.org()
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
        )

    @patch('client.GithubOrgClient.org', new_callable=Mock)
    def test_public_repos_url(self, mock_org: Mock) -> None:
        """
        Test GithubOrgClient._public_repos_url method with mocked org.
        """
        mock_org.return_value = {"repos_url": "http://example.com/repos"}
        client = GithubOrgClient("google")
        self.assertEqual(client._public_repos_url, "http://example.com/repos")

    @patch('client.get_json')
    @patch('client.GithubOrgClient._public_repos_url', new_callable=Mock)
    def test_public_repos(self, mock_url: Mock, mock_get_json: Mock) -> None:
        """
        Test GithubOrgClient.public_repos method with mocked data.
        """
        mock_url.return_value = "http://example.com/repos"
        mock_get_json.return_value = [{"name": "repo1"}, {"name": "repo2"}]

        client = GithubOrgClient("google")
        repos = client.public_repos()

        self.assertEqual(repos, ["repo1", "repo2"])
        mock_url.assert_called_once()
        mock_get_json.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(
        self, repo: dict, license_key: str, expected: bool
    ) -> None:
        """Test GithubOrgClient.has_license method for various licenses."""
        client = GithubOrgClient("google")
        self.assertEqual(client.has_license(repo, license_key), expected)


@parameterized_class(('org_payload', 'repos_payload', 'expected_repos', 'apache2_repos'), [
    (org_payload, repos_payload, expected_repos, apache2_repos),
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration tests for GithubOrgClient class."""

    @classmethod
    def setUpClass(cls) -> None:
        """Set up class-wide mock for requests.get."""
        cls.get_patcher = patch('client.requests.get')
        cls.mock_get = cls.get_patcher.start()

        cls.mock_get.side_effect = [
            Mock(json=lambda: cls.org_payload),
            Mock(json=lambda: cls.repos_payload)
        ]

    @classmethod
    def tearDownClass(cls) -> None:
        """Stop the patcher for requests.get."""
        cls.get_patcher.stop()

    def test_public_repos(self) -> None:
        """Test that public_repos returns the expected repos."""
        client = GithubOrgClient("google")
        self.assertEqual(client.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self) -> None:
        """
        Test that public_repos with license='apache-2.0'
        returns expected repos.
        """
        client = GithubOrgClient("google")
        self.assertEqual(
            client.public_repos(license="apache-2.0"), self.apache2_repos
        )
