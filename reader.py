#!/usr/bin/env python3
from time import sleep
from selenium import webdriver
from .parser import FifiParser


def get_html_from(url):
    driver = webdriver.Firefox()
    driver.get(url)
    sleep(5)
    html_page = driver.page_source
    driver.close()

    fifi_parser = FifiParser()
    fifi_parser.feed(html_page)

    return fifi_parser.document
