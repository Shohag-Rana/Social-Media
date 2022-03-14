from django import forms
from . models import Post

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['post_title', 'post_body', 'country', 'city', 'feature_photo']
		field_order = ['post_title', 'post_body', 'post_date', 'country', 'district', 'feature_photo']
		labels = {
		'post_title': 'Title', 'post_body':'Main Content',
		}
		widgets = {
		'post_title': forms.TextInput(attrs={'class': 'form-control'}),
		'city': forms.TextInput(attrs={'class': 'form-control'}),
		'post_body': forms.TextInput(attrs={'class': 'form-control'}),
		'country': forms.Select(attrs={'class': 'form-control'}),
		'feature_photo': forms.FileInput(attrs = {'class': 'form-control'}),
		}