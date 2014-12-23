#!/usr/bin/env python
#coding=utf8


""" Crawl all the posts of a qq group.
Simulate a user login by filling cookie in headers.
"""


import os
import re
import urlparse
import requests
from lxml import etree


class Crawler(object):

    def __init__(self, home_url, cookie, user_agent, outpath):
        self.home_url = home_url
        self.host = home_url.rsplit('/', 1)[0]
        self.headers = {
            'User-Agent': user_agent,
            'Cookie': cookie
        }
        self.parser = etree.HTMLParser()
        self.outpath = outpath

    def _get_posts(self, url):
        r = requests.get(url, headers=self.headers)
        tree = etree.fromstring(r.content, self.parser)
        links = tree.xpath('//div[@id="threadlist"]/div/dl/dt/a')

        if not links:
            return None

        for link in links:
            href = link.get('href')
            post_url = urlparse.urljoin(self.host, href)
            r_post = requests.get(post_url, headers=self.headers)
            outfile = os.path.join(self.outpath, href.replace('/', '_') + '.html')
            with open(outfile, 'w') as f:
                f.write(r_post.content)
            print 'Done:', link.get('title')

        return True

    def start(self):
        page = 1
        while True:
            url = '{home}?page={page}'.format(home=self.home_url, page=page)
            print url
            r = self._get_posts(url)
            if not r:
                break
            page += 1


def main():
    from config import QQ_GROUP_URL, COOKIE, USER_AGENT, OUTPATH
    r = re.search(r'(http://qgc.qq.com/\d+)', QQ_GROUP_URL)
    if not r:
        print 'Invalid QQ_GROUP_URL:', QQ_GROUP_URL
        return
    home_url = r.group(1)
    if not os.path.isdir(OUTPATH):
        os.makedirs(OUTPATH)

    crawler = Crawler(home_url, COOKIE, USER_AGENT, OUTPATH)
    crawler.start()


if __name__ == '__main__':
    main()
