#!/usr/bin/env python3
import time
from html.parser import HTMLParser


class FifiParser(HTMLParser):

    def __init__(self):
        super().__init__()
        self.document = {}
        self.actual_tag = []

    def handle_starttag(self, tag, attrs):
        self.actual_tag.append('id_{0}'.format(str(time.time())))
        actual_tag_idx = len(self.actual_tag) - 1
        parent = self.actual_tag[actual_tag_idx - 1] if (actual_tag_idx - 1) >= 0 else None
        self.document[self.actual_tag[actual_tag_idx]] = {'tag': tag, 'parent': parent, 'data': None}

    def handle_endtag(self, tag):
        self.actual_tag.pop()

    def handle_data(self, data):
        self.document[self.actual_tag[len(self.actual_tag) - 1]]['data'] = data
