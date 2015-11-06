from django.shortcuts import render, get_object_or_404, redirect
from posts.models import *

def index(request):
    #user_city_pref = request.session.get('cityslug')
    #if user_city_pref:
    #    return redirect('/' + user_city_pref)
    return render(request, 'index.html')

def reset_city(request):
    if request.session.get('cityslug'):
        del request.session['cityslug']
    if request.session.get('usercity'):
        del request.session['usercity']
    return redirect('/')
 
def city_view(request, city_code):
    found_city = get_object_or_404(City, slug=city_code)
    request.session['usercity'] = found_city.name_eng
    request.session['cityslug'] = found_city.slug
    recent_rent = RentPost.objects.filter(city=found_city).order_by('-created').prefetch_related('subarea')[:4]
    recent_sale = SalePost.objects.filter(city=found_city).order_by('-created').prefetch_related('subarea')[:4]
    no_rent = True if not recent_rent else False
    no_sale = True if not recent_sale else False

    return render(request,
                  'city.html',
                  {'recent_rent': recent_rent,
                   'recent_sale': recent_sale,
                   'no_rent': no_rent,
                   'no_sale': no_sale,
                   'cur_city': found_city})
