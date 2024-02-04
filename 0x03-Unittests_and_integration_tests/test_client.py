#!/usr/bin/env python3
"""
TestAccessNestedMap class that inherits from unittest.TestCase
"""
from client import GithubOrgClient
import unittest
from parameterized import parameterized, parameterized_class
from unittest.mock import patch, Mock
from typing import Mapping
from utils import memoize


class TestGithubOrgClient(unittest.TestCase):
    @parameterized.expand([('google'), ('abc')])
    patch('client.get_json')

    def test_org(self, pr, mock):
        servise = GithubOrgClient(pr)
        servise.org(pr)
        mock.assert_called_once_with(get_json())
