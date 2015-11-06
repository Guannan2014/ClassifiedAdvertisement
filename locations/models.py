from django.db import models
from core.models import BasicInfo

# Create your models here.
# 'Continent' class to represent continents
class Continent(BasicInfo):
    pass

# 'Country' class to represent countries
class Country(BasicInfo):
    continent = models.ForeignKey(Continent, blank=True, null=True)

# 'State' class to represent states in a country
class State(BasicInfo):
    country = models.ForeignKey(Country)

# 'City' class to represent cities in a state
class City(BasicInfo):
    state = models.ForeignKey(State)

# 'Subarea' class to represent subareas in a city
class Subarea(BasicInfo):
    city = models.ForeignKey(City)

# Neighbor'hood' class to represent neighborhoods in a district
class Hood(BasicInfo):
    subarea = models.ForeignKey(Subarea)