from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import Category, Item
from .forms import SignUpForm, NewItemForm, EditItemForm
from django.contrib import messages

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

def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, "Login successfully")
            return redirect('home')
        else:
            redirect('user_login')
            
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    messages.success(request, "User logged out")
    return redirect('user_login')

@login_required
def new(request):
    if request.method == "POST":
        form = NewItemForm(request.POST, request.FILES)
        
        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()
            return redirect('detail', pk=item.id)
    else:
        form = NewItemForm()
    
    return render(request, 'form.html', {
        'form': form,
        'title': 'NewItem',
        })

@login_required
def dashboard(request):
    items = Item.objects.filter(created_by=request.user)
    
    return render(request, 'index.html', {'items': items})

@login_required
def delete_item(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    item.delete()
    
    return redirect('dashboard')

@login_required
def edit_item(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    
    if request.method == "POST":
        form = EditItemForm(request.POST or None, request.FILES or None, instance=item)
        
        if form.is_valid():
            form.save()
            return redirect('detail', pk=item.id)
    else:
        form = EditItemForm(instance=item)
    
    return render(request, 'form.html', {
        'form': form,
        'title': 'Edit item',
        })