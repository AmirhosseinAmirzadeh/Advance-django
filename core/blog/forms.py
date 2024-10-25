from django import forms
from blog.models import Post


class PostForm(forms.Form):
    """
    A class for post form
    """
    class Meta:
        model = Post
        fields = ['author', 'title', 'content', 'status', 'category', 'published_date']