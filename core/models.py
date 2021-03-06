from django.db import models

# Create your models here.
# Abstract base model called 'BasicInfo' that contains basic information like:
#       the name in English, Simplified & Traditional Chinese, a slug to hold url
class BasicInfo(models.Model):
    name_eng = models.CharField(max_length=30)
    name_gbk = models.CharField(max_length=30, blank=True)
    name_bg5 = models.CharField(max_length=30, blank=True)
    slug = models.SlugField(max_length=30, blank=True)

    class Meta: # define as abstract base class in django
        abstract = True

    def __unicode__(self):
        # return u'%s, %s, %s, %s' % (
        #         self.name_eng, 
        #         self.name_gbk, 
        #         self.name_bg5, 
        #         self.slug)
        return u'%s%s' % (self.name_bg5, self.name_eng)
