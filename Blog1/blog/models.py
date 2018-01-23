# -*- coding:utf-8 -*-

from django.db import models

# Create your models here.





class Category(models.Model):
    name=models.CharField(max_length=16,verbose_name='分类')
    class Meta:
        verbose_name = u"分类"
        verbose_name_plural = verbose_name

    # def __unicode__(self):
    def __str__(self):
        return self.name

class Tag(models.Model):
    tag = models.CharField(max_length=16,verbose_name='标签')
    class Meta:
        verbose_name = u"标签"

        verbose_name_plural = verbose_name

    # def __unicode__(self):
    def __str__(self):
        return self.tag

class BlogProfile(models.Model):


    title = models.CharField(max_length=50,verbose_name="标题",default="")
    author = models.CharField(verbose_name="作者",max_length=16,default="")
    created = models.DateTimeField(verbose_name="发布时间",auto_now_add=True)
    category = models.ForeignKey(Category,verbose_name='类型')

    tag=models.ForeignKey(Tag,verbose_name="标签")
    content = models.TextField(blank = True, null = True)
    class Meta:
        verbose_name = u"博客信息"
        verbose_name_plural = verbose_name

    # 关于Meta：https://www.chenshaowen.com/bl     og/the-django-model-meta/

    def __unicode__(self):
        return self.title