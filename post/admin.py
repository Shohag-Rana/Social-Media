from django.contrib import admin
from . models import Country, Post, Comment, Replay, Liked

# Register your models here.
admin.site.register(Country)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Replay)
admin.site.register(Liked)
