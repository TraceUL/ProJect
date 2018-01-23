# -*- coding: utf-8 -*-


import scrapy
from scrapy import Request
from pyquery import PyQuery as pq
from ..items import BlogProfileItem
import time
# from scrapy.spider import CrawlSpider, Rule
# from scrapy.linkextractors import LinkExtractor
import re


class PythonSpider(scrapy.Spider):
    name = 'lxf'
    html_url=[]
    have_run_url=[]
    start_urls = ['http://www.runoob.com/python/']



    def parse(self, response):
        # print(response.text)
        parseurl=re.compile('href="(http://www.runoob.com/python/.*?)"')
        all_urls=re.findall(parseurl, response.text)
        for url in all_urls:
            if url not in self.html_url:
                self.html_url.append(url)


        for i in self.html_url:
            if i not in self.have_run_url:
                yield Request(i,callback=self.parse,dont_filter=True)
                yield Request(i, callback=self.parse2,dont_filter=True)
                self.have_run_url.append(i)
                # print(i)
        print(len(self.have_run_url))



    def parse2(self,response):
        item=BlogProfileItem()
        doc= pq(str(response.text))
        title = response.xpath('/html/head/title/text()').extract()
        author=response.xpath('//*[@id="footer"]/div[2]/strong[1]/a/text()').extract()
        create=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


        text = doc('.article-intro').text()
        # print(title,author,create,category,tag)
        item['title']=title
        item['author']=author
        item['created']=create
        item['content'] = text
        yield item


