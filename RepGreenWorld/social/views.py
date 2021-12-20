from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import UserRegisterForm, PostForm, CommentForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def feed(request, pk):
	posts = Post.objects.filter(category__id = pk)
	context = { 'posts': posts}
	return render(request, 'social/feed.html',{"posts": posts})

def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST) #Acceso a la informacion enviada a traves del form
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			messages.success(request, f'Usuario {username} creado')
			return redirect('login')
	else:
		form = UserRegisterForm()

	context = { 'form' : form }
	return render(request, 'social/register.html', context)

@login_required
def post(request):
	current_user = get_object_or_404(User, pk=request.user.pk)
	if request.method =='POST':
		form = PostForm(request.POST, request.FILES)
		if form.is_valid():
			post = form.save(commit=False)
			post.user = current_user
			post.save()
			messages.success(request, 'Publicación realizada')
			return redirect('home')
	else: 
		form = PostForm()
		return render(request, 'social/post.html', {'form':form })

def profile(request, username=None):
	current_user = request.user
	if username and username != current_user.username:
		user = User.objects.get(username=username)
		posts = user.posts.all()
	else: 
		posts = current_user.posts.all()
		user = current_user
	return render(request, 'social/profile.html', {'user':user, 'posts':posts})

def follow(request, username):
	current_user = request.user
	to_user = User.objects.get(username=username)
	to_user_id = to_user
	rel = Relationship(from_user=current_user, to_user=to_user_id)
	rel.save()
	messages.success(request, f'Sigues a {username}')
	return redirect('feed')

def unfollow(request, username):
	current_user = request.user
	to_user = User.objects.get(username=username)
	to_user_id = to_user.id
	rel = Relationship.objects.filter(from_user=current_user.id, to_user=to_user_id).get()
	rel.delete()
	messages.success(request, f'Ya no sigues a {username}')
	return redirect('feed')
	
@login_required
def commentpost(request, pk):
    post = get_object_or_404(Post, pk=pk)
    categoryId = post.category.id
    #posts = Post.objects.filter(category__id = pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('feed', categoryId)
    else:
        form = CommentForm()
    return render(request, 'social/add_comment_to_post.html', {'form': form})

def home(request):
	categories = Category.objects.all()

	return render(request, 'social/home.html', {'categories': categories})