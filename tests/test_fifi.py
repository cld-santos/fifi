#!/usr/bin/env python3
from unittest import TestCase
from ..fifi import investigate


class TestFifi(TestCase):

    # def test_get_html_page(self):
    #     result = investigate('humor', 'http://claudio-santos.com/')
    #     print('result', result)
    #     # self.assertTrue(result)

    def test_get_html_page_from_government(self):
        investigate('febre amarela', 'http://www.brasil.gov.br/home-1/ultimas-noticias')
