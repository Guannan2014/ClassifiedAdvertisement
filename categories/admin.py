from django.contrib import admin
from categories.models import *
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
	pass
	
admin.site.register(Category, CategoryAdmin)

class SubcategoryAdmin(admin.ModelAdmin):
	pass

admin.site.register(Subcategory, SubcategoryAdmin)

class SubtypeAdmin(admin.ModelAdmin):
	pass

admin.site.register(Subtype, SubtypeAdmin)
