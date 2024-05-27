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


class TestGetJson(unittest.TestCase):
    """
    Test case with parameterized tests and patch
    """

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


class TestMemoize(unittest.TestCase):
    """
    Test case for memoize using  Parameterize and patch
    """

    def test_memoize(self) -> None:

        """
        Test that memoize memoizes a function correctly
        """
        class TestClass:
            """
            Test class to test memoize
            """
            def a_method(self):
                return 42

            @memoize
            def a_memoized_method(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mock_a_method:
            instance = TestClass()
            mock_a_method.return_value = 42

            # Ensure the method returns the correct value
            self.assertEqual(instance.a_memoized_method(), 42)
            self.assertEqual(instance.a_memoized_method(), 42)

            # Ensure the method was only called once
            mock_a_method.assert_called_once()


if __name__ == "__main__":
    unittest.main()
