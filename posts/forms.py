from django.forms import ModelForm
from posts.models import *

class SalePostForm(ModelForm):
    def __init__(self, city, *args, **kwargs):
        super(SalePostForm, self).__init__(*args,**kwargs) # populates the post
        # <BAD> hardcoding the category in
        cat = Category.objects.get(id=2)
        # get the dropdown of subcategories from category
        self.fields['subcat'].queryset = Subcategory.objects.filter(category=cat).order_by('id')
        self.fields['subarea'].queryset = Subarea.objects.filter(city=city).order_by('id')
        
    class Meta:
        model = SalePost
        fields = ('title', 'price', 'subcat', 'picture1', 'subarea', 'details',  
        		  'contact_person', 'phone', 'email', 'qq', 'weixin')

class RentPostForm(ModelForm):
    def __init__(self, city, *args, **kwargs):
        super(RentPostForm, self).__init__(*args, **kwargs)
        self.fields['subarea'].queryset = Subarea.objects.filter(city=city).order_by('id')

    class Meta:
        model = RentPost
        fields = ('title', 'price', 'rent_out', 'subarea', 'picture1',
                  'structure', 'total_rooms', 'total_baths', 'details', 
                  'address', 'contact_person', 'phone', 'email', 'qq',
                  'weixin')
