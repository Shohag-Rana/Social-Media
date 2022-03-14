from django.urls import path
from . import views
 
urlpatterns = [
    path('create_post/', views.create_post, name= "create_post"), 
    path('delete_post/', views.delete_post, name= "delete_post"), 
    path('update_post/<int:uid>/', views.update_post, name= "update_post"), 
    path('view_post/', views.view_post, name= "view_post"),    
    path('comment/<int:post_id>/<int:user_id>/', views.discussion, name= "discussion"),    
    path('replay/<int:post_id>/<int:user_id>/<int:cmnt_id>/', views.replay, name= "replay"),    
    path('del_comment/<int:post_id>/<int:cmnt_id>/', views.delete_comment, name= "delete_comment"),    
    path('del_rep/<int:rep_id>/', views.delete_replay, name= "delete_replay"),    

] 
