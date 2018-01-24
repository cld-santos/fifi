#!/usr/bin/env python3
from unittest import TestCase
from ..parser import FifiParser


class TestFifiParser(TestCase):

    def test_must_read_a_simple_html(self):
        fifi_parser = FifiParser()
        fifi_parser.feed('<html><body><div class="item">meu item 1</div><div class="item">meu item 2</div><div class="item">meu item 3</div></body></html>')
        self.assertEqual(5, len(fifi_parser.document))

    def test_must_read_html(self):
        a_count = 0
        fifi_parser = FifiParser()
        fifi_parser.feed('<html>    <body>      <div class="item">meu item 1            <div>           <a href="link-1">teste</a>          </div>      </div>      <div class="item">meu item 2            <div>               <a href="link-2">teste</a>          </div>      </div>      <div class="item">meu item 3            <div>               <a href="link-3">teste</a>          </div>      </div>  </body></html>')

        for idx in fifi_parser.document:
            element = fifi_parser.document[idx]
            if element.get('tag', None) == 'a':
                a_count += 1
                parent = element.get('parent', None)
                if parent:
                    self.assertEqual(fifi_parser.document[parent]['tag'], 'div')

        self.assertEqual(a_count, 3)

