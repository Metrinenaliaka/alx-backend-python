#!/usr/bin/env python3
"""
Unittests for utils.py
"""

import unittest
import utils
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import get_json, memoize
from typing import Mapping, Sequence, Dict, Any


class TestAccessNestedMap(unittest.TestCase):
    """
    Test case with parameterized tests
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map: Mapping, path:
                               Sequence, expected: Any) -> None:
        from utils import access_nested_map
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map: Mapping, path:
                                         Sequence) -> None:
        from utils import access_nested_map
        with self.assertRaises(KeyError) as cm:
            access_nested_map(nested_map, path)
        self.assertEqual(cm.exception.args[0], path[-1])

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('utils.requests.get')
    def test_get_json(self, url: str, expected:
                      Dict[str, Any], mock_get: Mock) -> None:
        """
        Test that utils.get_json returns the expected result
        using mock
        """
        mock_response = Mock()
        mock_response.json.return_value = expected

        mock_get.return_value = mock_response

        result = utils.get_json(url)

        # Assert the function returned the expected result
        self.assertEqual(result, expected)

        # Ensure that a GET request was made to the correct URL
        mock_get.assert_called_once_with(url)


if __name__ == "__main__":
    unittest.main()
