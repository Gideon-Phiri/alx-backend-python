#!/usr/bin/env python3
"""Unit tests for utils module."""


import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """Test case for access_nested_map function."""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(
        self, nested_map: dict, path: tuple, expected: any
    ) -> None:
        """Test access_nested_map returns expected output for valid inputs."""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(
        self, nested_map: dict, path: tuple
    ) -> None:
        """Test access_nested_map raises KeyError for invalid inputs."""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Test case for get_json function."""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('utils.requests.get')
    def test_get_json(
        self, test_url: str, test_payload: dict, mock_get: Mock
    ) -> None:
        """Test get_json function with mocked requests.get."""
        mock_get.return_value = Mock(json=lambda: test_payload)
        response = get_json(test_url)
        self.assertEqual(response, test_payload)
        mock_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """Test case for memoize decorator."""

    class TestClass:
        """Test class to test memoize functionality."""

        def a_method(self) -> int:
            """Simple method to be memoized."""
            return 42

        @memoize
        def a_property(self) -> int:
            """Property method to return memoized result."""
            return self.a_method()

    @patch.object(TestClass, 'a_method')
    def test_memoize(self, mock_method: Mock) -> None:
        """
        Test that a_method is only called once when memoized.
        """
        mock_method.return_value = 42
        test_obj = self.TestClass()

        result1 = test_obj.a_property
        result2 = test_obj.a_property

        self.assertEqual(result1, 42)
        self.assertEqual(result2, 42)
        mock_method.assert_called_once()
