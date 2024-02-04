#!/usr/bin/env python3
"""
TestAccessNestedMap class that inherits from unittest.TestCase
"""
from utils import access_nested_map, get_json
import unittest
from parameterized import parameterized, parameterized_class
from unittest.mock import patch, Mock
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

    @parameterized.expand([({}, ("a",)), ({"a": 1}, ("a", "b"))])
    def test_access_nested_map_exception(self, nested_map, path):
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mock_req_json):
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_req_json.return_value = mock_response
        serv = get_json(test_url)
        self.assertEqual(serv, test_payload)
        mock_req_json.assert_called_once_with(test_url)


if __name__ == '__main__':
    unittest.main()
