from subprocess import call


def scrape_int(param):
    text = param
    if not isinstance(text, str):
        text = param.text().strip()
    if not text:
        return 0
    return int(text.replace(',', ''))


def scrape(language='all'):
    # call(['scrapy', 'list'])
    for t in ['daily', 'weekly', 'monthly']:
        spider = 'trending_{t}-{lang}'.format(t=t, lang=language)
        call(['scrapy', 'crawl', spider, '-o', spider + '.json'])


if __name__ == '__main__':
    scrape()
