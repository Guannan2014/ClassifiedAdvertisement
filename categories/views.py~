# -*- coding: utf-8 -*-
import re
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from posts.models import *

def category_view(request, city_code, category_code):
    # get current city, category from url slugs
    found_city = get_object_or_404(City, slug=city_code)
    found_category = get_object_or_404(Category, slug=category_code)
    # all subareas in a city
    subareas = Subarea.objects.filter(city=found_city).order_by('id')
    # all subcategories in the found category
    subcats = Subcategory.objects.filter(category=found_category).order_by('id')

    # create a dictionary to be passed into queryset filter
    filter_dict = {}

    # filters from search get parameters
    # max ask price
    hi = request.GET.get('hi')
    if hi:
        # substitute any , . $ with empty string
        hi_sub = re.sub(r'\,|\.|\$', '', hi)
        # try converting to integer
        try:
            filter_dict['price__lte'] = int(hi_sub)
        # if not integer, then pass, don't add it to filter
        except:
            pass

    # min ask price
    lo = request.GET.get('lo')
    if lo:
        lo_sub = re.sub(r'\,|\.|\$', '', lo)
        try:
            filter_dict['price__gte'] = int(lo_sub)
        except:
            pass
    

    # filter by available picture: django does not store null,
    # only empty strings in the database. can't use isnull filter.
    # so this is a kind of a hack. if pic url > empty string,
    # there could be a pic stored there. 
    pic = request.GET.get('pic')
    if pic == 'on':
        filter_dict['picture1__gt'] = ''

    # location filter
    loc = request.GET.get('loc')
    # BAD HACK empty string to store the converted integer
    loc_int = ''
    if loc:
        try: # try converting to integer, if fails, don't add to filter
            filter_dict['subarea'] = int(loc)
            loc_int = int(loc)
        except:
            pass

    # what to rent out
    avail = request.GET.get('avail')
    if avail:
        filter_dict['rent_out'] = avail
    
    # what structure is the unit
    struct = request.GET.get('struct')
    if struct:
        filter_dict['structure'] = struct

    # subcategory
    sc = request.GET.get('sc')
    # BAD HACK empty string to store the converted integer
    # prevent malicious inputs directly into get parameters that get passed
    # into filter dictionary
    # e.g. user not using select, enter random string or code
    sc_int = ''
    if sc:
        try:
            filter_dict['subcat'] = int(sc)
            sc_int = int(sc)
        except:
            pass
    # other query parameter
    q = request.GET.get('q')
    if q:
        filter_dict['title__icontains'] = request.GET.get('q')

    # look up objects in database by category from url
    category_lookup = {'r': RentPost, 's': SalePost}

    sort = request.GET.get('sort')
    if sort == 'cheapest':
        filtered_posts = category_lookup[category_code].objects.filter(city=found_city, **filter_dict).order_by('-weight', 'price').prefetch_related('subarea')
    elif sort == 'expensive':
        filtered_posts = category_lookup[category_code].objects.filter(city=found_city, **filter_dict).order_by('-weight', '-price').prefetch_related('subarea')
    else:
        filtered_posts = category_lookup[category_code].objects.filter(city=found_city, **filter_dict).order_by('-weight', '-created').prefetch_related('subarea')

    # show X number of posts per page
    paginator = Paginator(filtered_posts, 20)
    page = request.GET.get("page")
    try:
        cur_page = paginator.page(page)
    except PageNotAnInteger:
        # if page is not an integer, deliver first page
        cur_page = paginator.page(1)
    except EmptyPage:
        # if page out of range, show the last page in range
        cur_page = paginator.page(paginator.num_pages)
    
    # prepare pagination with other GET parameters
    query_dict = request.GET.copy()
    # if page is in the dictionary with other parameters, then remove it
    if 'page' in query_dict:
        del query_dict['page']

    house_dict = {'STU':'統倉 Studio',
                  'APT': '公寓 Apartment/Condo',
                  'HOU': '獨立屋 House',
                  'OTH': '其他 Other',
                  'SR': '單間出租',
                  'WU': '整套出租',
                  'SH': '床位/合租'}

    return render(request, 
                  'category.html',
                  {'place': found_city,
                   'category': found_category,
                   'cur_page': cur_page,
                   'subareas': subareas,
                   'subcats': subcats,
                   'hi': hi,
                   'lo': lo,
                   'pic': pic,
                   'sc': sc_int,
                   'struct': struct,
                   'avail': avail,
                   'q': q,
                   'loc': loc_int,
                   'sort': sort,
                   'query_url': query_dict.urlencode(),
                   'house_dict': house_dict})