#!/usr/bin/env python3
"""
TestAccessNestedMap class that inherits from unittest.TestCase
"""
from utils import access_nested_map
import unittest
from parameterized import parameterized, parameterized_class
from unittest.mock import patch
from typing import Mapping


class TestAccessNestedMap(unittest.TestCase):
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, excepted):
        service = access_nested_map(nested_map, path)
        self.assertEqual(service, excepted)

    @parameterized.expand([({}, ("a",)), ({"a": 1},("a", "b"))])
    def test_access_nested_map_exception(self, nested_map, path):
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


if __name__ == '__main__':
    unittest.main()
