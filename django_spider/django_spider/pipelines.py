# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from blog.models import Category,Tag

class BlogProfilePipeline(object):
    def process_item(self, item, spider):
        item['category'] = Category.objects.get(id=3)
        item['tag'] = Tag.objects.get(id=2)
        item.save()
        return item
