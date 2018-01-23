# -*- coding: utf-8 -*-
import scrapy
import re
from pyquery import PyQuery as pq
import time


from ..items import BlogProfileItem



class JsjcSpider(scrapy.Spider):
    name = 'jsjc'
    html_url = []
    allowed_domains = ['http://www.w3school.com.cn/js/']
    start_urls = ['http://www.w3school.com.cn/js/']


    def parse(self, response):
        parseurl=re.compile('href="(/js/.*?)"')
        all_ur=re.findall(parseurl, response.text)
        for ur in all_ur:
            url='http://www.w3school.com.cn'+ur
            if url not in self.html_url:
                self.html_url.append(url)
                yield scrapy.Request(url, callback=self.parse, dont_filter=True)
                yield scrapy.Request(url, callback=self.parse2, dont_filter=True)


    def parse2(self,response):
        doc=pq(str(response.text))
        item = BlogProfileItem()
        title = response.xpath('/html/head/title/text()').extract()
        author = "w3school"
        create = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        text = doc('#maincontent').text()
        print(title,'------',text,response.url)

        item['title'] = title
        item['author'] = author
        item['created'] = create
        item['content'] = text
        yield item
