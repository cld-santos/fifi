#!/usr/bin/env python3
from unittest import TestCase
from ..reader import get_html_from


class TestReader(TestCase):

    def test_get_html_page(self):
        result = get_html_from('http://claudio-santos.com/')
        self.assertTrue(result)
