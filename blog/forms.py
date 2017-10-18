from django import forms
from .models import Comment, Post

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ('user','email','body')

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title','author','content','category','seo_title','seo_description','status')

		