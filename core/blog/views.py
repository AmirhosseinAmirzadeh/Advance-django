from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView, RedirectView
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from blog.models import Post
from blog.forms import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def indexView(request):
    """
    A function based view to show index page
    """
    name = "amirhossein"
    context = {"name":name}
    return render(request, 'index.html', context)


class IndexView(TemplateView):
    """
    A class based view to show blog index page
    """
    template_name = 'base/index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = "Ali"
        context["posts"] = Post.objects.all()
        return context
    

class RedirectToBing(RedirectView):
    """
    A class based view for redirect
    """
    url = 'https://www.bing.com'
    

class PostListView(LoginRequiredMixin, ListView):
    """
    A class based view for post list view
    """
    model = Post
    paginate_by = 3
    ordering = 'id'
    context_object_name = 'posts'
    def get_queryset(self):
        posts = Post.objects.filter(status=True)
        return posts


class PostDetailView(LoginRequiredMixin, DetailView):
    """
    A class for post detail view
    """
    model = Post
    context_object_name = 'post'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    

class PostCreateView(LoginRequiredMixin, CreateView):
    """
    A class for post create view
    """
    model = Post
    fields = '__all__'
    success_url = '/blog/post/'
    
    
class PostEditView(LoginRequiredMixin, UpdateView):
    """
    A class for post edit view
    """
    model = Post
    fields  = '__all__'
    success_url = '/blog/post/'


class PostDeleteView(LoginRequiredMixin, DeleteView):
    """
    A class for post delete view
    """
    model = Post
    success_url = '/blog/post/'