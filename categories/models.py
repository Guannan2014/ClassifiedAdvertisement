from django.db import models
from core.models import BasicInfo
# Create your models here.
class Category(BasicInfo):
	pass

class Subcategory(BasicInfo):
	category = models.ForeignKey(Category)

class Subtype(BasicInfo):
	subcategory = models.ForeignKey(Subcategory)