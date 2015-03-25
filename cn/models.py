#coding:utf8
from django.db import models

# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=200)
    pic = models.ImageField('图片',upload_to='uploadImages')
    pub_date = models.DateField()
    puber = models.CharField(max_length=50)
    views = models.CharField(max_length=100)
    content1 = models.CharField(max_length=5000)
    content2 = models.CharField(max_length=1000)

    def __unicode__(self):
	return self.title
