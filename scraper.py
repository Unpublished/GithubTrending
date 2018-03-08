# coding:utf-8

import codecs
import errno
import json
import os
from collections import OrderedDict

import requests
from pyquery import PyQuery as pq


def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc:  # Python > 2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise


def scrape_int(param):
    text = param
    if not isinstance(text, str):
        text = param.text().strip()
    return int(text.replace(',', ''))


def scrape(language='all'):
    for t in ['daily', 'weekly', 'monthly']:
        scrape_time_span(t, language)


def scrape_time_span(time_span, language='all'):
    assert language == 'all'
    filename = "trending_{time_span}-{language}.json".format(time_span=time_span, language=language)

    url = 'https://github.com/trending'
    if not language == 'all':
        url = url + '/' + language

    url = url + '?since=' + time_span

    r = requests.get(url)
    assert r.status_code == 200

    # mkdir_p(os.path.dirname(filename))

    # print(r.encoding)

    d = pq(r.content)
    items = d('ol.repo-list li')

    # codecs to solve the problem utf-8 codec like chinese
    with codecs.open(filename, mode="w", encoding="utf-8") as f:
        array = []
        for item in items:
            i = pq(item)
            repo = i("h3 a").contents()[2].strip()
            owner = i("h3 a span").text()[0:-1].strip()
            description = i("p.col-9").text().strip()
            language = i('span[itemprop="programmingLanguage"]').text()
            stars = scrape_int(i('a[href$="stargazers"]'))
            forks = scrape_int(i('a[href$="network"]'))
            new_stars = scrape_int(i('span:last').text().replace('stars today', '')
                                   .replace('stars this week', '')
                                   .replace('stars this month', '').strip())
            d = OrderedDict()
            d['description'] = description
            d['language'] = language
            d['repo'] = repo
            d['new_stars'] = new_stars
            d['stars'] = stars
            d['owner'] = owner
            d['forks'] = forks
            array.append(d)

        f.write(json.dumps(array))


if __name__ == '__main__':
    scrape()
