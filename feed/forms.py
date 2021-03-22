from django import forms
from .models import Comments, Post

class NewPostForm(forms.ModelForm):
	description = forms.CharField(widget=forms.Textarea(attrs={
        "rows": "4",
        "placeholder": "write post description",
		
    }))
	tags = forms.CharField(widget=forms.Textarea(attrs={
        "rows": "2",
		"placeholder": "write hashtag,(begin with#)"
    }))
	class Meta:
		model = Post
		fields = ['description', 'pic', 'tags']

class NewCommentForm(forms.ModelForm):
	comment = forms.CharField(widget=forms.Textarea)

	class Meta:
		model = Comments
		fields = ['comment']