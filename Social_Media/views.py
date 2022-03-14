from django.shortcuts import render, HttpResponseRedirect
from post.models import Post, Liked
from django.contrib.auth.models import User
from django.db.models import Avg, Min, Max, Count, Sum

def home_page(request, post_id=None, user_id=None):
	posts = Post.objects.all()
	likes = []
	for i in posts:
		like = Liked.objects.filter(post= i).aggregate(Count('post'))
		likes.append(like['post__count'])
	if post_id is not None:
		post = Post.objects.get(pk= post_id)
		user = User.objects.get(pk= user_id)
		alredy_liked = Liked.objects.filter(post= post, user= user)
		flag = False
		for i in alredy_liked:
			flag = True
		if flag == False:
			like = Liked(post = post, user= user)
			like.save()
	return render(request, 'home.html', {'posts':posts, 'likes': likes})