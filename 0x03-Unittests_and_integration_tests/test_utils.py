#!/usr/bin/env python3
"""
Unittests for utils.py
"""

import unittest
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
    def test_access_nested_map(self, nested_map: Mapping, path: Sequence, expected: Any) -> None:
        from utils import access_nested_map
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map: Mapping, path: Sequence) -> None:
        from utils import access_nested_map
        with self.assertRaises(KeyError) as cm:
            access_nested_map(nested_map, path)
        self.assertEqual(cm.exception.args[0], path[-1])

    @patch('utils.requests.get')
    def test_get_json(self, mock_get: Mock) -> None:
        # Define test cases
        test_cases = [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False}),
        ]

        for test_url, test_payload in test_cases:
            with self.subTest(test_url=test_url, test_payload=test_payload):
                # Set up the mock to return a Mock response with a json method
                mock_response = Mock()
                mock_response.json.return_value = test_payload
                mock_get.return_value = mock_response

                # Call the function
                result: Dict[str, Any] = get_json(test_url)

                # Check that the mock was called with the correct URL
                mock_get.assert_called_once_with(test_url)

                # Check that the result is as expected
                self.assertEqual(result, test_payload)

                # Reset the mock for the next iteration
                mock_get.reset_mock()

    class TestMemoize(unittest.TestCase):
        """
        test cases using memoize decorator
        """

        class TestClass:
            """
            Test class
            """
            def a_method(self) -> int:
                """
                specifies that it retuurns an int
                """
                return 42

        @memoize
        def a_property(self) -> int:
            """
            specifies that it returns an integer
            """
            return self.a_method()

        def test_memoize(self) -> None:
            """
            tests the memoization behavior
            """
            with patch.object(self.TestClass, 'a_method') as mock_a_method:
                # Call the property twice
                obj = self.TestClass()
                result1 = obj.a_property
                result2 = obj.a_property

                # Assert that a_method was called only once
                mock_a_method.assert_called_once()

                # Assert that the results are correct
                self.assertEqual(result1, 42)
                self.assertEqual(result2, 42)


if __name__ == "__main__":
    unittest.main()
