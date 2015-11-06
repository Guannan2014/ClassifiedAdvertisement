# -*- coding: utf-8 -*-
from itertools import chain
from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.core.exceptions import PermissionDenied, SuspiciousOperation
from django.contrib.auth.decorators import login_required
from django.db.models.signals import pre_delete
from .models import *
from .forms import *

# Create your views here.
@login_required
def post_type(request, city_code):
	"""View for users to choose which type of post to make"""
	city = get_object_or_404(City, slug=city_code)
	return render(request, 'post_type.html', {'place': city})

@login_required
def new_post(request, city_code, post_type):
	""" Render the form for users to make a new post. """
	city = get_object_or_404(City, slug=city_code)
	if post_type not in ('fos', 'hrr'):
		raise Http404
	# prevent user from posting more than 3 listings
	# unless they are superuser
	rent_post_list = RentPost.objects.filter(poster=request.user)
	sale_post_list = SalePost.objects.filter(poster=request.user)
	num_posts = len(list(chain(rent_post_list, sale_post_list)))
	if num_posts >= 3 and not request.user.is_superuser:
		return redirect('max_posts_exceeded')
	# if the method is post, post to the form
	if request.POST:
		if post_type == 'fos':
			form = SalePostForm(city, request.POST, request.FILES)
			form_type_text = '集市'
			post_category_id = Category.objects.get(id=2)
		else:
			form = RentPostForm(city, request.POST, request.FILES)
			form_type_text = '房源'
			post_category_id = Category.objects.get(id=1)
		if form.is_valid():
			p = form.save(commit=False)
			p.city = city
			p.approved = False
			p.weight = 1
			p.poster = request.user
			p.cat = post_category_id
			p.save()
			return redirect('/%s/post/thanks/' %(city_code))
	else:
		if post_type == 'fos':
			form_type_text = '集市'
			form = SalePostForm(city)
		else:
			form_type_text = '房源'
			form = RentPostForm(city)
	return render(request, 'new_post.html', 
				  {'form': form, 
				   'place': city, 
				   'form_type_text': form_type_text})


def post_thanks(request, city_code):
	""" Thanks page after form is submitted """
	city = get_object_or_404(City, slug=city_code)
	return render(request, 'post_thanks.html', {'place': city})

def single_post(request, city_code, category_code, post_id):
	""" Detailed, single post view """
	city = get_object_or_404(City, slug=city_code)
	category = get_object_or_404(Category, slug=category_code)
	cat_lookup = {'r': (RentPost, 'RTP'), 's': (SalePost, 'SLP')}
	post = get_object_or_404(cat_lookup[category_code][0], id=post_id)
	house_dict = {'STU':'統倉 Studio',
			      'APT': '公寓 Apt/Condo',
			      'HOU': '獨立屋 House',
			      'OTH': '其他 Other',
			      'SR': '單間出租',
			      'WU': '整套出租',
		          'SH': '床位/合租一間'}
	return render(request, 
				  'single_post.html', 
				  {'post': post, 
				   'id_prefix': cat_lookup[category_code][1],
				   'place': city,
				   'house_dict': house_dict})

@login_required
def manage_posts(request):
	""" Lets logged-in user see the list of posts, of which
		they are eligible to edit and delete. """
	rent_post_list = RentPost.objects.filter(poster=request.user).prefetch_related('city', 'cat').order_by('-id')
	sale_post_list = SalePost.objects.filter(poster=request.user).prefetch_related('city', 'cat').order_by('-id')
	result_list = list(chain(rent_post_list, sale_post_list))
	num_posts = len(result_list)
	return render(request,
				  'manage_posts.html',
				  {'users_posts': result_list,
				   'num_posts': num_posts})

@login_required
def edit_post_success(request):
	return render(request, 'edit_success.html')

@login_required
def edit_post(request, cat_slug, post_id):
	""" Lets uer edit a post """
	# map category to type of post in dictionary
	cat_dict = {'r': RentPost,
				's': SalePost}
	cat_form_dict = {'r': RentPostForm,
					 's': SalePostForm}
	# if the category is rent or sale, return 404
	if cat_slug not in cat_dict:
		raise Http404

	# get the post by category and post id
	post_edited = get_object_or_404(cat_dict[cat_slug], id=post_id)
	# if the user is not the owner of the post, deny permissions
	if post_edited.poster != request.user:
		raise SuspiciousOperation
	city = post_edited.city

	# if request is post, check form is valid, then save
	if request.POST:
		form = cat_form_dict[cat_slug](city, request.POST, request.FILES, instance=post_edited)
		if form.is_valid():
			p = form.save(commit=False)
			p.save()
			return redirect('edit_post_success')
	# else render the form with pre existing data as get
	else:
		form = cat_form_dict[cat_slug](city, instance=post_edited)

	return render(request,
				  'edit_post.html',
				  {'form': form})

@login_required
def delete_post_success(request):
	return render(request, 'delete_success.html')

@login_required
def delete_post(request, cat_slug, post_id):
	cat_dict = {'r': RentPost,
				's': SalePost}
	if cat_slug not in cat_dict:
		raise Http404
	post_deleted = get_object_or_404(cat_dict[cat_slug], id=post_id)
	if post_deleted.poster != request.user:
		raise SuspiciousOperation
	if request.POST:
		post_deleted.delete()
		return redirect('delete_post_success', )
	return render(request,
				  'delete_confirm.html',
				  {'post_deleted': post_deleted})

@login_required
def max_posts_exceeded(request):
	return render(request, 'max_posts_exceeded.html')
