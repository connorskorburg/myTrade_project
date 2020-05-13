from django.shortcuts import render, redirect
import bcrypt
from .models import *
from django.contrib import messages

# Create your views here.

# RENDER TEMPLATES

# index page
def index(request):
    return render(request, 'index.html')

# register
def register(request):
    return render(request, 'register.html')

# display create account 
def create_profile(request):
    if 'id' not in request.session:
        return redirect('/')
    elif 'id' in request.session:
        user = User.objects.get(id=request.session['id'])
        if user.profile.count() == 0:
            return render(request, 'create_profile.html')
        else:
            return redirect('/login')
# login
def login(request):
    return render(request, 'login.html')

# display user dashboard
def user_dash(request):
    if 'id' not in request.session:
        return redirect('/')
    return render(request, 'user_dash.html')

# display user profile
def user_profile(request):
    if 'id' not in request.session:
        return redirect('/')
    user = User.objects.get(id=request.session['id'])
    context = {
        
    }
    return render(request, 'user_profile.html', context)

# display profile settings
def profile_settings(request):
    if 'id' not in request.session:
        return redirect('/')
    return render(request, 'profile_settings.html')

# display feed
def feed(request):
    if 'id' not in request.session:
        return redirect('/')
    user = User.objects.get(id=request.session['id'])
    user_profile = Profile.objects.get(user=user)
    profiles = Profile.objects.all()
    posts = Post.objects.all()
    context = {
        'profiles': profiles,
        'user': user,
        'user_profile': user_profile,
        'posts': posts,
    }
    return render(request, 'feed.html', context)

# display user account
def user_account(request):
    if 'id' not in request.session:
        return redirect('/')
    return render(request, 'user_account.html')

# display user analytics
def user_analytics(request):
    if 'id' not in request.session:
        return redirect('/')
    return render(request, 'user_analytics.html')

 

# HANDLING POST DATA

# process register
def process_register(request):
    if request.POST['password'] == request.POST['conf_password']:
        password = request.POST['password']
        password_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        # create the user
        new_user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=password_hash)
        request.session['id'] = new_user.id
        request.session['first_name'] = new_user.first_name
        request.session['last_name'] = new_user.last_name
        request.session['email'] = new_user.email
        return redirect('/create_profile')
    else:
        return redirect('/register')

# process profile info
def process_profile(request):
    registered_user = User.objects.get(id=request.session['id'])
    profile = Profile.objects.create(user=registered_user, username=request.POST['username'], bio=request.POST['bio'], avatar=request.POST['av_icon'])    
    return redirect('/user_dash')

# process login
def process_login(request):
    profiles = Profile.objects.all()
    for profile in profiles:
        if profile.username == request.POST['username']:
            if bcrypt.checkpw(request.POST['password'].encode(), profile.user.password.encode()):
                request.session['id'] = profile.user.id
                request.session['first_name'] = profile.user.first_name
                request.session['last_name'] = profile.user.last_name
                request.session['email'] = profile.user.email
                return redirect('/user_dash')
            else:
                return redirect('/login')
        else:
            return redirect('/login')
    return redirect('/login')

# logout
def logout(request):
    request.session.flush()
    return redirect('/')

# create post
def create_post(request):
    user = User.objects.get(id=request.session['id'])
    post = Post.objects.create(content=request.POST['content'], poster=user)
    return redirect('feed.html')