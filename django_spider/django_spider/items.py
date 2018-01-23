# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy_djangoitem import DjangoItem
import django
django.setup()
from blog.models import BlogProfile




class BlogProfileItem(DjangoItem):
    django_model =BlogProfile
