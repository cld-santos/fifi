#!/usr/bin/env python3
from unittest import TestCase
from ..parser import FifiParser
from ..finder import HtmlFinder


class TestFinder(TestCase):

    def test_must_found_a_subject_mentioned(self):
        fifi_parser = FifiParser()
        fifi_parser.feed('<html>    <body>      <div class="item">meu item 1            <div>           <a href="link-1">teste</a>          </div>      </div>      <div class="item">meu item 2            <div>               <a href="link-2">teste</a>          </div>      </div>      <div class="item">meu item 3            <div>               <a href="link-3">alvo</a>           </div>      alvo</div>  </body></html>')
        finder = HtmlFinder(fifi_parser.document)
        result = finder.find_subject('alvo')
        self.assertEqual(1, len(result))

    def test_must_found_a_uppercase_subject(self):
        fifi_parser = FifiParser()
        fifi_parser.feed('<html>    <body>      <div class="item">            <div>           <a href="link-1">teste</a>          </div>      </div>      <div class="item">meu item 2            <div>               <a href="link-2">teste</a>          </div>      </div>      <div class="item">meu item 3            <div>               <a href="link-3">alvo</a>           </div>     alvo </div>  meu item 1</body></html>')
        finder = HtmlFinder(fifi_parser.document)
        result = finder.find_subject('ALVO')
        self.assertEqual(1, len(result))

    def test_must_not_found_a_subject(self):
        fifi_parser = FifiParser()
        fifi_parser.feed('<html>    <body>      <div class="item">meu item 1            <div>           <a href="link-1">teste</a>          </div>      </div>      <div class="item">meu item 2            <div>               <a href="link-2">teste</a>          </div>      </div>      <div class="item">meu item 3            <div>               <a href="link-3">alvo</a>           </div>      </div>  </body></html>')
        finder = HtmlFinder(fifi_parser.document)
        result = finder.find_subject('termo inexistente')
        self.assertEqual(0, len(result))

    def test_must_found_a_complex_subject(self):
        fifi_parser = FifiParser()
        fifi_parser.feed('<html>    <body>      <div class="item">meu item 1            <div>           <a href="link-1">teste</a>          </div>      </div>      <div class="item">meu item 2            <div>               <a href="link-2">teste</a>          </div>      </div>      <div class="item">meu item 3            <div>               <a href="link-3">Alvo Existente</a>           </div>Alvo Existente      </div>  </body></html>')
        finder = HtmlFinder(fifi_parser.document)
        result = finder.find_subject('Alvo Existente')
        self.assertEqual(1, len(result))

    def test_must_found_more_than_one_subject(self):
        fifi_parser = FifiParser()
        fifi_parser.feed('<html>    <body>      <div class="item">meu item 1            <div>           <a href="link-1">teste</a>          </div>      </div>      <div class="item">meu item 2            <div>               <a href="link-2">Alvo Existente</a>          </div>Alvo Existente      </div>      <div class="item">meu item 3            <div>               <a href="link-3">Alvo Existente</a>           </div>Alvo Existente      </div>  </body></html>')
        finder = HtmlFinder(fifi_parser.document)
        result = finder.find_subject('Alvo Existente')
        self.assertEqual(2, len(result))
