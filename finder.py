#!/usr/bin/env python3


class HtmlFinder():

    def __init__(self, document):
        self.document = document

    def find_subject(self, subject):
        subject = subject.lower()
        elements_found = []
        for idx in self.document:
            element = self.document[idx]
            data = element.get('data', "")
            if data and element.get('tag') != 'a' and subject in data.lower():
                elements_found.append(self.document[idx])
        return elements_found

    def find_references(self, subject):
        subject = subject.lower()
        elements_found = []
        for idx in self.document:
            element = self.document[idx]
            data = element.get('data', "")
            if data and element.get('tag') == 'a' and subject in data.lower():
                elements_found.append(self.document[idx])
        return elements_found
