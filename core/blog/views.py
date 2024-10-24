from typing import Any
from django.shortcuts import render
from django.views.generic.base import TemplateView
from blog.models import Post


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