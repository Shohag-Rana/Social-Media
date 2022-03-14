from django.shortcuts import render, HttpResponseRedirect
from . forms import PostForm
from . models import Country, Post, Comment, Replay
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.

def update_post(request, uid):
	posts = Post.objects.filter(author = request.user)
	form = PostForm()
	return render(request, 'post/update_post.html', {'posts':posts, 'forms': form})

def view_post(request):
	comments = Comment.objects.all()
	replays = Replay.objects.all()
	if request.user.is_authenticated:
		if request.method == 'POST':
			data = request.POST['comment']
			print(data)
		posts = Post.objects.filter(author = request.user) 
		return render(request, 'post/viewpost.html', {'posts': posts, 'comments': comments, 'replays': replays})
	else:
		return HttpResponseRedirect('/auth/signup/')
	

def delete_post(request):
	pass

def create_post(request):
	if request.user.is_authenticated:
		if request.method == 'POST':
			form = PostForm(request.POST, request.FILES)
			if form.is_valid():
				title = form.cleaned_data['post_title']
				author = request.user
				post_body = form.cleaned_data['post_body']
				country = form.cleaned_data['country']
				city = form.cleaned_data['city']
				feature_photo = form.cleaned_data['feature_photo']

				data = Post(author= author, post_title= title, post_body= post_body, country = country, city = city, feature_photo = feature_photo)
				data.save()
				messages.success(request, 'Your Post Published Successful.')

		form = PostForm()
		return render(request, 'post/createpost.html', {'form': form})
	else:
		return HttpResponseRedirect('/auth/signup/')

def discussion(request, post_id, user_id):
	if request.user.is_authenticated:
		if request.method == 'POST':
			cmnt_body = request.POST['comment']
			user = User.objects.get(pk= user_id)
			post = Post.objects.get(pk= post_id)
			data = Comment(user= user, comment_body= cmnt_body, post= post)
			data.save()
			messages.success(request, 'Your comment added Successfulyy....')
			return HttpResponseRedirect('/post/view_post/')
	else:
		return HttpResponseRedirect('/auth/signup/')


def replay(request, post_id, user_id, cmnt_id):
	if request.user.is_authenticated:
		if request.method == 'POST':
			rep_body = request.POST['replay']
			user = User.objects.get(pk= user_id)
			post = Post.objects.get(pk= post_id)
			comment = Comment.objects.get(pk= cmnt_id)
			data = Replay(user= user, comment= comment, post= post, replay_body= rep_body)
			data.save()
			messages.success(request, 'Your replay added Successfulyy....')
			return HttpResponseRedirect('/post/view_post/')
	else:
		return HttpResponseRedirect('/auth/signup/')

def delete_comment(request, post_id, cmnt_id):
	if request.user.is_authenticated:
		data = Comment.objects.get(pk= cmnt_id)
		data.delete()
		messages.info(request, 'Your Comment is delete successfully....')
		return HttpResponseRedirect('/post/view_post/')
	else:
		return HttpResponseRedirect('/auth/signup/')

def delete_replay(request, rep_id):
	if request.user.is_authenticated:
		data = Replay.objects.get(pk= rep_id)
		data.delete()
		messages.warning(request, 'Your Replay is delete successfully....')
		return HttpResponseRedirect('/post/view_post/')
	else:
		return HttpResponseRedirect('/auth/signup/')
