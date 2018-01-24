import sys
from fifi import investigate

if __name__=='__main__':
    subject = sys.argv[1]
    url = sys.argv[2]

    # investigate('febre amarela', 'http://www.brasil.gov.br/home-1/ultimas-noticias')
    investigate(subject, url)
