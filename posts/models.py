# -*- coding: utf-8 -*-
import os
import uuid
from time import strftime
from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db.models.signals import pre_delete, pre_save
from easy_thumbnails.fields import ThumbnailerImageField
from locations.models import *
from categories.models import *

# custom validators
def validate_not_whitespace_only(value):
    if value.strip() == '':
        raise ValidationError(u"請輸入除空白字符以外的字符")

def get_image_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('usrpix', strftime("%Y/%m/%d"), filename)

# Create your models here.
class BasicPost(models.Model):
    poster = models.ForeignKey(User)
    cat = models.ForeignKey(Category)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=100, 
                             verbose_name=u'標題', 
                             help_text=u'必填 最多100字',
                             validators=[validate_not_whitespace_only])
    details = models.TextField(max_length=3000, 
                               blank=True, 
                               verbose_name=u'詳細描述')
    # contact details
    contact_person = models.CharField(max_length=30, 
                                      blank=True, 
                                      verbose_name=u'聯系人')
    phone = models.CharField(max_length=20, 
                             blank=True, 
                             verbose_name=u'電話')
    email = models.EmailField(blank=True, verbose_name=u'E-mail')
    qq = models.CharField(max_length=30, blank=True, verbose_name=u'QQ')
    weixin = models.CharField(max_length=30, blank=True, verbose_name=u'微信')
    # Relational keys
    city = models.ForeignKey(City, verbose_name=u'城市')
    subarea = models.ForeignKey(Subarea,
                                verbose_name=u'區域',
                                blank=True,
                                null=True)
    
    # Algorithmic display of posts
    approved = models.BooleanField(default=False)
    weight = models.PositiveSmallIntegerField(default=1)
    picture1 = ThumbnailerImageField(upload_to=get_image_path,
                                     null=False,
                                     blank=True,
                                     default='',
                                     verbose_name=u'上傳照片',
                                     max_length=256,
                                     help_text=u'僅限圖片文件(jpg, png, gif等)',
                                     resize_source=dict(size=(640, 0), crop='smart', upscale=False))

    class Meta:
        abstract = True

    def __unicode__(self):
        return u'%s' % (self.title)


class PricedPost(BasicPost):
    price = models.PositiveIntegerField(verbose_name=u'價格',
                                        help_text=u'必填 以當地貨幣爲準 例: 1000')

    class Meta:
        abstract = True

class SalePost(PricedPost):
    subcat = models.ForeignKey(Subcategory, 
                               verbose_name=u'分類',
                               help_text=u'必選')

class RentPost(PricedPost):
    ZERO = 0
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVEPLUS = 5
    NUM_ROOMS = (
        (ZERO, '0'),
        (ONE, '1'),
        (TWO, '2'),
        (THREE, '3'),
        (FOUR, '4'),
        (FIVEPLUS, '5+'),
    )

    HOUSE_TYPE = (
        ('STU', '統倉型 Studio'),
        ('APT', '公寓型 Apt/Condo'),
        ('HOU', '獨立屋 House'),
        ('OTH', '其他型 Other'),
    )

    RENT_TYPE = (
        ('SR', '單間出租'),
        ('WU', '整套出租'),
        ('SH', '床位/合租一間'),
    )
    total_rooms = models.SmallIntegerField(choices=NUM_ROOMS,
                                                   verbose_name=u'房屋臥室總數',
                                                   blank=True,
                                                   null=True)
    total_baths = models.SmallIntegerField(choices=NUM_ROOMS,
                                                   verbose_name=u'房屋浴室總數',
                                                   blank=True,
                                                   null=True)
    structure = models.CharField(max_length=3,
                                 choices=HOUSE_TYPE,
                                 verbose_name=u'房屋結構',
                                 blank=True)
    rent_out = models.CharField(max_length=2,
                                choices=RENT_TYPE,
                                verbose_name=u'出租類型',
                                help_text=u'必選')
    address = models.CharField(max_length=200,
                               verbose_name=u'具體地址',
                               help_text='例: 405 Hilgard Ave, Los Angeles, CA 90095',
                               blank=True)

# clean up thumbnails at listing deletion
def cleanup_thumbnails(sender, **kwargs):
    model = kwargs['instance']
    if bool(model.picture1):
        model.picture1.delete()

pre_delete.connect(cleanup_thumbnails, sender=RentPost)
pre_delete.connect(cleanup_thumbnails, sender=SalePost)