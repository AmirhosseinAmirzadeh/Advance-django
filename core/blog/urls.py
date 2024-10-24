from django.urls import path
from .views import indexView
from django.views.generic import TemplateView
from blog import views
from django.views.generic.base import RedirectView

app_name = 'blog'

urlpatterns = [
    path('fbv-index/', indexView, name='fbv-index'),
    # path('cbv-index/', TemplateView.as_view(template_name='blog/index.html', extra_context={"name":"ali"})),
    path('cbv-index/', views.IndexView.as_view(), name='cbv-index'),
    path('go-to-microsoft/', RedirectView.as_view(url='https://www.microsoft.com/'), name='redirect-to-microsoft'),
    path('go-to-bing/', views.RedirectToBing.as_view(), name='redirect-to-bing'),
    path('go-to-index/', RedirectView.as_view(pattern_name='blog:cbv-index'), name='redirect-to-index'),
    path('post/', views.PostListView.as_view(), name='post-list')
]