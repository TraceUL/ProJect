# -*- coding:utf-8 -*-

import xadmin
from xadmin import views
from .models import BlogProfile,Category,Tag


class BaseSetting(object):
    enable_themes =True
    use_bootswatch = True



class GlobalSetting(object):
    site_title = "后台管理"
    site_footer = "博客后台"
    menu_style = "accordion"


class BlogProfileXAdmin(object):
    list_display = ['title', 'author', 'content', 'created', 'category','tag']
    search_fields = ['title', 'author', 'content',  'category','tag']
    list_filter = ['title', 'author', 'content', 'created', 'category','tag']

class TagXadmin(object):
    list_display = [ 'tag']
    search_fields = ['tag']
    list_filter = ['tag']



class CategoryXadmin(object):
    list_display = ['name']
    search_fields = ['name']
    list_filter = ['name']


xadmin.site.register(BlogProfile, BlogProfileXAdmin)
xadmin.site.register(Tag, TagXadmin)
xadmin.site.register(Category, CategoryXadmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSetting)