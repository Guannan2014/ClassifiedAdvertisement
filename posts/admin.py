from django.contrib import admin
from posts.models import *
# Register your models here.


class SalePostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', 'approved', 'details', 'weight')
    list_filter = ('created', 'approved', 'city')
    date_hierarchy = 'created'
    ordering = ('-weight', '-created',)

admin.site.register(SalePost, SalePostAdmin)

class RentPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', 'approved', 'details', 'weight')
    list_filter = ('created', 'approved', 'city')
    date_hierarchy = 'created'
    ordering = ('-weight', '-created',)

admin.site.register(RentPost, RentPostAdmin)