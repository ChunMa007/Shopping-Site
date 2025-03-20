from django.shortcuts import render, get_object_or_404
from .models import Category, Item

def getting_started(request):
    return render(request, 'getting_started.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def privacy_and_policy(request):
    return render(request, 'privacy_and_policy.html')

def term_of_use(request):
    return render(request, 'term_of_use.html')

def home(request):
    items = Item.objects.filter(isSold=False)
    categories = Category.objects.all()
    
    return render(request, 'home.html', {
        'items': items, 
        'categories': categories,
    })

def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category=item.category, isSold=False).exclude(pk=pk)
    return render(request, 'detail.html', {
        'item': item,
        'related_items': related_items
        })