import sys
import datetime
from pymongo import MongoClient
from .reader import get_html_from
from .finder import HtmlFinder


def investigate(subject, url):
    print('look in url {0}'.format(url))

    document = get_html_from(url)
    finder = HtmlFinder(document)

    print('Finding "{0}" in {1}'.format(subject, url))    
    elements = finder.find_subject(subject)

    # Getting Elements with the subject searched term 
    client = MongoClient("mongodb+srv://csantos:amarela@febre-amarela-voxfg.mongodb.net/test")
    db = client['febre-amarela']
    # TODO: Get the context of information.
    for element in elements:
        info = {}
        date = datetime.datetime.today()
        info['content'] = element.get('data', "")
        info['date'] = date.strftime("%d/%m/%Y %H:%M")
        info['url'] = url
        db.inventory.insert_one(info)

    # Finding references (aka links) with the subject searched term  
    references = finder.find_references(subject)
    for reference in references:
        href = reference.get('attributes')['href']
        if href == url:
            continue
        # TODO: Change to http Match regex
        if 'http:' != href[0:5].lower():
            href = '{0}/{1}'.format(url, href)
            href = href.split('?')[0] + "/" if '?' in href else href
        investigate(subject, href)

    # Finding references (aka links) to next pages
    next_references = []
    for item in ['próximo', 'proximo', 'next']:
        next_references.extend(finder.find_references(item))
    for reference in next_references:
        href = reference.get('attributes')['href']
        href = href if 'http:' == href[0:5] else '{0}/{1}'.format(url, href) 
        investigate(subject, href)


if __name__=='__main__':
    subject = sys.argv[1]
    url= sys.argv[2]

    # investigate('febre amarela', 'http://www.brasil.gov.br/home-1/ultimas-noticias')
    investigate(subject, url)
