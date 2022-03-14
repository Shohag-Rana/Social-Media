from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Post(models.Model):
	author = models.ForeignKey(User, on_delete= models.CASCADE)
	post_title = models.CharField(max_length=300)
	post_body = models.CharField(max_length=1000)
	country = models.ForeignKey(Country,on_delete=models.CASCADE)
	city = models.CharField(max_length=100)
	post_date = models.DateTimeField(auto_now_add= True)
	feature_photo = models.ImageField(upload_to = 'feature_image', default= False)

	def __str__(self):
		return str(self.post_title)


class Comment(models.Model):
	user = models.ForeignKey(User, on_delete= models.CASCADE, related_name= 'author', default=False)
	comment_body = models.CharField(max_length=1000)
	post = models.ForeignKey(Post, on_delete= models.CASCADE, default=False)
	cmnt_time = models.DateTimeField(auto_now_add= True)

	def __str__(self):
		return str(self.post)


class Replay(models.Model):
	user = models.ForeignKey(User, on_delete= models.CASCADE, related_name= 'rep_author')
	comment = models.ForeignKey(Comment, on_delete= models.CASCADE, related_name= 'comment')
	replay_body = models.CharField(max_length=1000)
	post = models.ForeignKey(Post, on_delete= models.CASCADE, default=False)
	replay_time = models.DateTimeField(auto_now_add= True)

	def __str__(self):
		return str(self.comment)

class Liked(models.Model):
	post = models.ForeignKey(Post, on_delete= models.CASCADE)
	user = models.ForeignKey(User, on_delete= models.CASCADE)
	count = models.IntegerField(default= 0)


	