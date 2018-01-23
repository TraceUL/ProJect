# -*- coding: utf-8 -*-
import scrapy
import re
import time
from pyquery import PyQuery as pq
from ..items import BlogProfileItem






class DjSpider(scrapy.Spider):
    name = 'dj'
    html_url = []
    have_run_url = []
    allowed_domains = ['https://code.ziqiangxuetang.com/django/']
    start_urls = ['https://code.ziqiangxuetang.com/django/django-tutorial.html']




    def parse(self, response):
        # print(response.text)
        parseurl=re.compile('href="(/django/.*?)"')

        all_ur=re.findall(parseurl, response.text)
        for ur in all_ur:
            url='https://code.ziqiangxuetang.com'+ur
            if url not in self.html_url:
                self.html_url.append(url)


        for i in self.html_url:
            if i not in self.have_run_url:
                yield scrapy.Request(i,callback=self.parse,dont_filter=True)
                yield scrapy.Request(i, callback=self.parse2,dont_filter=True)
                self.have_run_url.append(i)
                # print(i)
        print(len(self.have_run_url))

        # print(self.have_run_url)
    def parse2(self,response):
        doc=pq(str(response.text))
        item = BlogProfileItem()
        title = response.xpath('/html/head/title/text()').extract()
        author = "自强学堂"
        create = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        text = doc('#main_content').text()

        item['title'] = title
        item['author'] = author
        item['created'] = create
        item['content'] = text
        yield item
