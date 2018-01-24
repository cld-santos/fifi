#!/usr/bin/env python3


class HtmlFinder():

    def __init__(self, document):
        self.document = document

    def find_subject(self, subject):
        subject = subject.lower()
        elements_found = []
        for idx in self.document:
            element = self.document[idx]
            if subject in element.get('data', "").lower():
                elements_found.append(self.document[idx])
        return elements_found
