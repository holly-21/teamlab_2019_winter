from django.shortcuts import render, get_object_or_404, redirect
from third2.models import Restaurants, Review
from django.core.paginator import Paginator
from third2.forms import RestaurantsForm, ReviewForm
from django.http import HttpResponseRedirect


# Create your views here.
def list(request):
    restaurants = Restaurants.objects.all()
    paginator = Paginator(restaurants, 5)

    page = request.GET.get('page')  ## third2/list?page=1
    items = paginator.get_page(page)

    context = {
        'restaurants': items
    }
    return render(request, 'third2/list.html', context)


def create(request):
    if request.method == 'POST':
        form = RestaurantsForm(request.POST)
        if form.is_valid():
            new_item = form.save()
        return HttpResponseRedirect('/third2/list/')
    form = RestaurantsForm()
    return render(request, 'third2/create.html', {'form': form})


def update(request):
    if request.method == 'POST' and 'id' in request.POST:
        # item = Restaurants.objects.get(pk=request.POST.get('id'))
        item = get_object_or_404(Restaurants, pk=request.POST.get('id'))
        form = RestaurantsForm(request.POST, instance=item)
        if form.is_valid():
            item = form.save()
    elif request.method == 'GET':
        # item = Restaurants.objects.get(pk=request.GET.get('id'))  ##third2/update?id=2
        item = get_object_or_404(Restaurants, pk=request.GET.get('id'))
        form = RestaurantsForm(instance=item)
        return render(request, 'third2/update.html', {'form': form})
    return HttpResponseRedirect('/third2/list/')


def detail(request, id):
    if id is not None:
        item = get_object_or_404(Restaurants, pk=id)
        reviews = Review.objects.filter(restaurants=item).all()
        return render(request, 'third2/detail.html', {'item': item, 'reviews': reviews})
    return HttpResponseRedirect('/third2/list/')


def delete(request):
    if 'id' in request.GET:
        item = get_object_or_404(Restaurants, pk=request.GET.get('id'))
        item.delete()
    return HttpResponseRedirect('/third2/list/')


def review_create(request, restaurants_id):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            new_item = form.save()
        return redirect('restaurants-detail', id=restaurants_id)

    item = get_object_or_404(Restaurants, pk=restaurants_id)
    form = ReviewForm(initial={'restaurants': item})
    return render(request, 'third2/review_create.html', {'form': form, 'item': item})


def review_delete(request, restaurants_id, review_id):
    item = get_object_or_404(Review, pk=review_id)
    item.delete()

    return redirect('restaurants-detail', id=restaurants_id)


def review_list(request):
    reviews = Review.objects.all().order_by('-created_at')
    paginator = Paginator(reviews, 10)

    page = request.GET.get('page')
    items = paginator.get_page(page)

    context = {
        'reviews': items
    }
    return render(request, 'third2/review_list.html', context)